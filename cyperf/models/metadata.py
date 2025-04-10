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
from cyperf.models.config_metadata_config_data_value import ConfigMetadataConfigDataValue
from cyperf.models.reference import Reference
from cyperf.models.rtp_profile_meta import RTPProfileMeta
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field

class Metadata(BaseModel):
    """
    Metadata
    """ # noqa: E501
    direction: Optional[StrictStr] = Field(default=None, description="The direction of the strike", alias="Direction")
    is_banner: Optional[StrictBool] = Field(default=None, description="Indicates that this is a command that is required, can only be add once and also must be the first", alias="IsBanner")
    keywords: Optional[List[ConfigMetadataConfigDataValue]] = Field(default=None, description="The keywords of the strike", alias="Keywords")
    legacy_names: Optional[List[StrictStr]] = Field(default=None, description="The names of the equivalent application/strike", alias="LegacyNames")
    protocol: Optional[StrictStr] = Field(default=None, description="The protocol of the strike", alias="Protocol")
    rtp_profile_meta: Optional[RTPProfileMeta] = Field(default=None, alias="RTPProfileMeta")
    references: Optional[List[Reference]] = Field(default=None, description="The references of the strike", alias="References")
    requires_uniqueness: Optional[StrictBool] = Field(default=None, description="If true, for applications with the same protocol id, application/attack must have been uniquely identified in previous commands", alias="RequiresUniqueness")
    severity: Optional[StrictStr] = Field(default=None, description="The severity of the strike", alias="Severity")
    skip_attack_generation: Optional[StrictBool] = Field(default=None, description="If true, don't generate an attack for this strike", alias="SkipAttackGeneration")
    sort_severity: Optional[StrictStr] = Field(default=None, description="The field by which the severity is sorted", alias="SortSeverity")
    static: Optional[StrictBool] = Field(default=None, description="If true, the application/strike is managed directly by the controller", alias="Static")
    supported_apps: Optional[List[StrictStr]] = Field(default=None, description="The apps that this strike can be used with", alias="SupportedApps")
    year: Optional[StrictStr] = Field(default=None, description="The year of the strike", alias="Year")
    __properties: ClassVar[List[str]] = ["Direction", "IsBanner", "Keywords", "LegacyNames", "Protocol", "RTPProfileMeta", "References", "RequiresUniqueness", "Severity", "SkipAttackGeneration", "SortSeverity", "Static", "SupportedApps", "Year"]

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
        """Create an instance of Metadata from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in keywords (list)
        _items = []
        if self.keywords:
            for _item in self.keywords:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Keywords'] = _items
        # override the default output from pydantic by calling `to_dict()` of rtp_profile_meta
        if self.rtp_profile_meta:
            _dict['RTPProfileMeta'] = self.rtp_profile_meta.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in references (list)
        _items = []
        if self.references:
            for _item in self.references:
                if _item:
                    _items.append(_item.to_dict())
            _dict['References'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Metadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "Direction": obj.get("Direction"),
                        "IsBanner": obj.get("IsBanner"),
                        "Keywords": [ConfigMetadataConfigDataValue.from_dict(_item) for _item in obj["Keywords"]] if obj.get("Keywords") is not None else None,
                        "LegacyNames": obj.get("LegacyNames"),
                        "Protocol": obj.get("Protocol"),
                        "RTPProfileMeta": RTPProfileMeta.from_dict(obj["RTPProfileMeta"]) if obj.get("RTPProfileMeta") is not None else None,
                        "References": [Reference.from_dict(_item) for _item in obj["References"]] if obj.get("References") is not None else None,
                        "RequiresUniqueness": obj.get("RequiresUniqueness"),
                        "Severity": obj.get("Severity"),
                        "SkipAttackGeneration": obj.get("SkipAttackGeneration"),
                        "SortSeverity": obj.get("SortSeverity"),
                        "Static": obj.get("Static"),
                        "SupportedApps": obj.get("SupportedApps"),
                        "Year": obj.get("Year")
            ,
            "links": obj.get("links")
        })
        return _obj


