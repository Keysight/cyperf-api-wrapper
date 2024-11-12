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

from cyperf.models.pangp_encapsulation import PANGPEncapsulation

class TestPANGPEncapsulation(unittest.TestCase):
    """PANGPEncapsulation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PANGPEncapsulation:
        """Test PANGPEncapsulation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PANGPEncapsulation`
        """
        model = PANGPEncapsulation()
        if include_optional:
            return PANGPEncapsulation(
                esp_over_udp_enabled = True,
                esp_over_udp_settings = cyperf.models.esp_over_udp_settings.ESPOverUDPSettings(
                    udp_profile = null, 
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
                encapsulation_mode = 'ESP_OVER_UDP',
                udp_port = 56,
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
            return PANGPEncapsulation(
                esp_over_udp_enabled = True,
                encapsulation_mode = 'ESP_OVER_UDP',
                udp_port = 56,
        )
        """

    def testPANGPEncapsulation(self):
        """Test PANGPEncapsulation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
