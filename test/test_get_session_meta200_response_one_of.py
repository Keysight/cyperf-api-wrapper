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

from cyperf.models.get_session_meta200_response_one_of import GetSessionMeta200ResponseOneOf

class TestGetSessionMeta200ResponseOneOf(unittest.TestCase):
    """GetSessionMeta200ResponseOneOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetSessionMeta200ResponseOneOf:
        """Test GetSessionMeta200ResponseOneOf
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetSessionMeta200ResponseOneOf`
        """
        model = GetSessionMeta200ResponseOneOf()
        if include_optional:
            return GetSessionMeta200ResponseOneOf(
                data = [
                    cyperf.models.pair.Pair(
                        id = 56, 
                        key = '', 
                        value = '', )
                    ],
                total_count = 56
            )
        else:
            return GetSessionMeta200ResponseOneOf(
        )
        """

    def testGetSessionMeta200ResponseOneOf(self):
        """Test GetSessionMeta200ResponseOneOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
