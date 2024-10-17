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

from cyperf.models.get_plugins200_response_one_of import GetPlugins200ResponseOneOf

class TestGetPlugins200ResponseOneOf(unittest.TestCase):
    """GetPlugins200ResponseOneOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetPlugins200ResponseOneOf:
        """Test GetPlugins200ResponseOneOf
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetPlugins200ResponseOneOf`
        """
        model = GetPlugins200ResponseOneOf()
        if include_optional:
            return GetPlugins200ResponseOneOf(
                data = [
                    cyperf.models.plugin.Plugin(
                        id = '', 
                        keys = [
                            ''
                            ], 
                        name = '', 
                        version = '', )
                    ],
                total_count = 56
            )
        else:
            return GetPlugins200ResponseOneOf(
        )
        """

    def testGetPlugins200ResponseOneOf(self):
        """Test GetPlugins200ResponseOneOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
