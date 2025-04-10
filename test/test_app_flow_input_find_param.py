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

from cyperf.models.app_flow_input_find_param import AppFlowInputFindParam

class TestAppFlowInputFindParam(unittest.TestCase):
    """AppFlowInputFindParam unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppFlowInputFindParam:
        """Test AppFlowInputFindParam
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppFlowInputFindParam`
        """
        model = AppFlowInputFindParam()
        if include_optional:
            return AppFlowInputFindParam(
                app_flow_desc = cyperf.models.app_flow_desc.AppFlowDesc(
                    dst_address = 'YQ==', 
                    dst_port = 56, 
                    src_address = 'YQ==', 
                    src_port = 56, ),
                app_flow_id = '',
                exchange_names = [
                    ''
                    ],
                exchanges = [
                    ''
                    ]
            )
        else:
            return AppFlowInputFindParam(
        )
        """

    def testAppFlowInputFindParam(self):
        """Test AppFlowInputFindParam"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
