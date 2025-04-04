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

from cyperf.models.reboot_ports_operation import RebootPortsOperation

class TestRebootPortsOperation(unittest.TestCase):
    """RebootPortsOperation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RebootPortsOperation:
        """Test RebootPortsOperation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RebootPortsOperation`
        """
        model = RebootPortsOperation()
        if include_optional:
            return RebootPortsOperation(
                controllers = [
                    cyperf.models.ports_by_controller.PortsByController(
                        compute_nodes = [
                            cyperf.models.ports_by_node.PortsByNode(
                                compute_node_id = '', 
                                ports = [
                                    ''
                                    ], )
                            ], 
                        controller_id = '', )
                    ]
            )
        else:
            return RebootPortsOperation(
        )
        """

    def testRebootPortsOperation(self):
        """Test RebootPortsOperation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
