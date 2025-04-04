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


class StreamPayloadType(str, Enum):
    """
    StreamPayloadType
    """

    """
    allowed enum values
    """
    RANDOM = 'RANDOM'
    PSEUDORANDOM = 'PSEUDORANDOM'
    LESS_THAN_NIL_GREATER_THAN = '<nil>'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of StreamPayloadType from a JSON string"""
        return cls(json.loads(json_str))


