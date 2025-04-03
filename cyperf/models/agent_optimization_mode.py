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


class AgentOptimizationMode(str, Enum):
    """
    Use this property to switch between different agent optimization strategies (default: BALANCED_MODE)
    """

    """
    allowed enum values
    """
    BALANCED_MODE = 'BALANCED_MODE'
    RATE_MODE = 'RATE_MODE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AgentOptimizationMode from a JSON string"""
        return cls(json.loads(json_str))


