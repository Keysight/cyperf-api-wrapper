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

from cyperf.models.param_metadata_type_info_array_v2_elements_inner import ParamMetadataTypeInfoArrayV2ElementsInner

class TestParamMetadataTypeInfoArrayV2ElementsInner(unittest.TestCase):
    """ParamMetadataTypeInfoArrayV2ElementsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ParamMetadataTypeInfoArrayV2ElementsInner:
        """Test ParamMetadataTypeInfoArrayV2ElementsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ParamMetadataTypeInfoArrayV2ElementsInner`
        """
        model = ParamMetadataTypeInfoArrayV2ElementsInner()
        if include_optional:
            return ParamMetadataTypeInfoArrayV2ElementsInner(
                id = '',
                type = ''
            )
        else:
            return ParamMetadataTypeInfoArrayV2ElementsInner(
        )
        """

    def testParamMetadataTypeInfoArrayV2ElementsInner(self):
        """Test ParamMetadataTypeInfoArrayV2ElementsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
