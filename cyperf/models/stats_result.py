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
from cyperf.models.parameter import Parameter
from cyperf.models.snapshot import Snapshot
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field

class StatsResult(BaseModel):
    """
    StatsResult
    """ # noqa: E501
    available_filters: Optional[List[Parameter]] = Field(default=None, description="The list of available filters", alias="availableFilters")
    columns: Optional[List[StrictStr]] = Field(default=None, description="The list of columns returned by the query")
    name: Optional[StrictStr] = Field(default=None, description="The name of the query")
    snapshots: Optional[List[Snapshot]] = Field(default=None, description="The list of snapshots returned by the query")
    __properties: ClassVar[List[str]] = ["availableFilters", "columns", "name", "snapshots"]

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
        """Create an instance of StatsResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in available_filters (list)
        _items = []
        if self.available_filters:
            for _item in self.available_filters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['availableFilters'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in snapshots (list)
        _items = []
        if self.snapshots:
            for _item in self.snapshots:
                if _item:
                    _items.append(_item.to_dict())
            _dict['snapshots'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StatsResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "availableFilters": [Parameter.from_dict(_item) for _item in obj["availableFilters"]] if obj.get("availableFilters") is not None else None,
                        "columns": obj.get("columns"),
                        "name": obj.get("name"),
                        "snapshots": [Snapshot.from_dict(_item) for _item in obj["snapshots"]] if obj.get("snapshots") is not None else None
            ,
            "links": obj.get("links")
        })
        return _obj


