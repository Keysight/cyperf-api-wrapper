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

from cyperf.models.udp_profile import UdpProfile

class TestUdpProfile(unittest.TestCase):
    """UdpProfile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UdpProfile:
        """Test UdpProfile
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UdpProfile`
        """
        model = UdpProfile()
        if include_optional:
            return UdpProfile(
                max_src_port = 56,
                min_src_port = 56,
                recv_buff_size_ini = 56,
                recv_buff_size_res = 56,
                rx_buffer = 56,
                sock_group = '',
                tx_buffer = 56
            )
        else:
            return UdpProfile(
        )
        """

    def testUdpProfile(self):
        """Test UdpProfile"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
