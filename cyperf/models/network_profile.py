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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cyperf.models.api_link import APILink
from cyperf.models.dut_network import DUTNetwork
from cyperf.models.ip_network import IPNetwork
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field

class NetworkProfile(BaseModel):
    """
    The networks assigned to the current test configuration
    """ # noqa: E501
    dut_network_segment: Optional[List[DUTNetwork]] = Field(default=None, alias="DUTNetworkSegment")
    ip_network_segment: Optional[List[IPNetwork]] = Field(default=None, alias="IPNetworkSegment")
    id: StrictStr
    links: Optional[List[APILink]] = None
    __properties: ClassVar[List[str]] = ["DUTNetworkSegment", "IPNetworkSegment", "id", "links"]

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
        """Create an instance of NetworkProfile from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in dut_network_segment (list)
        _items = []
        if self.dut_network_segment:
            for _item in self.dut_network_segment:
                if _item:
                    _items.append(_item.to_dict())
            _dict['DUTNetworkSegment'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in ip_network_segment (list)
        _items = []
        if self.ip_network_segment:
            for _item in self.ip_network_segment:
                if _item:
                    _items.append(_item.to_dict())
            _dict['IPNetworkSegment'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NetworkProfile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "DUTNetworkSegment": [DUTNetwork.from_dict(_item) for _item in obj["DUTNetworkSegment"]] if obj.get("DUTNetworkSegment") is not None else None,
                        "IPNetworkSegment": [IPNetwork.from_dict(_item) for _item in obj["IPNetworkSegment"]] if obj.get("IPNetworkSegment") is not None else None,
                        "id": obj.get("id"),
                        "links": [APILink.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None
            ,
            "links": obj.get("links")
        })
        return _obj


