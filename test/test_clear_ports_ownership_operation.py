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

from cyperf.models.clear_ports_ownership_operation import ClearPortsOwnershipOperation

class TestClearPortsOwnershipOperation(unittest.TestCase):
    """ClearPortsOwnershipOperation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClearPortsOwnershipOperation:
        """Test ClearPortsOwnershipOperation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClearPortsOwnershipOperation`
        """
        model = ClearPortsOwnershipOperation()
        if include_optional:
            return ClearPortsOwnershipOperation(
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
            return ClearPortsOwnershipOperation(
        )
        """

    def testClearPortsOwnershipOperation(self):
        """Test ClearPortsOwnershipOperation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
