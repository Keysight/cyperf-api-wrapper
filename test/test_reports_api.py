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

from cyperf.api.reports_api import ReportsApi


class TestReportsApi(unittest.TestCase):
    """ReportsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ReportsApi()

    def tearDown(self) -> None:
        pass

    def test_download_pdf(self) -> None:
        """Test case for download_pdf

        """
        pass

    def test_get_download_csv_by_id(self) -> None:
        """Test case for get_download_csv_by_id

        """
        pass

    def test_poll_results_generate_csv(self) -> None:
        """Test case for poll_results_generate_csv

        """
        pass

    def test_poll_results_generate_pdf(self) -> None:
        """Test case for poll_results_generate_pdf

        """
        pass

    def test_start_results_generate_csv(self) -> None:
        """Test case for start_results_generate_csv

        """
        pass

    def test_start_results_generate_pdf(self) -> None:
        """Test case for start_results_generate_pdf

        """
        pass


if __name__ == '__main__':
    unittest.main()
