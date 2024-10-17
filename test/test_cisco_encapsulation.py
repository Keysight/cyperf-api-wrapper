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

from cyperf.models.cisco_encapsulation import CiscoEncapsulation

class TestCiscoEncapsulation(unittest.TestCase):
    """CiscoEncapsulation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CiscoEncapsulation:
        """Test CiscoEncapsulation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CiscoEncapsulation`
        """
        model = CiscoEncapsulation()
        if include_optional:
            return CiscoEncapsulation(
                dtls_enabled = True,
                dtls_settings = cyperf.models.dtls_settings.DTLSSettings(
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
                    tls_client_profile = null, 
                    udp_profile = null, ),
                encapsulation_mode = 'DTLS',
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
                udp_port = 56
            )
        else:
            return CiscoEncapsulation(
                dtls_enabled = True,
                encapsulation_mode = 'DTLS',
                udp_port = 56,
        )
        """

    def testCiscoEncapsulation(self):
        """Test CiscoEncapsulation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
