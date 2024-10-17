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

from cyperf.models.static_arp_entry import StaticARPEntry

class TestStaticARPEntry(unittest.TestCase):
    """StaticARPEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StaticARPEntry:
        """Test StaticARPEntry
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StaticARPEntry`
        """
        model = StaticARPEntry()
        if include_optional:
            return StaticARPEntry(
                count = 56,
                id = '',
                remote_ip = '::02:84:9:0cc0:F:CCf',
                remote_ip_incr = '::02:84:9:0cc0:F:CCf',
                remote_mac = '2E-B0-08-29:0c:01',
                remote_mac_incr = '2E-B0-08-29:0c:01',
                static_arp_entry_name = 'YBuLd'
            )
        else:
            return StaticARPEntry(
                id = '',
                static_arp_entry_name = 'YBuLd',
        )
        """

    def testStaticARPEntry(self):
        """Test StaticARPEntry"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
