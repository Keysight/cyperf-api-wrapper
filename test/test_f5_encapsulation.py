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

from cyperf.models.f5_encapsulation import F5Encapsulation

class TestF5Encapsulation(unittest.TestCase):
    """F5Encapsulation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> F5Encapsulation:
        """Test F5Encapsulation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `F5Encapsulation`
        """
        model = F5Encapsulation()
        if include_optional:
            return F5Encapsulation(
                encapsulation_mode = 'PPP_OVER_DTLS',
                ppp_over_dtls_enabled = True,
                ppp_over_dtls_settings = cyperf.models.dtls_settings.DTLSSettings(
                    tls_client_profile = null, 
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
            return F5Encapsulation(
                encapsulation_mode = 'PPP_OVER_DTLS',
                ppp_over_dtls_enabled = True,
                udp_port = 56,
        )
        """

    def testF5Encapsulation(self):
        """Test F5Encapsulation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
