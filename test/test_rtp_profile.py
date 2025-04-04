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

from cyperf.models.rtp_profile import RTPProfile

class TestRTPProfile(unittest.TestCase):
    """RTPProfile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RTPProfile:
        """Test RTPProfile
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RTPProfile`
        """
        model = RTPProfile()
        if include_optional:
            return RTPProfile(
                encryption_mode = 'ZOOM',
                mos_mode = 'DISABLED',
                profile_id = ''
            )
        else:
            return RTPProfile(
                encryption_mode = 'ZOOM',
                mos_mode = 'DISABLED',
                profile_id = '',
        )
        """

    def testRTPProfile(self):
        """Test RTPProfile"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
