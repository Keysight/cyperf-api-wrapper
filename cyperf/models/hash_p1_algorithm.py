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


class HashP1Algorithm(str, Enum):
    """
    HashP1Algorithm
    """

    """
    allowed enum values
    """
    HMAC_MD5 = 'HMAC MD5'
    HMAC_SHA1 = 'HMAC SHA1'
    AES_XCBC = 'AES XCBC'
    HMAC_SHA256 = 'HMAC SHA256'
    HMAC_SHA384 = 'HMAC SHA384'
    HMAC_SHA512 = 'HMAC SHA512'
    P1_MINUS_HASH_MINUS_HMAC_MINUS_MD5 = 'P1-HASH-HMAC-MD5'
    HASH_MINUS_HMAC_MINUS_SHA1 = 'HASH-HMAC-SHA1'
    HASH_MINUS_AES_MINUS_XCBC = 'HASH-AES-XCBC'
    HASH_MINUS_HMAC_MINUS_SHA256 = 'HASH-HMAC-SHA256'
    HASH_MINUS_HMAC_MINUS_SHA384 = 'HASH-HMAC-SHA384'
    HASH_MINUS_HMAC_MINUS_SHA512 = 'HASH-HMAC-SHA512'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of HashP1Algorithm from a JSON string"""
        return cls(json.loads(json_str))


