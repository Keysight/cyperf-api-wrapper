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

from cyperf.models.get_resources_certificates200_response import GetResourcesCertificates200Response

class TestGetResourcesCertificates200Response(unittest.TestCase):
    """GetResourcesCertificates200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetResourcesCertificates200Response:
        """Test GetResourcesCertificates200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetResourcesCertificates200Response`
        """
        model = GetResourcesCertificates200Response()
        if include_optional:
            return GetResourcesCertificates200Response(
                data = [
                    cyperf.models.generic_file.GenericFile(
                        content = 'YQ==', 
                        id = '', 
                        md5 = '', 
                        metadata = cyperf.models.file_metadata.FileMetadata(
                            default = True, 
                            user_visible = True, ), 
                        name = '', 
                        options = {
                            'key' : null
                            }, 
                        owner = '', 
                        owner_id = '', 
                        reference_links = {
                            'key' : 56
                            }, 
                        size = 56, 
                        type = '', )
                    ],
                total_count = 56
            )
        else:
            return GetResourcesCertificates200Response(
        )
        """

    def testGetResourcesCertificates200Response(self):
        """Test GetResourcesCertificates200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
