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

from cyperf.models.local_subnet_config import LocalSubnetConfig

class TestLocalSubnetConfig(unittest.TestCase):
    """LocalSubnetConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LocalSubnetConfig:
        """Test LocalSubnetConfig
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LocalSubnetConfig`
        """
        model = LocalSubnetConfig()
        if include_optional:
            return LocalSubnetConfig(
                host_count_per_tunnel = 56,
                hosts_increment = '::02:84:9:0cc0:F:CCf',
                hosts_prefix = 56,
                increment = '::02:84:9:0cc0:F:CCf',
                prefix = 56,
                start = '::02:84:9:0cc0:F:CCf',
                total_host_count = '',
                network_tags = [
                    ''
                    ]
            )
        else:
            return LocalSubnetConfig(
                host_count_per_tunnel = 56,
                hosts_increment = '::02:84:9:0cc0:F:CCf',
                hosts_prefix = 56,
                increment = '::02:84:9:0cc0:F:CCf',
                prefix = 56,
                start = '::02:84:9:0cc0:F:CCf',
                total_host_count = '',
                network_tags = [
                    ''
                    ],
        )
        """

    def testLocalSubnetConfig(self):
        """Test LocalSubnetConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
