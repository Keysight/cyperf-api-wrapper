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

from cyperf.models.advanced_settings import AdvancedSettings

class TestAdvancedSettings(unittest.TestCase):
    """AdvancedSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvancedSettings:
        """Test AdvancedSettings
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvancedSettings`
        """
        model = AdvancedSettings()
        if include_optional:
            return AdvancedSettings(
                agent_optimization_mode = 'BALANCED_MODE',
                agent_streaming_purpose_cpu_percent = 56,
                automatic_cpu_percent = True,
                connection_graceful_stop_timeout = 56,
                warm_up_period = 56
            )
        else:
            return AdvancedSettings(
                warm_up_period = 56,
        )
        """

    def testAdvancedSettings(self):
        """Test AdvancedSettings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
