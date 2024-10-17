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

from cyperf.models.action import Action

class TestAction(unittest.TestCase):
    """Action unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Action:
        """Test Action
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Action`
        """
        model = Action()
        if include_optional:
            return Action(
                dst_host = '252.7.188.200',
                exchanges = [
                    cyperf.models.exchange.Exchange(
                        client_endpoint = '', 
                        id = '', 
                        name = '', 
                        server_endpoint = '', )
                    ],
                id = '',
                index = 56,
                is_banner = True,
                is_deprecated = True,
                is_hostname = 56,
                is_strike = True,
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
                name = '',
                params = [
                    cyperf.models.params.Params(
                        array_elements = [
                            {
                                'key' : ''
                                }
                            ], 
                        array_element_type = '', 
                        category = '', 
                        category_index = 56, 
                        deprecated_previous_source = '', 
                        description = '', 
                        dictionary_value = {
                            'key' : ''
                            }, 
                        enum = cyperf.models.params_enum.Params_Enum(
                            choices = [
                                cyperf.models.choice.Choice(
                                    description = '', 
                                    hidden = True, 
                                    name = '', 
                                    value = '', )
                                ], ), 
                        file_upload = [
                            'YQ=='
                            ], 
                        file_value = null, 
                        flow_identifier = True, 
                        id = '', 
                        is_deprecated = True, 
                        is_modified = True, 
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
                        media_files = [
                            cyperf.models.media_file.MediaFile(
                                file_value = null, 
                                media_tracks = [
                                    cyperf.models.media_track.MediaTrack(
                                        bitrate = 56, 
                                        bitrate_kbps = 56, 
                                        codec = '', 
                                        codec_description = '', 
                                        id = '', 
                                        track_id = '', 
                                        track_type = null, )
                                    ], )
                            ], 
                        metadata = cyperf.models.param_metadata.ParamMetadata(
                            type_info = cyperf.models.param_metadata_type_info.ParamMetadata_TypeInfo(
                                array_v2 = cyperf.models.param_metadata_type_info_array_v2.ParamMetadata_TypeInfo_arrayV2(
                                    elements = [
                                        cyperf.models.param_metadata_type_info_array_v2_elements_inner.ParamMetadata_TypeInfo_arrayV2_elements_inner(
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
                                    min_length = 56, ), ), ), 
                        name = '', 
                        param_id = '', 
                        readonly = True, 
                        source = '', 
                        supported_sources = [
                            ''
                            ], 
                        supports_dynamic_payload = True, 
                        type = '', 
                        upload_url = '', 
                        value = '', )
                    ],
                port = 56,
                protocol_id = '',
                requires_uniqueness = True
            )
        else:
            return Action(
        )
        """

    def testAction(self):
        """Test Action"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
