from time import sleep

import cyperf
from cyperf.utils import create_api_client_cli, require_ports, validate_ports


def assign_M8400_ports(api_client, config, controller_id):
    """Assign front panel ports on an M8400 chassis to the session's network segments."""
    api_agents_instance = cyperf.AgentsApi(api_client)
    front_panels = api_agents_instance.get_controller_front_panels(controller_id=controller_id)

    if len(front_panels) < 2:
        raise ValueError("Expected at least 2 available front panels")

    for front_panel in front_panels[:2]:
        require_ports(front_panel, min_count=1)

    validate_ports([front_panels[0].ports[0], front_panels[1].ports[0]])

    # Create a front panel port map (each network segment can be assigned one or more front panel ports)
    port_map = {
        'IP Network 1': [front_panels[0].ports[0].id],
        'IP Network 2': [front_panels[1].ports[0].id]
    }

    # Assign the front panel ports
    print("Assigning front panel ports ...")
    for net_profile in config.config.network_profiles:
        for ip_net in net_profile.ip_network_segment:
            if ip_net.name in port_map:
                front_panel_port_ids = port_map[ip_net.name]
                print(f"Front panel port(s) {', '.join(front_panel_port_ids)} assigned to {ip_net.name}.")
                capture_settings = None                                         # CaptureSettings | The capture settings of the front panel port that is assigned (optional)
                compute_resources_by_type = {"APS-ONE-400:non-aggregated":2}    # Dict[str, int] | The number of compute resources to assign per compute node type & aggregation (necessary)
                links = None                                                    # List[APILink] |  (optional)
                port_details = [cyperf.AgentAssignmentByFrontPanelPort(capture_settings=capture_settings,
                                                                        compute_resources_by_type=compute_resources_by_type,
                                                                        front_panel_port_id=front_panel_port_id,
                                                                        id=front_panel_port_id,
                                                                        links=links)
                                 for front_panel_port_id in front_panel_port_ids]
                if not ip_net.agent_assignments:
                    by_front_panel_port = None                  # List[AgentAssignmentByFrontPanelPort] | The front panel ports assigned to the current test configuration (necessary)
                    by_id = None                                # List[AgentAssignmentDetails] | The agents statically assigned to the current test configuration (optional)
                    by_port	= None                              # List[AgentAssignmentByPort] | The ports assigned to the current test configuration (incompatible with M8400)
                    by_tag = None                               # List[str]	| The tags according to which the agents are dynamically assigned (incompatible with M8400)
                    ip_net.agent_assignments = cyperf.AgentAssignments(by_front_panel_port=by_front_panel_port,
                                                                       by_id=by_id,
                                                                       by_port=by_port,
                                                                       by_tag=by_tag,
                                                                       links=links)
                ip_net.agent_assignments.by_front_panel_port = port_details
                ip_net.update()
    print("Assigning front panel ports completed.\n")


def _assign_by_port_ids(config, port_map):
    """Assign the given port_map (network segment name -> list of port IDs) to the session's network segments."""
    print("Assigning ports ...")
    for net_profile in config.config.network_profiles:
        for ip_net in net_profile.ip_network_segment:
            if ip_net.name in port_map:
                port_ids = port_map[ip_net.name]
                print(f"Port(s) {', '.join(port_ids)} assigned to {ip_net.name}.")
                capture_settings = None                         # CaptureSettings | The capture settings of the port that is assigned (optional)
                links = None                                    # List[APILink] |  (optional)
                port_details = [cyperf.AgentAssignmentByPort(capture_settings=capture_settings,
                                                              port_id=port_id,
                                                              id=port_id,
                                                              links=links)
                                 for port_id in port_ids]
                if not ip_net.agent_assignments:
                    by_front_panel_port = None                  # List[AgentAssignmentByFrontPanelPort] | The front panel ports assigned to the current test configuration (compatible with M8400)
                    by_id = None                                # List[AgentAssignmentDetails] | The agents statically assigned to the current test configuration (optional)
                    by_port	= None                              # List[AgentAssignmentByPort] | The ports assigned to the current test configuration (optional)
                    by_tag = None                               # List[str]	| The tags according to which the agents are dynamically assigned
                    ip_net.agent_assignments = cyperf.AgentAssignments(by_front_panel_port=by_front_panel_port,
                                                                       by_id=by_id,
                                                                       by_port=by_port,
                                                                       by_tag=by_tag,
                                                                       links=links)
                ip_net.agent_assignments.by_port = port_details
                ip_net.update()
    print("Assigning ports completed.\n")


def assign_M1010_ports(api_client, config, controller_id):
    """Assign ports from a single M1010 compute node to the session's network segments."""
    api_agents_instance = cyperf.AgentsApi(api_client)
    compute_nodes = api_agents_instance.get_controller_compute_nodes(controller_id=controller_id)

    if len(compute_nodes) == 0:
        raise ValueError("Expected at least one available compute node")

    compute_node_ports = require_ports(compute_nodes[0], min_count=4)

    validate_ports(compute_node_ports[:4])

    # Ports are wired as loopback pairs (0<->2, 1<->3)
    port_map = {
        'IP Network 1': [compute_node_ports[0].id, compute_node_ports[1].id],
        'IP Network 2': [compute_node_ports[2].id, compute_node_ports[3].id]
    }

    _assign_by_port_ids(config, port_map)


def assign_novusminipro_ports(api_client, config, controller_id):
    """Assign ports from a NovusMiniPro's 'mgmt' compute node to the session's network segments."""
    api_agents_instance = cyperf.AgentsApi(api_client)
    compute_node_mgmt = api_agents_instance.get_controller_compute_node_by_id(controller_id=controller_id, compute_node_id="mgmt")
    ports = require_ports(compute_node_mgmt, min_count=4)

    validate_ports(ports[:4])

    # Ports are assumed to be wired as loopback pairs (0<->1, 2<->3)
    port_map = {
        'IP Network 1': [ports[0].id, ports[1].id],
        'IP Network 2': [ports[2].id, ports[3].id]
    }

    _assign_by_port_ids(config, port_map)


# Maps a platform name to its port assignment function and default controller ID.
# Add a new entry here (and a corresponding assign_*_ports function above) to support another platform.
PLATFORMS = {
    'M8400': (assign_M8400_ports, "chs-001"),
    'M1010': (assign_M1010_ports, "chs-001"),
    'novusminipro': (assign_novusminipro_ports, "nvm1"),
}


if __name__ == "__main__":
    import urllib3; urllib3.disable_warnings()

    # Select which hardware platform to run against, then replace that platform's
    # controller ID in PLATFORMS above with your own (see AgentsApi.get_controllers())
    platform = 'M1010'                             # one of: 'M8400', 'M1010', 'novusminipro'
    if platform not in PLATFORMS:
        raise ValueError(f"Unknown platform '{platform}', expected one of {list(PLATFORMS)}")
    assign_ports, controller_id = PLATFORMS[platform]

    # Enter a context with an instance of the API client
    with create_api_client_cli(verify_ssl=False) as api_client:
        # Find the pre-canned config
        api_config_instance  = cyperf.ConfigurationsApi(api_client)
        take = 1                                                        # int | The number of search results to return (optional)
        skip = None	                                                    # int | The number of search results to skip (optional)
        search_col = 'displayName'                                      # str | A list of comma-separated columns used to search for the supplied values (optional)
        search_val = 'Not Working From Home Traffic Mix'                # str | The keywords used to filter the items (optional)
        filter_mode = None                                              # str | The operator applied to the supplied values (optional)
        sort = None                                                     # str | A list of comma-separated field:direction pairs used to sort the items where direction must be asc or dsc (optional)
        config = api_config_instance.get_configs(take=1,
                                                 skip=skip,
                                                 search_col=search_col,
                                                 search_val=search_val,
                                                 filter_mode=filter_mode,
                                                 sort=sort)

        if len(config.data) == 0:
            raise ValueError("Couldn't find the specified configuration.")

        # Load a pre-canned config
        api_session_instance = cyperf.SessionsApi(api_client)
        application	= None                                          # str | The user-friendly name for the application that controls this session (optional)
        config_name	= None                                          # str | The display name of the configuration loaded in the session (optional)
        config_url = config.data[0].config_url                      # str | The external URL of the configuration loaded in the session (optional)
        index = None                                                # int | The session's index (optional) (readonly)
        name = None                                                 # str | The user-visible name of the session (optional)
        owner = None                                                # str | The user-visible name of the session's owner (optional) (readonly)
        sessions = [cyperf.Session(application=application,
                                   config_name=config_name,
                                   configUrl=config_url,
                                   index=index,
                                   name=name,
                                   owner=owner)]

        # Create a session
        session = None
        print(f"Creating session from config called {search_val} ...")
        api_session_response = api_session_instance.create_sessions(sessions=sessions)
        session = api_session_response[0]
        print("Session created.\n")

        # Get the configuration of the created session
        include = 'Config, TrafficProfiles'                          # str | Specifies if the sub-fields that are objects should be included (eg. 'Config'). (optional)
        config = api_session_instance.get_session_config(session_id=session.id, include=include)

        # Modify test duration
        config.config.traffic_profiles[0].objectives_and_timeline.primary_objective.timeline[1].duration = 30
        config.config.traffic_profiles[0].objectives_and_timeline.primary_objective.update()

        # Assign the ports/front panels for the selected platform
        assign_ports(api_client, config, controller_id)

        # Start traffic
        print("Starting the test ...")
        api_test_operation_instance = cyperf.TestOperationsApi(api_client)
        api_test_operation_response = api_test_operation_instance.start_test_run_start(session_id=session.id)
        api_test_operation_response.await_completion()

        # Wait for the test to be finished
        print("Test running ...")
        session.refresh()
        while session.test.status != 'STOPPED':
            sleep(5)
            session.refresh()
        print("Test finished successfully.\n")

        # Download the test results
        print("Downloading test results ...")
        api_test_results_instance = cyperf.TestResultsApi(api_client)
        generate_all_operation = cyperf.GenerateAllOperation()
        api_test_results_response = api_test_results_instance.start_result_generate_all(result_id=session.test.test_id, generate_all_operation=generate_all_operation)
        file_path = api_test_results_response.await_completion()

        last_separator_index = file_path.rfind("\\")
        directory = file_path[:last_separator_index]
        file_name = file_path[last_separator_index + 1:]

        print(f"Saved as: '{file_name}' at {directory}\n")
