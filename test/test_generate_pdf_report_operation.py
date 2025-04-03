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

from cyperf.models.generate_pdf_report_operation import GeneratePDFReportOperation

class TestGeneratePDFReportOperation(unittest.TestCase):
    """GeneratePDFReportOperation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GeneratePDFReportOperation:
        """Test GeneratePDFReportOperation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GeneratePDFReportOperation`
        """
        model = GeneratePDFReportOperation()
        if include_optional:
            return GeneratePDFReportOperation(
                force_generate = True,
                timezone_offset = 56
            )
        else:
            return GeneratePDFReportOperation(
        )
        """

    def testGeneratePDFReportOperation(self):
        """Test GeneratePDFReportOperation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
