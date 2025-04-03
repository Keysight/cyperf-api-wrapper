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

from cyperf.models.application_type import ApplicationType

class TestApplicationType(unittest.TestCase):
    """ApplicationType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApplicationType:
        """Test ApplicationType
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApplicationType`
        """
        model = ApplicationType()
        if include_optional:
            return ApplicationType(
                commands = [
                    cyperf.models.command.Command(
                        action_id = '', 
                        description = '', 
                        exchanges = [
                            cyperf.models.exchange.Exchange(
                                client_endpoint = '', 
                                name = '', 
                                server_endpoint = '', 
                                id = '', )
                            ], 
                        is_strike = True, 
                        metadata = cyperf.models.metadata.Metadata(
                            cve_count = 56, 
                            direction = '', 
                            keywords = [
                                null
                                ], 
                            legacy_names = [
                                ''
                                ], 
                            references = [
                                cyperf.models.reference.Reference(
                                    type = '', 
                                    value = '', )
                                ], 
                            severity = '', 
                            strikes_count = 56, ), 
                        name = '', 
                        parameters = [
                            cyperf.models.parameter.Parameter(
                                default_array_elements = [
                                    {
                                        'key' : ''
                                        }
                                    ], 
                                default_source = '', 
                                default_value = '', 
                                element_type = '', 
                                sources = [
                                    ''
                                    ], 
                                type = '', 
                                field = '', 
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
                                operator = '', 
                                query_param = '', )
                            ], 
                        links = [
                            cyperf.models.api_link.APILink(
                                content_type = '', 
                                href = '', 
                                method = '', 
                                name = '', 
                                references_count = 56, 
                                rel = '', 
                                type = '', )
                            ], )
                    ],
                connections = [
                    cyperf.models.connection.Connection(
                        client_endpoint = '', 
                        client_port = 56, 
                        closing_end = '', 
                        disable_encryption = True, 
                        hostname = '', 
                        hostname_param = null, 
                        http_forward_proxy_mode = 'INHERIT_DUT', 
                        is_deprecated = True, 
                        max_transactions = 56, 
                        name = '', 
                        port_settings = null, 
                        readonly = True, 
                        readonly_hostname = True, 
                        readonly_max_trans = True, 
                        readonly_type = True, 
                        server_endpoint = '', 
                        server_port = 56, 
                        type = 'http', 
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
                            ], )
                    ],
                custom_stats = [
                    cyperf.models.custom_stat.CustomStat(
                        function = '', 
                        path = '', )
                    ],
                data_types = [
                    cyperf.models.data_type.DataType(
                        values = [
                            cyperf.models.data_type_values_inner.DataType_Values_inner(
                                id = '', 
                                value_type = '', )
                            ], 
                        id = '', )
                    ],
                definition = cyperf.models.definition.Definition(
                    xml = 'YQ==', ),
                description = '',
                endpoints = [
                    cyperf.models.endpoint.Endpoint(
                        name = '', 
                        network_mapping = null, 
                        type = 'Client', 
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
                            ], )
                    ],
                file_name = '',
                has_banner_command = True,
                md5_content = '',
                md5_metadata = '',
                metadata = cyperf.models.metadata.Metadata(
                    cve_count = 56, 
                    direction = '', 
                    keywords = [
                        null
                        ], 
                    legacy_names = [
                        ''
                        ], 
                    references = [
                        cyperf.models.reference.Reference(
                            type = '', 
                            value = '', )
                        ], 
                    severity = '', 
                    strikes_count = 56, ),
                name = '',
                parameters = [
                    cyperf.models.parameter.Parameter(
                        default_array_elements = [
                            {
                                'key' : ''
                                }
                            ], 
                        default_source = '', 
                        default_value = '', 
                        element_type = '', 
                        metadata = cyperf.models.parameter_metadata.ParameterMetadata(
                            category = '', 
                            category_index = 56, 
                            default = '', 
                            description = '', 
                            display_name = '', 
                            enum = cyperf.models.enum.Enum(
                                choices = [
                                    cyperf.models.choice.Choice(
                                        description = '', 
                                        hidden = True, 
                                        name = '', 
                                        value = '', )
                                    ], 
                                default = '', ), 
                            flow_identifier = True, 
                            input = '', 
                            legacy_names = [
                                ''
                                ], 
                            mandatory = True, 
                            payload = cyperf.models.payload_metadata.PayloadMetadata(
                                file_extension = '', 
                                file_name = '', 
                                file_type = '', 
                                file_url = '', ), 
                            readonly = True, 
                            shared = True, 
                            type = '', 
                            type_info = cyperf.models.type_info_metadata.TypeInfoMetadata(
                                array_v2 = cyperf.models.type_array_v2_metadata.TypeArrayV2Metadata(
                                    elements = [
                                        cyperf.models.array_v2_element_metadata.ArrayV2ElementMetadata(
                                            id = '', 
                                            type = '', )
                                        ], ), 
                                int = cyperf.models.type_int_metadata.TypeIntMetadata(
                                    max_value = 56, 
                                    min_value = 56, ), 
                                media = cyperf.models.type_media_metadata.TypeMediaMetadata(
                                    track_id = '', 
                                    track_type = '', ), 
                                string = cyperf.models.type_string_metadata.TypeStringMetadata(
                                    charset = '', 
                                    max_length = 56, 
                                    min_length = 56, ), ), 
                            unique_value = True, 
                            links = [
                                cyperf.models.api_link.APILink(
                                    content_type = '', 
                                    href = '', 
                                    method = '', 
                                    name = '', 
                                    references_count = 56, 
                                    rel = '', 
                                    type = '', )
                                ], ), 
                        sources = [
                            ''
                            ], 
                        type = '', 
                        field = '', 
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
                        operator = '', 
                        query_param = '', )
                    ],
                strikes = [
                    cyperf.models.command.Command(
                        action_id = '', 
                        description = '', 
                        exchanges = [
                            cyperf.models.exchange.Exchange(
                                client_endpoint = '', 
                                name = '', 
                                server_endpoint = '', 
                                id = '', )
                            ], 
                        is_strike = True, 
                        metadata = cyperf.models.metadata.Metadata(
                            cve_count = 56, 
                            direction = '', 
                            keywords = [
                                null
                                ], 
                            legacy_names = [
                                ''
                                ], 
                            references = [
                                cyperf.models.reference.Reference(
                                    type = '', 
                                    value = '', )
                                ], 
                            severity = '', 
                            strikes_count = 56, ), 
                        name = '', 
                        parameters = [
                            cyperf.models.parameter.Parameter(
                                default_array_elements = [
                                    {
                                        'key' : ''
                                        }
                                    ], 
                                default_source = '', 
                                default_value = '', 
                                element_type = '', 
                                sources = [
                                    ''
                                    ], 
                                type = '', 
                                field = '', 
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
                                operator = '', 
                                query_param = '', )
                            ], 
                        links = [
                            cyperf.models.api_link.APILink(
                                content_type = '', 
                                href = '', 
                                method = '', 
                                name = '', 
                                references_count = 56, 
                                rel = '', 
                                type = '', )
                            ], )
                    ],
                supports_calibration = True,
                supports_client_http_profile = True,
                supports_http_profiles = True,
                supports_server_http_profile = True,
                supports_strikes = True,
                supports_tls = True,
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
                    ]
            )
        else:
            return ApplicationType(
        )
        """

    def testApplicationType(self):
        """Test ApplicationType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
