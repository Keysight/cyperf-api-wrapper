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

from cyperf.api.authorization_api import AuthorizationApi


class TestAuthorizationApi(unittest.TestCase):
    """AuthorizationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AuthorizationApi()

    def tearDown(self) -> None:
        pass

    def test_authenticate(self) -> None:
        """Test case for authenticate

        """
        pass


if __name__ == '__main__':
    unittest.main()
