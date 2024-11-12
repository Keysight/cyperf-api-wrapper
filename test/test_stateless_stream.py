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

from cyperf.models.stateless_stream import StatelessStream

class TestStatelessStream(unittest.TestCase):
    """StatelessStream unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StatelessStream:
        """Test StatelessStream
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StatelessStream`
        """
        model = StatelessStream()
        if include_optional:
            return StatelessStream(
                client_stream_profile = cyperf.models.stream_profile.StreamProfile(
                    packet_rate = 56, 
                    payload_size = 56, 
                    payload_type = null, 
                    total_estimated_throughput = '', 
                    total_estimated_throughput_per_simulated_user = '', 
                    unique_pool_size = 56, ),
                direction = 'ClientToServer',
                is_flood_stream = True,
                server_stream_profile = cyperf.models.stream_profile.StreamProfile(
                    packet_rate = 56, 
                    payload_size = 56, 
                    payload_type = null, 
                    total_estimated_throughput = '', 
                    total_estimated_throughput_per_simulated_user = '', 
                    unique_pool_size = 56, ),
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
            return StatelessStream(
        )
        """

    def testStatelessStream(self):
        """Test StatelessStream"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
