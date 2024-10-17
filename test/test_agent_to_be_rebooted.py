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

from cyperf.models.agent_to_be_rebooted import AgentToBeRebooted

class TestAgentToBeRebooted(unittest.TestCase):
    """AgentToBeRebooted unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AgentToBeRebooted:
        """Test AgentToBeRebooted
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AgentToBeRebooted`
        """
        model = AgentToBeRebooted()
        if include_optional:
            return AgentToBeRebooted(
                agent_id = ''
            )
        else:
            return AgentToBeRebooted(
        )
        """

    def testAgentToBeRebooted(self):
        """Test AgentToBeRebooted"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
