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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cyperf.models.api_link import APILink
from cyperf.models.dtls_settings import DTLSSettings
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field

class CiscoEncapsulation(BaseModel):
    """
    CiscoEncapsulation
    """ # noqa: E501
    dtls_enabled: StrictBool = Field(alias="DTLSEnabled")
    dtls_settings: Optional[DTLSSettings] = Field(default=None, alias="DTLSSettings")
    encapsulation_mode: StrictStr = Field(description="The encapsulation mode for inner traffic.", alias="EncapsulationMode")
    udp_port: StrictInt = Field(alias="UdpPort")
    links: Optional[List[APILink]] = None
    __properties: ClassVar[List[str]] = ["DTLSEnabled", "DTLSSettings", "EncapsulationMode", "UdpPort", "links"]

    @field_validator('encapsulation_mode')
    def encapsulation_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['DTLS', 'TLS']):
            raise ValueError("must be one of enum values ('DTLS', 'TLS')")
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
        """Create an instance of CiscoEncapsulation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of dtls_settings
        if self.dtls_settings:
            _dict['DTLSSettings'] = self.dtls_settings.to_dict()
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
        """Create an instance of CiscoEncapsulation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "DTLSEnabled": obj.get("DTLSEnabled"),
                        "DTLSSettings": DTLSSettings.from_dict(obj["DTLSSettings"]) if obj.get("DTLSSettings") is not None else None,
                        "EncapsulationMode": obj.get("EncapsulationMode"),
                        "UdpPort": obj.get("UdpPort"),
                        "links": [APILink.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None
            ,
            "links": obj.get("links")
        })
        return _obj


