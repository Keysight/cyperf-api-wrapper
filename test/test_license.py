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

from cyperf.models.license import License

class TestLicense(unittest.TestCase):
    """License unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> License:
        """Test License
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `License`
        """
        model = License()
        if include_optional:
            return License(
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
                quantity = 56
            )
        else:
            return License(
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
                quantity = 56,
        )
        """

    def testLicense(self):
        """Test License"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
