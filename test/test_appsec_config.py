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

from cyperf.models.appsec_config import AppsecConfig

class TestAppsecConfig(unittest.TestCase):
    """AppsecConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppsecConfig:
        """Test AppsecConfig
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppsecConfig`
        """
        model = AppsecConfig()
        if include_optional:
            return AppsecConfig(
                config = cyperf.models.config.Config(
                    attack_profiles = [
                        null
                        ], 
                    config_validation = null, 
                    custom_dashboards = null, 
                    expected_disk_space = [
                        cyperf.models.expected_disk_space.ExpectedDiskSpace(
                            message = cyperf.models.expected_disk_space_message.ExpectedDiskSpace_message(
                                per_minute = '', 
                                per_second = '', 
                                total = '', ), 
                            pretty_size = cyperf.models.expected_disk_space_pretty_size.ExpectedDiskSpace_prettySize(
                                per_minute = '', 
                                per_second = '', 
                                total = '', ), 
                            size = cyperf.models.expected_disk_space_size.ExpectedDiskSpace_size(
                                per_minute = 56, 
                                per_second = 56, 
                                total = 56, ), )
                        ], 
                    network_profiles = [
                        cyperf.models.network_profile.NetworkProfile(
                            dut_network_segment = [
                                null
                                ], 
                            ip_network_segment = [
                                null
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
                                ], )
                        ], 
                    traffic_profiles = [
                        null
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
                        ], 
                    validate = [
                        'YQ=='
                        ], ),
                session_id = '',
                template_id = '',
                config_type_name = '',
                data_model_version = '',
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
                name = ''
            )
        else:
            return AppsecConfig(
                config_type_name = '',
        )
        """

    def testAppsecConfig(self):
        """Test AppsecConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
