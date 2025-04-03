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
from cyperf.models.config import Config
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field

class AppsecConfig(BaseModel):
    """
    AppsecConfig
    """ # noqa: E501
    config: Optional[Config] = Field(default=None, alias="Config")
    session_id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the session this configuration belongs to", alias="SessionID")
    template_id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the CyPerf configuration template from which this configuration was created", alias="TemplateID")
    config_type_name: StrictStr = Field(description="Used for API clients to decide what type of config they have loaded", alias="configTypeName")
    data_model_version: Optional[StrictStr] = Field(default=None, description="The version of the data model used for this configuration", alias="dataModelVersion")
    id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the CyPerf configuration")
    links: Optional[List[APILink]] = None
    name: Optional[StrictStr] = Field(default=None, description="The name of the configuration")
    __properties: ClassVar[List[str]] = ["Config", "SessionID", "TemplateID", "configTypeName", "dataModelVersion", "id", "links", "name"]

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
        """Create an instance of AppsecConfig from a JSON string"""
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
            "session_id",
            "template_id",
            "data_model_version",
            "id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of config
        if self.config:
            _dict['Config'] = self.config.to_dict()
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
        """Create an instance of AppsecConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "Config": Config.from_dict(obj["Config"]) if obj.get("Config") is not None else None,
                        "SessionID": obj.get("SessionID"),
                        "TemplateID": obj.get("TemplateID"),
                        "configTypeName": obj.get("configTypeName"),
                        "dataModelVersion": obj.get("dataModelVersion"),
                        "id": obj.get("id"),
                        "links": [APILink.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
                        "name": obj.get("name")
            ,
            "links": obj.get("links")
        })
        return _obj


