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

from cyperf.models.config import Config

class TestConfig(unittest.TestCase):
    """Config unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Config:
        """Test Config
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Config`
        """
        model = Config()
        if include_optional:
            return Config(
                attack_profiles = [
                    null
                    ],
                config_validation = cyperf.models.config_validation.ConfigValidation(
                    is_validated = True, 
                    validation_messages = [
                        cyperf.models.validation_message.ValidationMessage(
                            message = '', 
                            severity = 'WARNING', )
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
                        ], ),
                custom_dashboards = cyperf.models.custom_dashboards.CustomDashboards(
                    active = True, 
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
                    ]
            )
        else:
            return Config(
        )
        """

    def testConfig(self):
        """Test Config"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
