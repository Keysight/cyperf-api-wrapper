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
from cyperf.models.connection_persistence import ConnectionPersistence
from cyperf.models.http_version import HTTPVersion
from cyperf.models.params import Params
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field

class HTTPProfile(BaseModel):
    """
    HTTPProfile
    """ # noqa: E501
    additional_headers: Optional[Params] = Field(default=None, alias="AdditionalHeaders")
    connection_persistence: Optional[ConnectionPersistence] = Field(default=None, alias="ConnectionPersistence")
    connections_max_transactions: Optional[StrictInt] = Field(default=None, description="The maximum number of transactions for all scenario connections.", alias="ConnectionsMaxTransactions")
    description: StrictStr = Field(description="The description of the HTTP profile.", alias="Description")
    external_resource_url: Optional[StrictStr] = Field(default=None, description="The external resource URL of the HTTP profile.", alias="ExternalResourceURL")
    http_version: Optional[HTTPVersion] = Field(default=None, alias="HTTPVersion")
    headers: Optional[Params] = Field(default=None, alias="Headers")
    is_modified: Optional[StrictBool] = Field(default=None, alias="IsModified")
    name: StrictStr = Field(description="The name of the HTTP profile.", alias="Name")
    params: Optional[List[Params]] = Field(default=None, description="The list of parameters present in the HTTP profile.", alias="Params")
    use_application_server_headers: Optional[StrictBool] = Field(default=None, alias="UseApplicationServerHeaders")
    links: Optional[List[APILink]] = None
    __properties: ClassVar[List[str]] = ["AdditionalHeaders", "ConnectionPersistence", "ConnectionsMaxTransactions", "Description", "ExternalResourceURL", "HTTPVersion", "Headers", "IsModified", "Name", "Params", "UseApplicationServerHeaders", "links"]

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
        """Create an instance of HTTPProfile from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of additional_headers
        if self.additional_headers:
            _dict['AdditionalHeaders'] = self.additional_headers.to_dict()
        # override the default output from pydantic by calling `to_dict()` of headers
        if self.headers:
            _dict['Headers'] = self.headers.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in params (list)
        _items = []
        if self.params:
            for _item in self.params:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Params'] = _items
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
        """Create an instance of HTTPProfile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "AdditionalHeaders": Params.from_dict(obj["AdditionalHeaders"]) if obj.get("AdditionalHeaders") is not None else None,
                        "ConnectionPersistence": obj.get("ConnectionPersistence"),
                        "ConnectionsMaxTransactions": obj.get("ConnectionsMaxTransactions"),
                        "Description": obj.get("Description"),
                        "ExternalResourceURL": obj.get("ExternalResourceURL"),
                        "HTTPVersion": obj.get("HTTPVersion"),
                        "Headers": Params.from_dict(obj["Headers"]) if obj.get("Headers") is not None else None,
                        "IsModified": obj.get("IsModified"),
                        "Name": obj.get("Name"),
                        "Params": [Params.from_dict(_item) for _item in obj["Params"]] if obj.get("Params") is not None else None,
                        "UseApplicationServerHeaders": obj.get("UseApplicationServerHeaders"),
                        "links": [APILink.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None
            ,
            "links": obj.get("links")
        })
        return _obj


