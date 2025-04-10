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
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field

class LicenseServerMetadata(BaseModel):
    """
    LicenseServerMetadata
    """ # noqa: E501
    connection_status: Optional[StrictStr] = Field(default=None, description="The license server's connection status", alias="connectionStatus")
    failure_reason: Optional[StrictStr] = Field(default=None, description="The license server's connection failure reason", alias="failureReason")
    fingerprint: Optional[StrictStr] = Field(default=None, description="The license server's fingerprint")
    host_name: Optional[StrictStr] = Field(default=None, description="The hostname/IP of the server", alias="hostName")
    id: Optional[StrictInt] = Field(default=None, description="The unique identifier of the license server")
    interactive_fingerprint_verification: Optional[StrictBool] = Field(default=None, description="Validate the license's server fingerprint interactively", alias="interactiveFingerprintVerification")
    password: Optional[StrictStr] = Field(default=None, description="The license server's authentication password")
    pretty_conn_status: Optional[StrictStr] = Field(default=None, description="The license server's connection status in a human-readable format", alias="prettyConnStatus")
    trust_new: Optional[StrictBool] = Field(default=None, description="The flag used to skip license server's identity verifications", alias="trustNew")
    tunnel_host_name: Optional[StrictStr] = Field(default=None, description="The hostname/IP of the license server tunnel", alias="tunnelHostName")
    user: Optional[StrictStr] = Field(default=None, description="The license server's authentication user")
    __properties: ClassVar[List[str]] = ["connectionStatus", "failureReason", "fingerprint", "hostName", "id", "interactiveFingerprintVerification", "password", "prettyConnStatus", "trustNew", "tunnelHostName", "user"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of LicenseServerMetadata from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "connection_status",
            "id",
            "pretty_conn_status",
            "tunnel_host_name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LicenseServerMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "connectionStatus": obj.get("connectionStatus"),
                        "failureReason": obj.get("failureReason"),
                        "fingerprint": obj.get("fingerprint"),
                        "hostName": obj.get("hostName"),
                        "id": obj.get("id"),
                        "interactiveFingerprintVerification": obj.get("interactiveFingerprintVerification"),
                        "password": obj.get("password"),
                        "prettyConnStatus": obj.get("prettyConnStatus"),
                        "trustNew": obj.get("trustNew"),
                        "tunnelHostName": obj.get("tunnelHostName"),
                        "user": obj.get("user")
            ,
            "links": obj.get("links")
        })
        return _obj


