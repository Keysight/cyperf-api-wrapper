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

from cyperf.models.param_metadata import ParamMetadata

class TestParamMetadata(unittest.TestCase):
    """ParamMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ParamMetadata:
        """Test ParamMetadata
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ParamMetadata`
        """
        model = ParamMetadata()
        if include_optional:
            return ParamMetadata(
                type_info = cyperf.models.param_metadata_type_info.ParamMetadata_TypeInfo(
                    array_v2 = cyperf.models.param_metadata_type_info_array_v2.ParamMetadata_TypeInfo_arrayV2(
                        elements = [
                            cyperf.models.param_metadata_type_info_array_v2_elements_inner.ParamMetadata_TypeInfo_arrayV2_elements_inner(
                                id = '', 
                                type = '', )
                            ], ), 
                    int = cyperf.models.param_metadata_type_info_int.ParamMetadata_TypeInfo_int(
                        max_value = 56, 
                        min_value = 56, ), 
                    media = cyperf.models.param_metadata_type_info_media.ParamMetadata_TypeInfo_media(
                        track_id = '', 
                        track_type = '', ), 
                    string = cyperf.models.param_metadata_type_info_string.ParamMetadata_TypeInfo_string(
                        charset = '', 
                        max_length = 56, 
                        min_length = 56, ), )
            )
        else:
            return ParamMetadata(
        )
        """

    def testParamMetadata(self):
        """Test ParamMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
