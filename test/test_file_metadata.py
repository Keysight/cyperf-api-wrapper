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

from cyperf.models.file_metadata import FileMetadata

class TestFileMetadata(unittest.TestCase):
    """FileMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FileMetadata:
        """Test FileMetadata
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FileMetadata`
        """
        model = FileMetadata()
        if include_optional:
            return FileMetadata(
                default = True,
                user_visible = True
            )
        else:
            return FileMetadata(
        )
        """

    def testFileMetadata(self):
        """Test FileMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
