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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cyperf.models.api_link import APILink
from cyperf.models.compute_node import ComputeNode
from cyperf.models.health_issue import HealthIssue
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field

class Controller(BaseModel):
    """
    Controller
    """ # noqa: E501
    compute_nodes: Optional[List[ComputeNode]] = Field(default=None, description="The compute nodes of the controller", alias="computeNodes")
    health_details: Optional[List[HealthIssue]] = Field(default=None, description="Details regarding any health issue of the controller", alias="healthDetails")
    healthy: Optional[StrictBool] = Field(default=None, description="Whether the controller has any health issue or not")
    id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the controller")
    links: Optional[List[APILink]] = None
    name: Optional[StrictStr] = Field(default=None, description="A user-friendly display name for the controller")
    serial: Optional[StrictStr] = Field(default=None, description="The serial of the controller")
    type: Optional[StrictStr] = Field(default=None, description="The type of the controller")
    __properties: ClassVar[List[str]] = ["computeNodes", "healthDetails", "healthy", "id", "links", "name", "serial", "type"]

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
        """Create an instance of Controller from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in compute_nodes (list)
        _items = []
        if self.compute_nodes:
            for _item in self.compute_nodes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['computeNodes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in health_details (list)
        _items = []
        if self.health_details:
            for _item in self.health_details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['healthDetails'] = _items
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
        """Create an instance of Controller from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "computeNodes": [ComputeNode.from_dict(_item) for _item in obj["computeNodes"]] if obj.get("computeNodes") is not None else None,
                        "healthDetails": [HealthIssue.from_dict(_item) for _item in obj["healthDetails"]] if obj.get("healthDetails") is not None else None,
                        "healthy": obj.get("healthy"),
                        "id": obj.get("id"),
                        "links": [APILink.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
                        "name": obj.get("name"),
                        "serial": obj.get("serial"),
                        "type": obj.get("type")
            ,
            "links": obj.get("links")
        })
        return _obj


