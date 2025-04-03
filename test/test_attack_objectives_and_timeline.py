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

from cyperf.models.attack_objectives_and_timeline import AttackObjectivesAndTimeline

class TestAttackObjectivesAndTimeline(unittest.TestCase):
    """AttackObjectivesAndTimeline unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AttackObjectivesAndTimeline:
        """Test AttackObjectivesAndTimeline
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AttackObjectivesAndTimeline`
        """
        model = AttackObjectivesAndTimeline()
        if include_optional:
            return AttackObjectivesAndTimeline(
                timeline_segments = [
                    null
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
            return AttackObjectivesAndTimeline(
        )
        """

    def testAttackObjectivesAndTimeline(self):
        """Test AttackObjectivesAndTimeline"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
