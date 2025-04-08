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

from cyperf.api.notifications_api import NotificationsApi


class TestNotificationsApi(unittest.TestCase):
    """NotificationsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = NotificationsApi()

    def tearDown(self) -> None:
        pass

    def test_delete_notification(self) -> None:
        """Test case for delete_notification

        """
        pass

    def test_get_notification_by_id(self) -> None:
        """Test case for get_notification_by_id

        """
        pass

    def test_get_notification_counts(self) -> None:
        """Test case for get_notification_counts

        """
        pass

    def test_get_notifications(self) -> None:
        """Test case for get_notifications

        """
        pass

    def test_poll_notifications_cleanup(self) -> None:
        """Test case for poll_notifications_cleanup

        """
        pass

    def test_poll_notifications_dismiss(self) -> None:
        """Test case for poll_notifications_dismiss

        """
        pass

    def test_start_notifications_cleanup(self) -> None:
        """Test case for start_notifications_cleanup

        """
        pass

    def test_start_notifications_dismiss(self) -> None:
        """Test case for start_notifications_dismiss

        """
        pass


if __name__ == '__main__':
    unittest.main()
