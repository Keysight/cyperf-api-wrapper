from dataclasses import dataclass, field

import cyperf
from cyperf import AgentAssignments, IPNetwork, DUTNetwork, Address, DUTRange
from cyperf.utils import parse_cli_options

BASE_CONFIG_NAME = "Cyperf Empty Config"

OUTER_VLAN_ID = 200
OUTER_VLAN_INCR = 1
OUTER_VLAN_COUNT = 1
OUTER_TPID = 0x88A8
OUTER_INCREMENT_EVERY_NO_OF_IPS = 1
OUTER_PRIORITY = 0

INNER_VLAN_ID = 100
INNER_VLAN_INCR = 1
INNER_VLAN_COUNT = 1
INNER_TPID = 0x8100
INNER_INCREMENT_EVERY_NO_OF_IPS = 1
INNER_PRIORITY = 0
HTTP_APP_SEARCH = "HTTP App"
DEFAULT_MSS = 1460

DEFAULT_COUNT = 18
DEFAULT_SUB_STEP_COUNT = 3
DEFAULT_CLIENT_START_IP="10.0.0.10"
DEFAULT_SERVER_START_IP="10.0.0.40"
DEFAULT_IP_INCREMENT="0.1.0.0"

DEFAULT_CLIENT_START_MAC="10:00:00:00:00:10"
DEFAULT_SERVER_START_MAC="20:00:00:00:00:00"
DEFAULT_MAC_INCREMENT="00:00:00:01:00:00"

@dataclass
class StepNode:
    step: str
    count: int = field(default=DEFAULT_SUB_STEP_COUNT)
    sub_steps: list["StepNode"] = field(default_factory=list)

    def to_substep(self):
        return _step_s(
            step=self.step,
            count=self.count,
            sub_steps=[c.to_substep() for c in self.sub_steps],
        )

IP_SUBSTEPS=[
    StepNode(step="0.0.1.0", sub_steps=[StepNode("0.0.0.1")]),
    StepNode(step="0.0.2.0", sub_steps=[StepNode("0.0.0.2")]),
]

MAC_SUBSTEPS=[
    StepNode(step="00:00:00:00:01:00", sub_steps=[StepNode("00:00:00:00:00:01")]),
    StepNode(step="00:00:00:00:02:00", sub_steps=[StepNode("00:00:00:00:00:02")]),
]

def _create_api_client_from_cli():
    args, offline_token = parse_cli_options(
        extra_options=[
            ("--client-agent-ip", "Agent IP to assign to IP Network 1", True),
            ("--server-agent-ip", "Agent IP to assign to IP Network 2", True),
        ]
    )

    configuration = cyperf.Configuration(
        host=f"https://{args.controller}",
        refresh_token=offline_token,
        username=args.user,
        password=args.password,
    )
    configuration.verify_ssl = False
    api_client = cyperf.ApiClient(configuration)

    return api_client, args.client_agent_ip, args.server_agent_ip

def _find_config_url(api_client, config_name: str) -> str:
    configs_api = cyperf.ConfigurationsApi(api_client)
    configs = configs_api.get_configs(
        take=1,
        search_col="displayName",
        search_val=config_name,
    )

    if not configs.data:
        raise ValueError(f"Configuration '{config_name}' was not found.")

    return configs.data[0].config_url

def _create_session(api_client, config_url: str):
    sessions_api = cyperf.SessionsApi(api_client)
    sessions = sessions_api.create_sessions([cyperf.Session(config_url=config_url)])
    if not sessions:
        raise RuntimeError("Failed to create session.")
    return sessions[0]

def _add_application_profile_with_http_app(api_client, session):
    sessions_api = cyperf.SessionsApi(api_client)
    app_resources_api = cyperf.ApplicationResourcesApi(api_client)

    traffic_profiles = session.config.config.traffic_profiles
    existing_profiles = len(traffic_profiles) if traffic_profiles else 0
    traffic_profiles.append(cyperf.ApplicationProfile(Name="Application Profile"))
    traffic_profiles.update()

    apps = app_resources_api.get_resources_apps(
        take=1,
        skip=0,
        search_col="Name",
        search_val=HTTP_APP_SEARCH,
        sort="Name:asc",
    )
    if not apps.data:
        raise ValueError(f"No application found for search value '{HTTP_APP_SEARCH}'.")

    app = apps.data[0]
    traffic_profile_id = str(existing_profiles + 1)
    operation = sessions_api.start_config_add_applications(
        session.id,
        traffic_profile_id,
        external_resource_info=[
            cyperf.ExternalResourceInfo(externalResourceURL=str(app.id))
        ],
    )
    operation.await_completion()

def _ip_range(name: str, count: int):
    return cyperf.IPRange(
        GwAuto=False,
        IpAuto=False,
        IpRangeName=name,
        MssAuto=True,
        Mss=DEFAULT_MSS,
        NetMaskAuto=False,
        NetMask=16,
        VLANType=cyperf.VLANType.VLAN_NONE,
        HostCount=1,
        IpVer=cyperf.IpVer.IPV4,
        Count=count,
        GwStart="10.0.0.1",
    )

def _create_ip_range(ip_net, count, ip_address_seq: cyperf.SequenceValue, inner_vlan: cyperf.VLANRange | None = None, outer_vlan: cyperf.VLANRange | None = None):
    default_ip_range = _ip_range(f"{ip_net.name} Range 1", count)
    ip_net.ip_ranges = [default_ip_range]
    ip_net.ip_ranges.update()
    ip_range = ip_net.ip_ranges[0]
    ip_range.ip_auto = False
    ip_range.gw_auto = False
    ip_range.count = count
    ip_range.max_count_per_agent = count
    ip_range.gw_start = "10.0.0.0"
    ip_range.mss = DEFAULT_MSS
    ip_range.ip_address = ip_address_seq
    if inner_vlan is not None:
        ip_range.vlan_type = cyperf.VLANType.VLAN
        ip_range.inner_vlan_range = inner_vlan
    if outer_vlan is not None:
        ip_range.vlan_type = cyperf.VLANType.VLAN_IN_VLAN
        ip_range.outer_vlan_range = outer_vlan

    ip_range.update()

def _ip_seq(seq_type: cyperf.SequenceValueTypes, ip_start: str, increment: str, sub_steps: list[cyperf.SubStep] | None = None):
    return _sequence(seq_type, ip_start, increment, cyperf.SequenceDataTypes.IP_SEQ, *(sub_steps or []))

def _mac_seq(seq_type: cyperf.SequenceValueTypes, ip_start: str, increment: str, sub_steps: list[cyperf.SubStep] | None = None):
    return _sequence(seq_type, ip_start, increment, cyperf.SequenceDataTypes.MAC_SEQ, *(sub_steps or []))

def _step_s(step: str, count: int, sub_steps: list[cyperf.SubStep] | None = None):
    return cyperf.SubStep(
        Step=cyperf.SingleValue(
            StringValue=step,
        ),
        Count=count,
        SubSteps=sub_steps or []
    )

def _dut_address(count: int, ip_seq: cyperf.SequenceValue, inner_vlan: cyperf.VLANRange | None = None, outer_vlan: cyperf.VLANRange | None = None):
    address = Address(
        UseRange=True,
        Range=DUTRange(
            Count=count,
            Ip=ip_seq,
            VLANType=cyperf.VLANType.VLAN_NONE
        )
    )
    if inner_vlan is not None:
        address.range.vlan_type = cyperf.VLANType.VLAN
        address.range.inner_vlan_range = inner_vlan
    if outer_vlan is not None:
        address.range.vlan_type = cyperf.VLANType.VLAN_IN_VLAN
        address.range.outer_vlan_range = outer_vlan
    return address

def _dut(inner_vlan: cyperf.VLANRange | None = None, outer_vlan: cyperf.VLANRange | None = None):
    dut_seq = _ip_seq(
        seq_type=cyperf.SequenceValueTypes.CUSTOM,
        ip_start=DEFAULT_SERVER_START_IP,
        increment=DEFAULT_IP_INCREMENT,
        sub_steps=[n.to_substep() for n in IP_SUBSTEPS]
    )
    return DUTNetwork(
        id="1",
        Name="DUT Network 1",
        ConfigSettings="ADVANCED_MODE",
        ServerDUTAddress=_dut_address(
            count=DEFAULT_COUNT,
            ip_seq=dut_seq,
            inner_vlan=inner_vlan,
            outer_vlan=outer_vlan),
        active=True,
        ServerDUTActive=True,
    )

def _sequence(seq_type: cyperf.SequenceValueTypes, ip_start: str, increment: str, seq_data_type: cyperf.SequenceDataTypes, *sub_steps: cyperf.SubStep):
    return cyperf.SequenceValue(
        SequenceType=seq_type,
        Custom=cyperf.CustomSequence(
            Start=cyperf.SingleValue(
                StringValue=ip_start
            ),
            Step=cyperf.SingleValue(
                StringValue=increment
            ),
            SubSteps=list(sub_steps),
        ),
        Increment=cyperf.SimpleSequenceValue(
            Start=cyperf.SingleValue(
                StringValue=ip_start
            ),
            Step=cyperf.SingleValue(
                StringValue=increment
            ),
        ),
        DataType=seq_data_type,
    )

def _vlan_range(vlan_range_name: str, vlan_id: int, vlan_incr: int, vlan_count: int, tpid: int, increment_every_no_of_ips: int = 1, priority: int = 0,
):
    vlan_range = cyperf.VLANRange(VlanAuto=False, VlanRangeName=vlan_range_name, VlanId=vlan_id)
    vlan_range.vlan_auto = False
    vlan_range.vlan_id = vlan_id
    vlan_range.vlan_incr = vlan_incr
    vlan_range.count = vlan_count
    vlan_range.priority = priority
    vlan_range.tag_protocol_id = tpid
    vlan_range.count_per_agent = 1
    vlan_range.increment_every_no_of_ips = increment_every_no_of_ips
    return vlan_range

def configure_networks(session, dut_id: str | None = None):
    if not session.config.config.network_profiles:
        raise ValueError("Session configuration has no network profiles.")

    dut_connections: list[str] = ["1"]
    if dut_id is not None:
        dut_connections = [dut_id]
    client_net = IPNetwork(Name="IP Network 1", id="1", agentAssignments=AgentAssignments(ByID=[], ByTag=[]), minAgents=1, IPRanges=[], DUTConnections=dut_connections)
    server_net = IPNetwork(Name="IP Network 2", id="2", agentAssignments=AgentAssignments(ByID=[], ByTag=[]), minAgents=1, IPRanges=[], DUTConnections=dut_connections)
    session.config.config.network_profiles[0].ip_network_segment = [client_net, server_net]
    session.config.config.network_profiles[0].ip_network_segment.update()

def configure_dut(session, inner_vlan: cyperf.VLANRange | None = None, outer_vlan: cyperf.VLANRange | None = None):
    if not session.config.config.network_profiles:
        raise ValueError("Session configuration has no network profiles.")

    session.config.config.network_profiles[0].dut_network_segment = [_dut(inner_vlan, outer_vlan)]
    session.config.config.network_profiles[0].dut_network_segment.update()

    return session.config.config.network_profiles[0].dut_network_segment[0].id

def configure_ip_ranges(session, inner_vlan: cyperf.VLANRange | None = None, outer_vlan: cyperf.VLANRange | None = None):
    client_net = session.config.config.network_profiles[0].ip_network_segment[0]
    server_net = session.config.config.network_profiles[0].ip_network_segment[1]
    _create_ip_range(client_net, DEFAULT_COUNT, _ip_seq(
        seq_type=cyperf.SequenceValueTypes.INCREMENT,
        ip_start=DEFAULT_CLIENT_START_IP,
        increment=DEFAULT_IP_INCREMENT
    ), inner_vlan, outer_vlan)
    _create_ip_range(server_net, DEFAULT_COUNT, _ip_seq(
        seq_type=cyperf.SequenceValueTypes.CUSTOM,
        ip_start=DEFAULT_SERVER_START_IP,
        increment=DEFAULT_IP_INCREMENT,
        sub_steps=[n.to_substep() for n in IP_SUBSTEPS]
    ), inner_vlan, outer_vlan)

def _mac_dtls(name: str, inner_vlan: cyperf.VLANRange | None = None, outer_vlan: cyperf.VLANRange | None = None):
    mac_dtls_stack = cyperf.MacDtlsStack(
        id="1",
        DTLSRangeName=name,
        TunnelDestinationMacStart="AA:BB:CC:DD:EE:FF",
        TunnelDestinationMacIncr="00:00:00:00:00:01",
        InIV="0x22222222",
        InIVIncr="0x00000001",
        InKey="0xBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
        InKeyIncr="0x0000000000000000000000000000000000000000000000000000000000000001",
        OutIV="0x11111111",
        OutIVIncr="0x00000001",
        OutKey="0xAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
        OutKeyIncr="0x0000000000000000000000000000000000000000000000000000000000000001",
        TunnelCount=1
    )
    mac_dtls_stack.ip_range = _ip_range(f"{name} IP Range 1", DEFAULT_COUNT)
    if inner_vlan is not None:
        mac_dtls_stack.vlan_type = cyperf.VLANType.VLAN
        mac_dtls_stack.vlan_range = inner_vlan
    if outer_vlan is not None:
        mac_dtls_stack.vlan_type = cyperf.VLANType.VLAN_IN_VLAN
        mac_dtls_stack.outer_vlan_range = outer_vlan
    return mac_dtls_stack

def configure_mac_dtls(session, inner_vlan: cyperf.VLANRange | None = None, outer_vlan: cyperf.VLANRange | None = None):
    client_net = session.config.config.network_profiles[0].ip_network_segment[0]
    server_net = session.config.config.network_profiles[0].ip_network_segment[1]
    client_net.mac_dtls_stacks = [_mac_dtls("Client MAC-DTLS 1", inner_vlan, outer_vlan)]
    server_net.mac_dtls_stacks = [_mac_dtls("Server MAC-DTLS 1", inner_vlan, outer_vlan)]
    client_net.mac_dtls_stacks.update()
    server_net.mac_dtls_stacks.update()

    client_mac_dtls = client_net.mac_dtls_stacks[0]
    client_mac_dtls.dtls_enabled = False
    client_mac_dtls.update()

    client_ip_range = client_mac_dtls.ip_range
    client_ip_range.ip_address = _ip_seq(
        seq_type=cyperf.SequenceValueTypes.INCREMENT,
        ip_start=DEFAULT_CLIENT_START_IP,
        increment=DEFAULT_IP_INCREMENT
    )
    client_ip_range.update()

    server_mac_dtls = server_net.mac_dtls_stacks[0]
    server_mac_dtls.dtls_enabled = False
    server_mac_dtls.update()

    server_ip_range = server_mac_dtls.ip_range
    server_ip_range.ip_address =  _ip_seq(
        seq_type=cyperf.SequenceValueTypes.CUSTOM,
        ip_start=DEFAULT_SERVER_START_IP,
        increment=DEFAULT_IP_INCREMENT,
        sub_steps=[n.to_substep() for n in IP_SUBSTEPS]
    )
    server_ip_range.update()


def configure_ethernet(session):
    client_net = session.config.config.network_profiles[0].ip_network_segment[0]
    server_net = session.config.config.network_profiles[0].ip_network_segment[1]

    client_net.eth_range.mac_auto = False
    client_net.eth_range.one_mac_per_ip = False
    client_net.eth_range.mac_address = _mac_seq(
        seq_type=cyperf.SequenceValueTypes.INCREMENT,
        ip_start=DEFAULT_CLIENT_START_MAC,
        increment=DEFAULT_MAC_INCREMENT,
    )
    client_net.eth_range.update()
    server_net.eth_range.mac_auto = False
    server_net.eth_range.one_mac_per_ip = False
    server_net.eth_range.mac_address = _mac_seq(
        seq_type=cyperf.SequenceValueTypes.CUSTOM,
        ip_start=DEFAULT_SERVER_START_MAC,
        increment=DEFAULT_MAC_INCREMENT,
        sub_steps=[n.to_substep() for n in MAC_SUBSTEPS]
    )
    server_net.eth_range.update()

def assign_agents_by_ip(api_client, session, network_to_agent_ip):
    agents_api = cyperf.AgentsApi(api_client)
    available_agents = agents_api.get_agents(exclude_offline="true")
    available_by_ip = {agent.ip: agent for agent in available_agents}

    net_profile = session.config.config.network_profiles[0]

    for idx, ip_net in enumerate(net_profile.ip_network_segment):
        if ip_net.name not in network_to_agent_ip:
            continue

        agent_ip = network_to_agent_ip[ip_net.name]
        if agent_ip not in available_by_ip:
            raise ValueError(
                f"Agent IP '{agent_ip}' is not connected or is offline."
            )

        agent = available_by_ip[agent_ip]
        agent_details = [cyperf.AgentAssignmentDetails(agentId=agent.id, id = str(idx))]
        ip_net.agent_assignments.by_id = agent_details
        ip_net.agent_assignments.update()

if __name__ == "__main__":
    import urllib3

    urllib3.disable_warnings()

    api_client, client_agent_ip, server_agent_ip = _create_api_client_from_cli()

    with api_client:
        config_url = _find_config_url(api_client, BASE_CONFIG_NAME)
        session = _create_session(api_client, config_url)

        print(f"Session created: {session.id}")
        print("Creating application profile with HTTP app...")
        _add_application_profile_with_http_app(api_client, session)


        print("Applying Network settings...")

        #without VLAN
        inner_vlan = None
        outer_vlan = None

        #with VLAN
        inner_vlan = _vlan_range('inner_vlan', INNER_VLAN_ID, INNER_VLAN_INCR, INNER_VLAN_COUNT, INNER_TPID, 1, INNER_PRIORITY)
        outer_vlan = _vlan_range('outer_vlan', OUTER_VLAN_ID, OUTER_VLAN_INCR, OUTER_VLAN_COUNT, OUTER_TPID, 1, OUTER_PRIORITY)

        print("Configuring DUT")
        dut_id = None

        #uncomment this line for plain IP, comment it for MAC DTLS
        dut_id = configure_dut(session, inner_vlan, outer_vlan)
        print("Configuring Networks")
        configure_networks(session, dut_id)
        print("Configuring ethernet for networks")
        configure_ethernet(session)
        print("Configuring IP ranges for networks")

        #uncomment this line for plain IP, comment it for MAC DTLS
        configure_ip_ranges(session, inner_vlan, outer_vlan)

        #uncomment this line for MAC DTLS, comment it for plain IP
        # configure_mac_dtls(session, inner_vlan, outer_vlan)
        print("Network configured successfully.")

        print("Assigning agents by IP...")
        assign_agents_by_ip(
            api_client,
            session,
            {
                "IP Network 1": client_agent_ip,
                "IP Network 2": server_agent_ip,
            },
        )

        print("Test is now configured!")
