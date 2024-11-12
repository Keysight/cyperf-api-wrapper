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

from cyperf.models.compute_node import ComputeNode

class TestComputeNode(unittest.TestCase):
    """ComputeNode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ComputeNode:
        """Test ComputeNode
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ComputeNode`
        """
        model = ComputeNode()
        if include_optional:
            return ComputeNode(
                aggregated_mode = True,
                app_mode = cyperf.models.app_mode.AppMode(
                    app_id = '', 
                    ui_app_id = '', ),
                health_details = [
                    cyperf.models.health_issue.HealthIssue(
                        message = '', 
                        type = '', )
                    ],
                healthy = True,
                id = '',
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
                name = '',
                ports = [
                    cyperf.models.port.Port(
                        disabled = True, 
                        id = '', 
                        link = '', 
                        name = '', 
                        reserved_by = '', 
                        speed = '', 
                        status = '', 
                        traffic_status = '', )
                    ],
                serial = '',
                slot_number = 56,
                status = '',
                type = ''
            )
        else:
            return ComputeNode(
        )
        """

    def testComputeNode(self):
        """Test ComputeNode"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
