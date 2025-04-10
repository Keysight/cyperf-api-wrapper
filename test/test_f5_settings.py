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

from cyperf.models.f5_settings import F5Settings

class TestF5Settings(unittest.TestCase):
    """F5Settings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> F5Settings:
        """Test F5Settings
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `F5Settings`
        """
        model = F5Settings()
        if include_optional:
            return F5Settings(
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
                    ],
                f5_encapsulation = cyperf.models.f5_encapsulation.F5Encapsulation(
                    encapsulation_mode = 'PPP_OVER_DTLS', 
                    ppp_over_dtls_enabled = True, 
                    ppp_over_dtls_settings = null, 
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
                        ], ),
                outer_tls_client_profile = cyperf.models.tls_profile.TLSProfile(
                    certificate_file = null, 
                    cipher = null, 
                    cipher12 = null, 
                    cipher13 = null, 
                    ciphers12 = [
                        'ECDHE-RSA-AES256-GCM-SHA384'
                        ], 
                    ciphers13 = [
                        'AES-256-GCM-SHA384'
                        ], 
                    dh_file = null, 
                    get_tls_conflicts = [
                        'YQ=='
                        ], 
                    immediate_close = True, 
                    key_file = null, 
                    key_file_password = '', 
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
                    middle_box_enabled = True, 
                    profile_id = '', 
                    resolve_tls_conflicts = [
                        cyperf.models.conflict.Conflict(
                            name = '', 
                            path_to_target = '', 
                            path_vars = {
                                'key' : ''
                                }, )
                        ], 
                    send_close_notify = True, 
                    session_reuse_count = 56, 
                    session_reuse_method = null, 
                    session_reuse_method12 = null, 
                    session_reuse_method13 = null, 
                    sni_cert_configs = [
                        cyperf.models.cert_config.CertConfig(
                            certificate_file = null, 
                            dh_file = null, 
                            get_sni_conflicts = [
                                'YQ=='
                                ], 
                            id = '', 
                            is_playlist = True, 
                            key_file = null, 
                            key_file_password = '', 
                            playlist_column_name = '', 
                            playlist_filename = '', 
                            resolve_sni_conflicts = [
                                cyperf.models.conflict.Conflict(
                                    name = '', 
                                    path_to_target = '', 
                                    path_vars = {
                                        'key' : ''
                                        }, )
                                ], 
                            sni_hostname = '', )
                        ], 
                    sni_enabled = True, 
                    supported_groups13 = [
                        'P-256'
                        ], 
                    tls12_enabled = True, 
                    tls13_enabled = True, 
                    use_tls_profile = True, 
                    version = 'NONE', ),
                vpn_gateway = '::'
            )
        else:
            return F5Settings(
        )
        """

    def testF5Settings(self):
        """Test F5Settings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
