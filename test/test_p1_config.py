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

from cyperf.models.p1_config import P1Config

class TestP1Config(unittest.TestCase):
    """P1Config unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> P1Config:
        """Test P1Config
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `P1Config`
        """
        model = P1Config()
        if include_optional:
            return P1Config(
                dh_group = 'MODP 768',
                enc_algorithm = 'DES CBC',
                hash_algorithm = 'HMAC MD5',
                initial_contact = True,
                lifetime = 56,
                prf_algorithm = 'HMAC MD5'
            )
        else:
            return P1Config(
                dh_group = 'MODP 768',
                enc_algorithm = 'DES CBC',
                hash_algorithm = 'HMAC MD5',
                initial_contact = True,
                lifetime = 56,
                prf_algorithm = 'HMAC MD5',
        )
        """

    def testP1Config(self):
        """Test P1Config"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
