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

from cyperf.models.param_metadata_type_info_string import ParamMetadataTypeInfoString

class TestParamMetadataTypeInfoString(unittest.TestCase):
    """ParamMetadataTypeInfoString unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ParamMetadataTypeInfoString:
        """Test ParamMetadataTypeInfoString
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ParamMetadataTypeInfoString`
        """
        model = ParamMetadataTypeInfoString()
        if include_optional:
            return ParamMetadataTypeInfoString(
                charset = '',
                max_length = 56,
                min_length = 56
            )
        else:
            return ParamMetadataTypeInfoString(
        )
        """

    def testParamMetadataTypeInfoString(self):
        """Test ParamMetadataTypeInfoString"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
