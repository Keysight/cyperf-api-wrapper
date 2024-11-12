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

from cyperf.models.emulated_router_range import EmulatedRouterRange

class TestEmulatedRouterRange(unittest.TestCase):
    """EmulatedRouterRange unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EmulatedRouterRange:
        """Test EmulatedRouterRange
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EmulatedRouterRange`
        """
        model = EmulatedRouterRange()
        if include_optional:
            return EmulatedRouterRange(
                automatic_ip_type = 'BOTH_IPV4_IPV6',
                count = 56,
                gw_auto = True,
                gw_start = '::02:84:9:0cc0:F:CCf',
                host_count = 56,
                inner_vlan_range = cyperf.models.vlan_range.VLANRange(
                    count = 56, 
                    count_per_agent = 56, 
                    max_count_per_agent = 56, 
                    priority = 56, 
                    static_arp_table = [
                        cyperf.models.static_arp_entry.StaticARPEntry(
                            count = 56, 
                            remote_ip = '::02:84:9:0cc0:F:CCf', 
                            remote_ip_incr = '::02:84:9:0cc0:F:CCf', 
                            remote_mac = '2E-B0-08-29:0c:01', 
                            remote_mac_incr = '2E-B0-08-29:0c:01', 
                            static_arp_entry_name = 'YBuLd', 
                            id = '', )
                        ], 
                    tag_protocol_id = 33024, 
                    vlan_auto = True, 
                    vlan_enabled = True, 
                    vlan_id = 56, 
                    vlan_incr = 56, 
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
                ip_auto = True,
                ip_incr = '::02:84:9:0cc0:F:CCf',
                ip_range_name = 'YBuLd',
                ip_start = '::02:84:9:0cc0:F:CCf',
                ip_ver = 'IPV4',
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
                    ]
            )
        else:
            return EmulatedRouterRange(
                gw_auto = True,
                ip_auto = True,
                ip_range_name = 'YBuLd',
                ip_ver = 'IPV4',
                mss = 56,
                mss_auto = True,
                net_mask_auto = True,
                id = '',
        )
        """

    def testEmulatedRouterRange(self):
        """Test EmulatedRouterRange"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
