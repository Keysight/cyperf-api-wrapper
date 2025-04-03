# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Contact: support@keysight.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class SessionReuseMethodTLS13(str, Enum):
    """
    The session reuse method. Must be DISABLE (default: DISABLE).
    """

    """
    allowed enum values
    """
    DISABLE = 'DISABLE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SessionReuseMethodTLS13 from a JSON string"""
        return cls(json.loads(json_str))


