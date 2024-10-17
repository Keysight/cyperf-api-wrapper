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

from cyperf.models.pep_dut import PepDUT

class TestPepDUT(unittest.TestCase):
    """PepDUT unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PepDUT:
        """Test PepDUT
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PepDUT`
        """
        model = PepDUT()
        if include_optional:
            return PepDUT(
                auth_method = cyperf.models.params.Params(
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
                            id = '', 
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
                    value = '', ),
                auth_profile_params = [
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
                                id = '', 
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
                auth_profile_type = '',
                hostname_suffix = '252.7.188.200',
                idp_type = cyperf.models.params.Params(
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
                            id = '', 
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
                    value = '', ),
                is_explicit_proxy = True,
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
                pep_host = '252.7.188.200',
                pep_port = 56,
                simulated_id_p = cyperf.models.simulated_id_p.SimulatedIdP(
                    assertion_signature = True, 
                    audience_uri = '', 
                    cert_config = null, 
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
                    name_id_format = null, 
                    response_signature = True, 
                    signature_algorithm = null, 
                    single_sign_on_url = '', 
                    xml_metadata = [
                        'YQ=='
                        ], )
            )
        else:
            return PepDUT(
        )
        """

    def testPepDUT(self):
        """Test PepDUT"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
