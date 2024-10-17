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
from cyperf.models.parameter_metadata import ParameterMetadata
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field

class Parameter(BaseModel):
    """
    Parameter
    """ # noqa: E501
    default_array_elements: Optional[List[Dict[str, StrictStr]]] = Field(default=None, description="The default values of the parameter", alias="DefaultArrayElements")
    default_source: Optional[StrictStr] = Field(default=None, description="The default source of the parameter", alias="DefaultSource")
    default_value: Optional[StrictStr] = Field(default=None, description="The default value of the parameter", alias="DefaultValue")
    element_type: Optional[StrictStr] = Field(default=None, description="The type of elements in the values array", alias="ElementType")
    var_field: Optional[StrictStr] = Field(default=None, description="The name of the ES document field", alias="field")
    id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the parameter")
    links: Optional[List[APILink]] = None
    metadata: Optional[ParameterMetadata] = Field(default=None, alias="Metadata")
    operator: Optional[StrictStr] = Field(default=None, description="The operator that the parameter supports")
    query_param: Optional[StrictStr] = Field(default=None, description="The corresponding query param", alias="queryParam")
    sources: Optional[List[StrictStr]] = Field(default=None, description="The sources of the parameter", alias="Sources")
    type: Optional[StrictStr] = Field(default=None, description="The type of the parameter", alias="Type")
    __properties: ClassVar[List[str]] = ["DefaultArrayElements", "DefaultSource", "DefaultValue", "ElementType", "field", "id", "links", "Metadata", "operator", "queryParam", "Sources", "Type"]

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
        """Create an instance of Parameter from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['Metadata'] = self.metadata.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Parameter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "DefaultArrayElements": obj.get("DefaultArrayElements"),
                        "DefaultSource": obj.get("DefaultSource"),
                        "DefaultValue": obj.get("DefaultValue"),
                        "ElementType": obj.get("ElementType"),
                        "field": obj.get("field"),
                        "id": obj.get("id"),
                        "links": [APILink.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
                        "Metadata": ParameterMetadata.from_dict(obj["Metadata"]) if obj.get("Metadata") is not None else None,
                        "operator": obj.get("operator"),
                        "queryParam": obj.get("queryParam"),
                        "Sources": obj.get("Sources"),
                        "Type": obj.get("Type")
            ,
            "links": obj.get("links")
        })
        return _obj


