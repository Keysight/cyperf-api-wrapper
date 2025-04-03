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

from cyperf.models.timeline_segment import TimelineSegment

class TestTimelineSegment(unittest.TestCase):
    """TimelineSegment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimelineSegment:
        """Test TimelineSegment
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimelineSegment`
        """
        model = TimelineSegment()
        if include_optional:
            return TimelineSegment(
                duration = 56,
                segment_type = 'SteadySegment',
                warm_up_period = 56,
                id = '',
                objective_unit = '',
                objective_value = 1.337,
                primary_objective_unit = '',
                primary_objective_value = 1.337,
                secondary_objective_values = [
                    cyperf.models.objective_value_entry.ObjectiveValueEntry(
                        unit = '', 
                        value = 1.337, 
                        id = '', )
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
            return TimelineSegment(
                duration = 56,
                segment_type = 'SteadySegment',
                id = '',
                primary_objective_unit = '',
                primary_objective_value = 1.337,
        )
        """

    def testTimelineSegment(self):
        """Test TimelineSegment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
