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

from cyperf.models.get_result_stats200_response import GetResultStats200Response

class TestGetResultStats200Response(unittest.TestCase):
    """GetResultStats200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetResultStats200Response:
        """Test GetResultStats200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetResultStats200Response`
        """
        model = GetResultStats200Response()
        if include_optional:
            return GetResultStats200Response(
                data = [
                    cyperf.models.stats_result.StatsResult(
                        available_filters = [
                            cyperf.models.parameter.Parameter(
                                matches = [
                                    cyperf.models.parameter_match.ParameterMatch(
                                        match_location = [
                                            ''
                                            ], 
                                        match_type = '', 
                                        regex_match = cyperf.models.regex_match.RegexMatch(
                                            patterns = [
                                                ''
                                                ], ), )
                                    ], 
                                name = '', 
                                field = '', 
                                operator = '', 
                                query_param = '', )
                            ], 
                        columns = [
                            ''
                            ], 
                        name = '', 
                        snapshots = [
                            cyperf.models.snapshot.Snapshot(
                                timestamp = 56, 
                                values = [
                                    [
                                        null
                                        ]
                                    ], )
                            ], )
                    ],
                total_count = 56
            )
        else:
            return GetResultStats200Response(
        )
        """

    def testGetResultStats200Response(self):
        """Test GetResultStats200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
