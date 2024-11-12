# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Contact: support@keysight.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cyperf.models.ip_network import IPNetwork

class TestIPNetwork(unittest.TestCase):
    """IPNetwork unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IPNetwork:
        """Test IPNetwork
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IPNetwork`
        """
        model = IPNetwork()
        if include_optional:
            return IPNetwork(
                name = 'YBuLd',
                id = '',
                network_tags = [
                    ''
                    ],
                dns_resolver = cyperf.models.dns_resolver.DNSResolver(
                    cache_timeout = 56, 
                    enable_perconnect = True, 
                    links = [
                        cyperf.models.api_link.APILink(
                            content_type = '', 
                            href = '', 
                            method = '', 
                            name = '', 
                            references_count = 56, 
                            rel = '', 
                            type = '', )
                        ], 
                    name_servers = [
                        cyperf.models.name_server.NameServer(
                            name = '4.207.188.200', )
                        ], ),
                dns_server = cyperf.models.dns_server.DNSServer(
                    enabled = True, 
                    port = 56, ),
                dut_connections = [
                    ''
                    ],
                emulated_router = None,
                eth_range = None,
                ip_ranges = [
                    cyperf.models.ip_range.IPRange(
                        automatic_ip_type = null, 
                        count = 56, 
                        gw_auto = True, 
                        gw_start = '::02:84:9:0cc0:F:CCf', 
                        host_count = 56, 
                        inner_vlan_range = null, 
                        ip_auto = True, 
                        ip_incr = '::02:84:9:0cc0:F:CCf', 
                        ip_range_name = 'YBuLd', 
                        ip_start = '::02:84:9:0cc0:F:CCf', 
                        ip_ver = null, 
                        is_emulated_router = True, 
                        mss = 56, 
                        mss_auto = True, 
                        net_mask = 56, 
                        net_mask_auto = True, 
                        id = '', 
                        links = [
                            cyperf.models.api_link.APILink(
                                content_type = '', 
                                href = '', 
                                method = '', 
                                name = '', 
                                references_count = 56, 
                                rel = '', 
                                type = '', )
                            ], 
                        max_count_per_agent = 56, 
                        network_tags = [
                            ''
                            ], )
                    ],
                ip_sec_stacks = [
                    cyperf.models.ip_sec_stack.IPSecStack(
                        ca_certificate_file = null, 
                        emulated_sub_config = null, 
                        enable_rekey = True, 
                        ip_sec_range = null, 
                        ip_sec_stack_name = 'YBuLd', 
                        local_sub_config = null, 
                        log_keys = True, 
                        max_initiation_rate = 56, 
                        max_pending = 56, 
                        outer_ip_range = null, 
                        rekey_margin = 56, 
                        rekey_retry_count = 56, 
                        retransmission_timeout = 56, 
                        retry_count = 56, 
                        retry_interval = 56, 
                        retry_interval_increment = 56, 
                        setup_timeout = 56, 
                        stack_role = 'INITIATOR', 
                        id = '', 
                        links = [
                            cyperf.models.api_link.APILink(
                                content_type = '', 
                                href = '', 
                                method = '', 
                                name = '', 
                                references_count = 56, 
                                rel = '', 
                                type = '', )
                            ], )
                    ],
                mac_dtls_stacks = [
                    cyperf.models.mac_dtls_stack.MacDtlsStack(
                        dtls_enabled = True, 
                        dtls_range_name = 'YBuLd', 
                        epoch = 56, 
                        epoch_incr = 56, 
                        ip_range = null, 
                        in_iv = '0x62ECB020', 
                        in_iv_incr = '0x62ECB020', 
                        in_key = '0x62ECB020842930cc01FFCCfeEe150AC32DcAEc8a83DDD7dBF7567C88195ffcea', 
                        in_key_incr = '0x62ECB020842930cc01FFCCfeEe150AC32DcAEc8a83DDD7dBF7567C88195ffcea', 
                        network_meshing = null, 
                        out_iv = '0x62ECB020', 
                        out_iv_incr = '0x62ECB020', 
                        out_key = '0x62ECB020842930cc01FFCCfeEe150AC32DcAEc8a83DDD7dBF7567C88195ffcea', 
                        out_key_incr = '0x62ECB020842930cc01FFCCfeEe150AC32DcAEc8a83DDD7dBF7567C88195ffcea', 
                        tunnel_count = 56, 
                        tunnel_destination_mac_incr = '2E-B0-08-29:0c:01', 
                        tunnel_destination_mac_start = '2E-B0-08-29:0c:01', 
                        vlan_range = null, 
                        id = '', 
                        links = [
                            cyperf.models.api_link.APILink(
                                content_type = '', 
                                href = '', 
                                method = '', 
                                name = '', 
                                references_count = 56, 
                                rel = '', 
                                type = '', )
                            ], )
                    ],
                tunnel_stacks = [
                    cyperf.models.tunnel_stack.TunnelStack(
                        inner_ip_range = null, 
                        outer_ip_range = null, 
                        tunnel_range = null, 
                        tunnel_stack_name = 'YBuLd', 
                        id = '', 
                        links = [
                            cyperf.models.api_link.APILink(
                                content_type = '', 
                                href = '', 
                                method = '', 
                                name = '', 
                                references_count = 56, 
                                rel = '', 
                                type = '', )
                            ], )
                    ],
                active = True,
                agent_assignments = cyperf.models.agent_assignments.AgentAssignments(
                    by_id = [
                        null
                        ], 
                    by_port = [
                        null
                        ], 
                    by_tag = [
                        ''
                        ], 
                    links = [
                        cyperf.models.api_link.APILink(
                            content_type = '', 
                            href = '', 
                            method = '', 
                            name = '', 
                            references_count = 56, 
                            rel = '', 
                            type = '', )
                        ], ),
                links = [
                    cyperf.models.api_link.APILink(
                        content_type = '', 
                        href = '', 
                        method = '', 
                        name = '', 
                        references_count = 56, 
                        rel = '', 
                        type = '', )
                    ],
                min_agents = 56
            )
        else:
            return IPNetwork(
                name = 'YBuLd',
                id = '',
        )
        """

    def testIPNetwork(self):
        """Test IPNetwork"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
