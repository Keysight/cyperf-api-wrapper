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

from cyperf.models.port_settings import PortSettings

class TestPortSettings(unittest.TestCase):
    """PortSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PortSettings:
        """Test PortSettings
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PortSettings`
        """
        model = PortSettings()
        if include_optional:
            return PortSettings(
                automatic = True,
                automatic_destination_port = True,
                automatic_forward_proxy_port = True,
                destination_port = 56,
                effective_ports = cyperf.models.effective_ports.EffectivePorts(
                    effective_destination_port = '', 
                    effective_forward_proxy_port = '', 
                    effective_server_port = '', ),
                forward_proxy_port = 56,
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
                readonly = True,
                server_listen_port = 56
            )
        else:
            return PortSettings(
                automatic = True,
                automatic_destination_port = True,
                automatic_forward_proxy_port = True,
                destination_port = 56,
                forward_proxy_port = 56,
                server_listen_port = 56,
        )
        """

    def testPortSettings(self):
        """Test PortSettings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
