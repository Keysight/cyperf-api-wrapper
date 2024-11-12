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

from cyperf.models.get_application_types200_response_one_of import GetApplicationTypes200ResponseOneOf

class TestGetApplicationTypes200ResponseOneOf(unittest.TestCase):
    """GetApplicationTypes200ResponseOneOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetApplicationTypes200ResponseOneOf:
        """Test GetApplicationTypes200ResponseOneOf
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetApplicationTypes200ResponseOneOf`
        """
        model = GetApplicationTypes200ResponseOneOf()
        if include_optional:
            return GetApplicationTypes200ResponseOneOf(
                data = [
                    cyperf.models.application_type.ApplicationType(
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
                                id = '', )
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
                                id = '', )
                            ], 
                        file_name = '', 
                        has_banner_command = True, 
                        md5_content = '', 
                        md5_metadata = '', 
                        metadata = cyperf.models.metadata.Metadata(
                            cve_count = 56, 
                            direction = '', 
                            severity = '', 
                            strikes_count = 56, ), 
                        name = '', 
                        parameters = [
                            cyperf.models.parameter.Parameter(
                                default_source = '', 
                                default_value = '', 
                                element_type = '', 
                                type = '', 
                                field = '', 
                                id = '', 
                                operator = '', 
                                query_param = '', )
                            ], 
                        strikes = [
                            cyperf.models.command.Command(
                                action_id = '', 
                                description = '', 
                                is_strike = True, 
                                name = '', )
                            ], 
                        supports_calibration = True, 
                        supports_client_http_profile = True, 
                        supports_http_profiles = True, 
                        supports_server_http_profile = True, 
                        supports_strikes = True, 
                        supports_tls = True, 
                        id = '', 
                        links = , )
                    ],
                total_count = 56
            )
        else:
            return GetApplicationTypes200ResponseOneOf(
        )
        """

    def testGetApplicationTypes200ResponseOneOf(self):
        """Test GetApplicationTypes200ResponseOneOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
