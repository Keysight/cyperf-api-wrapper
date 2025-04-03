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

from cyperf.models.tunnel_settings import TunnelSettings

class TestTunnelSettings(unittest.TestCase):
    """TunnelSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TunnelSettings:
        """Test TunnelSettings
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TunnelSettings`
        """
        model = TunnelSettings()
        if include_optional:
            return TunnelSettings(
                var_auth_settings = cyperf.models.auth_settings.AuthSettings(
                    auth_method = null, 
                    auth_param = null, 
                    certificate_file = null, 
                    key_file = null, 
                    key_file_password = '', 
                    passwords = [
                        ''
                        ], 
                    passwords_param = null, 
                    usernames = [
                        ''
                        ], 
                    usernames_param = null, 
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
                outer_tcp_profile = cyperf.models.tcp_profile.TcpProfile(
                    close_with_reset = True, 
                    defer_accept = True, 
                    ecn_enabled = True, 
                    max_rto = 56, 
                    max_src_port = 56, 
                    min_rto = 56, 
                    min_src_port = 56, 
                    ping_pong = True, 
                    pmtu_disc_disabled = True, 
                    recycle_tw_enabled = True, 
                    reordering = True, 
                    reuse_tw_enabled = True, 
                    rx_buffer = 56, 
                    sack_enabled = True, 
                    sock_group = '', 
                    timestamp_hdr_enabled = True, 
                    tx_buffer = 56, 
                    user_mss = 56, 
                    wscale_enabled = True, ),
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
            return TunnelSettings(
        )
        """

    def testTunnelSettings(self):
        """Test TunnelSettings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
