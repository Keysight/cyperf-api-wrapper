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

from cyperf.models.test_info import TestInfo

class TestTestInfo(unittest.TestCase):
    """TestInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TestInfo:
        """Test TestInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TestInfo`
        """
        model = TestInfo()
        if include_optional:
            return TestInfo(
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
                test_stopped = 56
            )
        else:
            return TestInfo(
        )
        """

    def testTestInfo(self):
        """Test TestInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
