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

from cyperf.models.get_apps200_response import GetApps200Response

class TestGetApps200Response(unittest.TestCase):
    """GetApps200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetApps200Response:
        """Test GetApps200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetApps200Response`
        """
        model = GetApps200Response()
        if include_optional:
            return GetApps200Response(
                data = [
                    cyperf.models.appsec_app.AppsecApp(
                        app = null, 
                        description = '', 
                        name = '', 
                        static = True, 
                        user_defined = True, 
                        app_metadata = cyperf.models.appsec_app_metadata.AppsecAppMetadata(
                            actions_metadata = [
                                cyperf.models.action_metadata.ActionMetadata(
                                    flow_index = {
                                        'key' : 56
                                        }, 
                                    flows = [
                                        cyperf.models.app_flow.AppFlow(
                                            dst_address = 'YQ==', 
                                            dst_port = 56, 
                                            exchanges = [
                                                cyperf.models.app_exchange.AppExchange(
                                                    c2s_payload = cyperf.models.generic_file.GenericFile(
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
                                                        type = '', ), 
                                                    id = '', 
                                                    payload = cyperf.models.exchange_payload.ExchangePayload(
                                                        c2s = 'YQ==', 
                                                        s2c = 'YQ==', ), 
                                                    s2c_payload = cyperf.models.generic_file.GenericFile(
                                                        content = 'YQ==', 
                                                        id = '', 
                                                        md5 = '', 
                                                        name = '', 
                                                        owner = '', 
                                                        owner_id = '', 
                                                        size = 56, 
                                                        type = '', ), )
                                                ], 
                                            id = '', 
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
                                            src_address = 'YQ==', 
                                            src_port = 56, 
                                            transport_type = '', )
                                        ], 
                                    index = 56, 
                                    name = '', )
                                ], ), 
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
                        owner = '', 
                        owner_id = '', )
                    ],
                total_count = 56
            )
        else:
            return GetApps200Response(
        )
        """

    def testGetApps200Response(self):
        """Test GetApps200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
