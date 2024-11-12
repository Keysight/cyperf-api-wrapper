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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cyperf.models.capture import Capture
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field

class AddInput(BaseModel):
    """
    AddInput
    """ # noqa: E501
    action_index: Optional[StrictInt] = Field(default=None, alias="ActionIndex")
    action_name: Optional[StrictStr] = Field(default=None, alias="ActionName")
    captures: Optional[List[Capture]] = Field(default=None, alias="Captures")
    exchange_index_insert_at: Optional[StrictInt] = Field(default=None, alias="ExchangeIndexInsertAt")
    flow_index_insert_at: Optional[StrictInt] = Field(default=None, alias="FlowIndexInsertAt")
    type: Optional[StrictStr] = Field(default=None, alias="Type")
    __properties: ClassVar[List[str]] = ["ActionIndex", "ActionName", "Captures", "ExchangeIndexInsertAt", "FlowIndexInsertAt", "Type"]

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
        """Create an instance of AddInput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in captures (list)
        _items = []
        if self.captures:
            for _item in self.captures:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Captures'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AddInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "ActionIndex": obj.get("ActionIndex"),
                        "ActionName": obj.get("ActionName"),
                        "Captures": [Capture.from_dict(_item) for _item in obj["Captures"]] if obj.get("Captures") is not None else None,
                        "ExchangeIndexInsertAt": obj.get("ExchangeIndexInsertAt"),
                        "FlowIndexInsertAt": obj.get("FlowIndexInsertAt"),
                        "Type": obj.get("Type")
            ,
            "links": obj.get("links")
        })
        return _obj


