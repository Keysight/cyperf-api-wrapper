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

from cyperf.models.eth_range import EthRange

class TestEthRange(unittest.TestCase):
    """EthRange unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EthRange:
        """Test EthRange
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EthRange`
        """
        model = EthRange()
        if include_optional:
            return EthRange(
                count = 56,
                mac_auto = True,
                mac_incr = '2E-B0-08-29:0c:01',
                mac_start = '2E-B0-08-29:0c:01',
                one_mac_per_ip = True,
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
                max_count_per_agent = 56
            )
        else:
            return EthRange(
                mac_auto = True,
        )
        """

    def testEthRange(self):
        """Test EthRange"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
