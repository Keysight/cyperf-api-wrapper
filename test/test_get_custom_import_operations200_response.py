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

from cyperf.models.get_custom_import_operations200_response import GetCustomImportOperations200Response

class TestGetCustomImportOperations200Response(unittest.TestCase):
    """GetCustomImportOperations200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetCustomImportOperations200Response:
        """Test GetCustomImportOperations200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCustomImportOperations200Response`
        """
        model = GetCustomImportOperations200Response()
        if include_optional:
            return GetCustomImportOperations200Response(
                data = [
                    cyperf.models.custom_import_handler.CustomImportHandler(
                        link = cyperf.models.api_link.APILink(
                            content_type = '', 
                            href = '', 
                            method = '', 
                            name = '', 
                            references_count = 56, 
                            rel = '', 
                            type = '', ), 
                        name = '', )
                    ],
                total_count = 56
            )
        else:
            return GetCustomImportOperations200Response(
        )
        """

    def testGetCustomImportOperations200Response(self):
        """Test GetCustomImportOperations200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
