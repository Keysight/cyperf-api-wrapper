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

from cyperf.api.utils_api import UtilsApi


class TestUtilsApi(unittest.TestCase):
    """UtilsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UtilsApi()

    def tearDown(self) -> None:
        pass

    def test_check_eulas(self) -> None:
        """Test case for check_eulas

        Check if all EULAs are accepted
        """
        pass

    def test_get_certificate(self) -> None:
        """Test case for get_certificate

        """
        pass

    def test_get_consumers(self) -> None:
        """Test case for get_consumers

        """
        pass

    def test_get_consumers_by_id(self) -> None:
        """Test case for get_consumers_by_id

        """
        pass

    def test_get_disk_usage(self) -> None:
        """Test case for get_disk_usage

        """
        pass

    def test_get_docs(self) -> None:
        """Test case for get_docs

        """
        pass

    def test_get_docs_json(self) -> None:
        """Test case for get_docs_json

        """
        pass

    def test_get_docs_yaml(self) -> None:
        """Test case for get_docs_yaml

        """
        pass

    def test_get_eula(self) -> None:
        """Test case for get_eula

        Retrieve EULA detail
        """
        pass

    def test_get_log_config(self) -> None:
        """Test case for get_log_config

        """
        pass

    def test_get_time(self) -> None:
        """Test case for get_time

        """
        pass

    def test_list_eulas(self) -> None:
        """Test case for list_eulas

        list of EULAs
        """
        pass

    def test_poll_disk_usage_cleanup_diagnostics(self) -> None:
        """Test case for poll_disk_usage_cleanup_diagnostics

        """
        pass

    def test_poll_disk_usage_cleanup_logs(self) -> None:
        """Test case for poll_disk_usage_cleanup_logs

        """
        pass

    def test_poll_disk_usage_cleanup_migration(self) -> None:
        """Test case for poll_disk_usage_cleanup_migration

        """
        pass

    def test_poll_disk_usage_cleanup_notifications(self) -> None:
        """Test case for poll_disk_usage_cleanup_notifications

        """
        pass

    def test_poll_disk_usage_cleanup_results(self) -> None:
        """Test case for poll_disk_usage_cleanup_results

        """
        pass

    def test_poll_generate(self) -> None:
        """Test case for poll_generate

        """
        pass

    def test_poll_upload(self) -> None:
        """Test case for poll_upload

        """
        pass

    def test_post_eula(self) -> None:
        """Test case for post_eula

        Update properties an EULA
        """
        pass

    def test_start_disk_usage_cleanup_diagnostics(self) -> None:
        """Test case for start_disk_usage_cleanup_diagnostics

        """
        pass

    def test_start_disk_usage_cleanup_logs(self) -> None:
        """Test case for start_disk_usage_cleanup_logs

        """
        pass

    def test_start_disk_usage_cleanup_migration(self) -> None:
        """Test case for start_disk_usage_cleanup_migration

        """
        pass

    def test_start_disk_usage_cleanup_notifications(self) -> None:
        """Test case for start_disk_usage_cleanup_notifications

        """
        pass

    def test_start_disk_usage_cleanup_results(self) -> None:
        """Test case for start_disk_usage_cleanup_results

        """
        pass

    def test_start_generate(self) -> None:
        """Test case for start_generate

        """
        pass

    def test_start_upload(self) -> None:
        """Test case for start_upload

        """
        pass

    def test_update_log_config(self) -> None:
        """Test case for update_log_config

        """
        pass


if __name__ == '__main__':
    unittest.main()
