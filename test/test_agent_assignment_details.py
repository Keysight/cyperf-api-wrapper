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

from cyperf.models.agent_assignment_details import AgentAssignmentDetails

class TestAgentAssignmentDetails(unittest.TestCase):
    """AgentAssignmentDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AgentAssignmentDetails:
        """Test AgentAssignmentDetails
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AgentAssignmentDetails`
        """
        model = AgentAssignmentDetails()
        if include_optional:
            return AgentAssignmentDetails(
                agent_id = '',
                capture_settings = cyperf.models.capture_settings.CaptureSettings(
                    capture_enabled = True, 
                    capture_latest_packets = True, 
                    log_level = null, 
                    max_capture_size = 56, ),
                id = '',
                interfaces = [
                    ''
                    ],
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
            return AgentAssignmentDetails(
                agent_id = '',
                id = '',
        )
        """

    def testAgentAssignmentDetails(self):
        """Test AgentAssignmentDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
