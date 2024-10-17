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

from cyperf.models.selected_env import SelectedEnv

class TestSelectedEnv(unittest.TestCase):
    """SelectedEnv unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SelectedEnv:
        """Test SelectedEnv
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SelectedEnv`
        """
        model = SelectedEnv()
        if include_optional:
            return SelectedEnv(
                session_id = '',
                test_interface = [
                    cyperf.models.interface.Interface(
                        gateway = '', 
                        ip = [
                            cyperf.models.ip_mask.IpMask(
                                net_mask = 56, )
                            ], 
                        mac = '', 
                        mtu = 56, 
                        name = '', )
                    ],
                token = ''
            )
        else:
            return SelectedEnv(
        )
        """

    def testSelectedEnv(self):
        """Test SelectedEnv"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
