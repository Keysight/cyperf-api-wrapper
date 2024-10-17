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

from cyperf.models.license_receipt import LicenseReceipt

class TestLicenseReceipt(unittest.TestCase):
    """LicenseReceipt unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LicenseReceipt:
        """Test LicenseReceipt
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LicenseReceipt`
        """
        model = LicenseReceipt()
        if include_optional:
            return LicenseReceipt(
                changed_licenses = [
                    cyperf.models.license.license(
                        activation_code = '', 
                        days_left_to_expire = 56, 
                        expiry_date = '', 
                        features = [
                            cyperf.models.feature.feature(
                                count = 56, 
                                feature_type = 'nodeLocked', 
                                is_uncounted = True, 
                                name = '', 
                                reservation = cyperf.models.feature_reservation.feature_reservation(
                                    available_count = 56, 
                                    is_allowed = True, 
                                    reserved_count = 56, 
                                    reserved_remaining_duration = 56, ), )
                            ], 
                        is_expired = True, 
                        links = [
                            cyperf.models.link.link(
                                href = '', 
                                method = '', 
                                type = '', )
                            ], 
                        maintenance_date = '', 
                        part_number_description = '', 
                        part_number_id = '', 
                        product = '', 
                        quantity = 56, )
                    ],
                is_online = True,
                operation_type = 'activation'
            )
        else:
            return LicenseReceipt(
                changed_licenses = [
                    cyperf.models.license.license(
                        activation_code = '', 
                        days_left_to_expire = 56, 
                        expiry_date = '', 
                        features = [
                            cyperf.models.feature.feature(
                                count = 56, 
                                feature_type = 'nodeLocked', 
                                is_uncounted = True, 
                                name = '', 
                                reservation = cyperf.models.feature_reservation.feature_reservation(
                                    available_count = 56, 
                                    is_allowed = True, 
                                    reserved_count = 56, 
                                    reserved_remaining_duration = 56, ), )
                            ], 
                        is_expired = True, 
                        links = [
                            cyperf.models.link.link(
                                href = '', 
                                method = '', 
                                type = '', )
                            ], 
                        maintenance_date = '', 
                        part_number_description = '', 
                        part_number_id = '', 
                        product = '', 
                        quantity = 56, )
                    ],
                is_online = True,
                operation_type = 'activation',
        )
        """

    def testLicenseReceipt(self):
        """Test LicenseReceipt"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
