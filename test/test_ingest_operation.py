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

from cyperf.models.ingest_operation import IngestOperation

class TestIngestOperation(unittest.TestCase):
    """IngestOperation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IngestOperation:
        """Test IngestOperation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IngestOperation`
        """
        model = IngestOperation()
        if include_optional:
            return IngestOperation(
                plugin_stats = cyperf.models.plugin_stats.PluginStats(
                    plugin = '', 
                    stats = [
                        {
                            'key' : null
                            }
                        ], 
                    version = '', )
            )
        else:
            return IngestOperation(
        )
        """

    def testIngestOperation(self):
        """Test IngestOperation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
