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

from cyperf.models.diagnostic_component_context import DiagnosticComponentContext

class TestDiagnosticComponentContext(unittest.TestCase):
    """DiagnosticComponentContext unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DiagnosticComponentContext:
        """Test DiagnosticComponentContext
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DiagnosticComponentContext`
        """
        model = DiagnosticComponentContext()
        if include_optional:
            return DiagnosticComponentContext(
                component_list = [
                    cyperf.models.diagnostic_component.DiagnosticComponent(
                        component_name = '', 
                        options = [
                            cyperf.models.diagnostic_options.DiagnosticOptions(
                                name = '', 
                                value = '', )
                            ], 
                        sub_components = [
                            cyperf.models.diagnostic_component.DiagnosticComponent(
                                component_name = '', )
                            ], )
                    ],
                context = [
                    cyperf.models.diagnostic_options.DiagnosticOptions(
                        name = '', 
                        value = '', )
                    ]
            )
        else:
            return DiagnosticComponentContext(
                component_list = [
                    cyperf.models.diagnostic_component.DiagnosticComponent(
                        component_name = '', 
                        options = [
                            cyperf.models.diagnostic_options.DiagnosticOptions(
                                name = '', 
                                value = '', )
                            ], 
                        sub_components = [
                            cyperf.models.diagnostic_component.DiagnosticComponent(
                                component_name = '', )
                            ], )
                    ],
        )
        """

    def testDiagnosticComponentContext(self):
        """Test DiagnosticComponentContext"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
