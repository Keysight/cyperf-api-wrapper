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

from cyperf.models.remote_access import RemoteAccess

class TestRemoteAccess(unittest.TestCase):
    """RemoteAccess unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RemoteAccess:
        """Test RemoteAccess
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RemoteAccess`
        """
        model = RemoteAccess()
        if include_optional:
            return RemoteAccess(
                mode_cfg_increment = '::02:84:9:0cc0:F:CCf',
                mode_cfg_start = '::02:84:9:0cc0:F:CCf',
                mode_cfg_suffix = 56
            )
        else:
            return RemoteAccess(
                mode_cfg_increment = '::02:84:9:0cc0:F:CCf',
                mode_cfg_suffix = 56,
        )
        """

    def testRemoteAccess(self):
        """Test RemoteAccess"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
