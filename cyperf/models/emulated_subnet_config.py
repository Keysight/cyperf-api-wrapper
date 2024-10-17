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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field

class EmulatedSubnetConfig(BaseModel):
    """
    The Inner IP Range assigned to the current test configuration
    """ # noqa: E501
    host_count_per_tunnel: StrictInt = Field(alias="HostCountPerTunnel")
    hosts_increment: Annotated[str, Field(strict=True)] = Field(description="The IP incrementation rule (default: 0.0.0.1).", alias="HostsIncrement")
    hosts_prefix: StrictInt = Field(description="The network mask of the IP Range (default: 16).", alias="HostsPrefix")
    increment: Annotated[str, Field(strict=True)] = Field(description="The IP incrementation rule (default: 0.0.1.0).", alias="Increment")
    network_tags: List[StrictStr] = Field(description="A list of tags.", alias="networkTags")
    prefix: StrictInt = Field(description="The network mask of the IP Range (default: 16).", alias="Prefix")
    start: Annotated[str, Field(strict=True)] = Field(description="The start IP for the IPRange (default: 10.0.0.10).", alias="Start")
    total_host_count: StrictStr = Field(alias="TotalHostCount")
    __properties: ClassVar[List[str]] = ["HostCountPerTunnel", "HostsIncrement", "HostsPrefix", "Increment", "networkTags", "Prefix", "Start", "TotalHostCount"]

    @field_validator('hosts_increment')
    def hosts_increment_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(([0-9a-fA-F]{1,4}:){5,5}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}|([0-9a-fA-F]{1,4}:){1,4}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){2,2}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){3,3}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){4,4})|:(:[0-9a-fA-F]{1,4}){1,5}):((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])))$", value):
            raise ValueError(r"must validate the regular expression /^(((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(([0-9a-fA-F]{1,4}:){5,5}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}|([0-9a-fA-F]{1,4}:){1,4}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){2,2}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){3,3}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){4,4})|:(:[0-9a-fA-F]{1,4}){1,5}):((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])))$/")
        return value

    @field_validator('increment')
    def increment_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(([0-9a-fA-F]{1,4}:){5,5}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}|([0-9a-fA-F]{1,4}:){1,4}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){2,2}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){3,3}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){4,4})|:(:[0-9a-fA-F]{1,4}){1,5}):((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])))$", value):
            raise ValueError(r"must validate the regular expression /^(((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(([0-9a-fA-F]{1,4}:){5,5}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}|([0-9a-fA-F]{1,4}:){1,4}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){2,2}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){3,3}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){4,4})|:(:[0-9a-fA-F]{1,4}){1,5}):((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])))$/")
        return value

    @field_validator('start')
    def start_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(([0-9a-fA-F]{1,4}:){5,5}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}|([0-9a-fA-F]{1,4}:){1,4}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){2,2}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){3,3}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){4,4})|:(:[0-9a-fA-F]{1,4}){1,5}):((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])))$", value):
            raise ValueError(r"must validate the regular expression /^(((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(([0-9a-fA-F]{1,4}:){5,5}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}|([0-9a-fA-F]{1,4}:){1,4}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){2,2}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){3,3}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){4,4})|:(:[0-9a-fA-F]{1,4}){1,5}):((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])))$/")
        return value

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
        """Create an instance of EmulatedSubnetConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EmulatedSubnetConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "HostCountPerTunnel": obj.get("HostCountPerTunnel"),
                        "HostsIncrement": obj.get("HostsIncrement"),
                        "HostsPrefix": obj.get("HostsPrefix"),
                        "Increment": obj.get("Increment"),
                        "networkTags": obj.get("networkTags"),
                        "Prefix": obj.get("Prefix"),
                        "Start": obj.get("Start"),
                        "TotalHostCount": obj.get("TotalHostCount")
            ,
            "links": obj.get("links")
        })
        return _obj


