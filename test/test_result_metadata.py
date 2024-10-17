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

from cyperf.models.result_metadata import ResultMetadata

class TestResultMetadata(unittest.TestCase):
    """ResultMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResultMetadata:
        """Test ResultMetadata
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResultMetadata`
        """
        model = ResultMetadata()
        if include_optional:
            return ResultMetadata(
                active_session = '',
                config_url = '',
                csv_url = '',
                display_name = '',
                download_all = None,
                download_diagnostic = None,
                end_time = 56,
                files = [
                    cyperf.models.result_file_metadata.ResultFileMetadata(
                        file_id = '', 
                        file_name = '', 
                        id = '', 
                        last_modified = 56, 
                        result_id = '', 
                        type = '', )
                    ],
                id = '',
                last_modified = 56,
                links = [
                    cyperf.models.api_link.APILink(
                        content_type = '', 
                        href = '', 
                        method = '', 
                        name = '', 
                        references_count = 56, 
                        rel = '', 
                        type = '', )
                    ],
                marked_as_deleted = cyperf.models.marked_as_deleted.MarkedAsDeleted(
                    delete_progress = 56, 
                    value = True, ),
                owner = '',
                owner_id = '',
                pdf_url = '',
                pinned = True,
                reporting_links = [
                    cyperf.models.api_link.APILink(
                        content_type = '', 
                        href = '', 
                        method = '', 
                        name = '', 
                        references_count = 56, 
                        rel = '', 
                        type = '', )
                    ],
                result_url = '',
                start_time = 56,
                tags = {
                    'key' : ''
                    },
                test_name = '',
                type = '',
                user_tags = [
                    ''
                    ]
            )
        else:
            return ResultMetadata(
        )
        """

    def testResultMetadata(self):
        """Test ResultMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
