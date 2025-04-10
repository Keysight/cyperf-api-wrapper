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

from cyperf.models.broker import Broker

class TestBroker(unittest.TestCase):
    """Broker unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Broker:
        """Test Broker
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Broker`
        """
        model = Broker()
        if include_optional:
            return Broker(
                connection_status = '',
                failure_reason = '',
                fingerprint = '',
                host = '',
                host_name = '',
                id = '',
                interactive_fingerprint_verification = True,
                password = '',
                pretty_conn_status = '',
                trust_new = True,
                user = ''
            )
        else:
            return Broker(
        )
        """

    def testBroker(self):
        """Test Broker"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
