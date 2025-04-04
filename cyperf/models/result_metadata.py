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
from cyperf.models.marked_as_deleted import MarkedAsDeleted
from cyperf.models.result_file_metadata import ResultFileMetadata
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field

class ResultMetadata(BaseModel):
    """
    ResultMetadata
    """ # noqa: E501
    active_session: Optional[StrictStr] = Field(default=None, description="The id of the session where the result is currently loaded", alias="activeSession")
    config_url: Optional[StrictStr] = Field(default=None, description="The URL of the result's configuration", alias="configUrl")
    csv_url: Optional[StrictStr] = Field(default=None, description="The URL of the cached csv archive", alias="csvURL")
    display_name: Optional[StrictStr] = Field(default=None, description="The user-visible name of the result", alias="displayName")
    download_all: Optional[Any] = Field(default=None, description="Download all available test result types", alias="download-all")
    download_diagnostic: Optional[Any] = Field(default=None, description="The available test diagnostic result", alias="download-diagnostic")
    end_time: Optional[StrictInt] = Field(default=None, description="A Unix timestamp that indicates when the test ended", alias="endTime")
    files: Optional[List[ResultFileMetadata]] = Field(default=None, description="The list of result files")
    id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the result")
    last_modified: Optional[StrictInt] = Field(default=None, description="A Unix timestamp that indicates when the result was last modified", alias="lastModified")
    links: Optional[List[APILink]] = None
    marked_as_deleted: Optional[MarkedAsDeleted] = Field(default=None, alias="markedAsDeleted")
    owner: Optional[StrictStr] = Field(default=None, description="The user-visible name of the user who owns the result")
    owner_id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the user who owns the result", alias="ownerId")
    pdf_url: Optional[StrictStr] = Field(default=None, description="The URL of the cached pdf report", alias="pdfURL")
    pinned: Optional[StrictBool] = Field(default=None, description="A flag that indicates if the result's configuration is pinned")
    reporting_links: Optional[List[APILink]] = Field(default=None, description="A list of links to result reporting resources", alias="reportingLinks")
    result_url: Optional[StrictStr] = Field(default=None, description="The URL of the result", alias="resultUrl")
    start_time: Optional[StrictInt] = Field(default=None, description="A Unix timestamp that indicates when the test was started", alias="startTime")
    tags: Optional[Dict[str, StrictStr]] = Field(default=None, description="A series of tags that describe the result")
    test_name: Optional[StrictStr] = Field(default=None, description="The name of the test associated with the result", alias="testName")
    type: Optional[StrictStr] = Field(default=None, description="The application type of the result")
    user_tags: Optional[List[StrictStr]] = Field(default=None, description="The list of user defined tags", alias="userTags")
    __properties: ClassVar[List[str]] = ["activeSession", "configUrl", "csvURL", "displayName", "download-all", "download-diagnostic", "endTime", "files", "id", "lastModified", "links", "markedAsDeleted", "owner", "ownerId", "pdfURL", "pinned", "reportingLinks", "resultUrl", "startTime", "tags", "testName", "type", "userTags"]

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
        """Create an instance of ResultMetadata from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "config_url",
            "id",
            "last_modified",
            "owner",
            "owner_id",
            "result_url",
            "start_time",
            "type",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in files (list)
        _items = []
        if self.files:
            for _item in self.files:
                if _item:
                    _items.append(_item.to_dict())
            _dict['files'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # override the default output from pydantic by calling `to_dict()` of marked_as_deleted
        if self.marked_as_deleted:
            _dict['markedAsDeleted'] = self.marked_as_deleted.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in reporting_links (list)
        _items = []
        if self.reporting_links:
            for _item in self.reporting_links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['reportingLinks'] = _items
        # set to None if download_all (nullable) is None
        # and model_fields_set contains the field
        if self.download_all is None and "download_all" in self.model_fields_set:
            _dict['download-all'] = None

        # set to None if download_diagnostic (nullable) is None
        # and model_fields_set contains the field
        if self.download_diagnostic is None and "download_diagnostic" in self.model_fields_set:
            _dict['download-diagnostic'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResultMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "activeSession": obj.get("activeSession"),
                        "configUrl": obj.get("configUrl"),
                        "csvURL": obj.get("csvURL"),
                        "displayName": obj.get("displayName"),
                        "download-all": obj.get("download-all"),
                        "download-diagnostic": obj.get("download-diagnostic"),
                        "endTime": obj.get("endTime"),
                        "files": [ResultFileMetadata.from_dict(_item) for _item in obj["files"]] if obj.get("files") is not None else None,
                        "id": obj.get("id"),
                        "lastModified": obj.get("lastModified"),
                        "links": [APILink.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
                        "markedAsDeleted": MarkedAsDeleted.from_dict(obj["markedAsDeleted"]) if obj.get("markedAsDeleted") is not None else None,
                        "owner": obj.get("owner"),
                        "ownerId": obj.get("ownerId"),
                        "pdfURL": obj.get("pdfURL"),
                        "pinned": obj.get("pinned"),
                        "reportingLinks": [APILink.from_dict(_item) for _item in obj["reportingLinks"]] if obj.get("reportingLinks") is not None else None,
                        "resultUrl": obj.get("resultUrl"),
                        "startTime": obj.get("startTime"),
                        "tags": obj.get("tags"),
                        "testName": obj.get("testName"),
                        "type": obj.get("type"),
                        "userTags": obj.get("userTags")
            ,
            "links": obj.get("links")
        })
        return _obj


