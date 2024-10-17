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
from cyperf.models.api_link import APILink
from cyperf.models.config_metadata_config_data_value import ConfigMetadataConfigDataValue
from cyperf.models.version import Version
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field

class ConfigMetadata(BaseModel):
    """
    ConfigMetadata
    """ # noqa: E501
    application: Optional[StrictStr] = None
    config_data: Optional[Dict[str, ConfigMetadataConfigDataValue]] = Field(default=None, description="The actual configuration object", alias="configData")
    config_url: Optional[StrictStr] = Field(default=None, description="The backend URL of the saved config data", alias="configUrl")
    created_on: Optional[StrictInt] = Field(default=None, description="A Unix timestamp that indicates when config was created", alias="createdOn")
    display_name: Optional[StrictStr] = Field(default=None, description="The user-visible name of the configuration", alias="displayName")
    encoded_files: Optional[StrictBool] = Field(default=None, alias="encodedFiles")
    id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the configuration")
    last_accessed: Optional[StrictInt] = Field(default=None, description="A Unix timestamp that indicates when config was last opened or modified", alias="lastAccessed")
    last_modified: Optional[StrictInt] = Field(default=None, description="A Unix timestamp that indicates when config was last modified", alias="lastModified")
    linked_resources: Optional[List[APILink]] = Field(default=None, alias="linkedResources")
    owner: Optional[StrictStr] = Field(default=None, description="A user-friendly display name of the config's owner")
    owner_id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the config's owner", alias="ownerId")
    readonly: Optional[StrictBool] = Field(default=None, description="Indicates if the configuration can be modified.")
    tags: Optional[Dict[str, StrictStr]] = Field(default=None, description="Tags used for categorizing configs")
    type: Optional[StrictStr] = Field(default=None, description="The type of config")
    version: Optional[Version] = None
    __properties: ClassVar[List[str]] = ["application", "configData", "configUrl", "createdOn", "displayName", "encodedFiles", "id", "lastAccessed", "lastModified", "linkedResources", "owner", "ownerId", "readonly", "tags", "type", "version"]

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
        """Create an instance of ConfigMetadata from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "created_on",
            "id",
            "last_modified",
            "owner",
            "owner_id",
            "readonly",
            "type",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each value in config_data (dict)
        _field_dict = {}
        if self.config_data:
            for _key in self.config_data:
                if self.config_data[_key]:
                    _field_dict[_key] = self.config_data[_key].to_dict()
            _dict['configData'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each item in linked_resources (list)
        _items = []
        if self.linked_resources:
            for _item in self.linked_resources:
                if _item:
                    _items.append(_item.to_dict())
            _dict['linkedResources'] = _items
        # override the default output from pydantic by calling `to_dict()` of version
        if self.version:
            _dict['version'] = self.version.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "application": obj.get("application"),
                        "configData": dict(
                (_k, ConfigMetadataConfigDataValue.from_dict(_v))
                for _k, _v in obj["configData"].items()
            )
            if obj.get("configData") is not None
            else None,
                        "configUrl": obj.get("configUrl"),
                        "createdOn": obj.get("createdOn"),
                        "displayName": obj.get("displayName"),
                        "encodedFiles": obj.get("encodedFiles"),
                        "id": obj.get("id"),
                        "lastAccessed": obj.get("lastAccessed"),
                        "lastModified": obj.get("lastModified"),
                        "linkedResources": [APILink.from_dict(_item) for _item in obj["linkedResources"]] if obj.get("linkedResources") is not None else None,
                        "owner": obj.get("owner"),
                        "ownerId": obj.get("ownerId"),
                        "readonly": obj.get("readonly"),
                        "tags": obj.get("tags"),
                        "type": obj.get("type"),
                        "version": Version.from_dict(obj["version"]) if obj.get("version") is not None else None
            ,
            "links": obj.get("links")
        })
        return _obj


