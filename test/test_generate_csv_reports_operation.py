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

from cyperf.models.generate_csv_reports_operation import GenerateCSVReportsOperation

class TestGenerateCSVReportsOperation(unittest.TestCase):
    """GenerateCSVReportsOperation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GenerateCSVReportsOperation:
        """Test GenerateCSVReportsOperation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GenerateCSVReportsOperation`
        """
        model = GenerateCSVReportsOperation()
        if include_optional:
            return GenerateCSVReportsOperation(
                force_generate = True,
                var_from = '',
                interval = '',
                stats = [
                    cyperf.models.filtered_stat.FilteredStat(
                        filters = [
                            cyperf.models.filter.Filter(
                                name = '', 
                                value = '', )
                            ], 
                        name = '', )
                    ],
                to = '',
                use_relative_time = True
            )
        else:
            return GenerateCSVReportsOperation(
        )
        """

    def testGenerateCSVReportsOperation(self):
        """Test GenerateCSVReportsOperation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
