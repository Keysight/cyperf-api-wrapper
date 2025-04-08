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

from cyperf.models.get_stats_plugins200_response_one_of import GetStatsPlugins200ResponseOneOf

class TestGetStatsPlugins200ResponseOneOf(unittest.TestCase):
    """GetStatsPlugins200ResponseOneOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetStatsPlugins200ResponseOneOf:
        """Test GetStatsPlugins200ResponseOneOf
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetStatsPlugins200ResponseOneOf`
        """
        model = GetStatsPlugins200ResponseOneOf()
        if include_optional:
            return GetStatsPlugins200ResponseOneOf(
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
            return GetStatsPlugins200ResponseOneOf(
        )
        """

    def testGetStatsPlugins200ResponseOneOf(self):
        """Test GetStatsPlugins200ResponseOneOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
