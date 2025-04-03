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

from cyperf.models.get_sessions200_response import GetSessions200Response

class TestGetSessions200Response(unittest.TestCase):
    """GetSessions200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetSessions200Response:
        """Test GetSessions200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetSessions200Response`
        """
        model = GetSessions200Response()
        if include_optional:
            return GetSessions200Response(
                data = [
                    cyperf.models.session.Session(
                        application = '', 
                        config = cyperf.models.appsec_config.AppsecConfig(
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
                                validate_config = [
                                    'YQ=='
                                    ], ), 
                            session_id = '', 
                            template_id = '', 
                            config_type_name = '', 
                            data_model_version = '', 
                            id = '', 
                            links = , 
                            name = '', ), 
                        config_name = '', 
                        config_url = '', 
                        created = 56, 
                        data_model_url = '', 
                        id = '', 
                        index = 56, 
                        last_visited = 56, 
                        links = , 
                        meta = [
                            cyperf.models.pair.Pair(
                                id = 56, 
                                key = '', 
                                value = '', )
                            ], 
                        name = '', 
                        owner = '', 
                        owner_id = '', 
                        pinned = True, 
                        state = '', 
                        test = cyperf.models.test_info.TestInfo(
                            dashboards = [
                                cyperf.models.dashboard.Dashboard(
                                    id = '', 
                                    name = '', )
                                ], 
                            default_dashboard_index = 56, 
                            default_polling_interval = 56, 
                            status = '', 
                            test_details = '', 
                            test_duration = 56, 
                            test_elapsed = 56, 
                            test_id = '', 
                            test_initialized = 56, 
                            test_started = 56, 
                            test_stopped = 56, ), )
                    ],
                total_count = 56
            )
        else:
            return GetSessions200Response(
        )
        """

    def testGetSessions200Response(self):
        """Test GetSessions200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
