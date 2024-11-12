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
from cyperf.models.track_type import TrackType
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field

class MediaTrack(BaseModel):
    """
    MediaTrack
    """ # noqa: E501
    bitrate: Optional[StrictInt] = Field(default=None, alias="Bitrate")
    bitrate_kbps: Optional[StrictInt] = Field(default=None, alias="BitrateKbps")
    codec: Optional[StrictStr] = Field(default=None, alias="Codec")
    codec_description: Optional[StrictStr] = Field(default=None, alias="CodecDescription")
    track_id: StrictStr = Field(alias="TrackId")
    track_type: TrackType = Field(alias="TrackType")
    id: StrictStr
    __properties: ClassVar[List[str]] = ["Bitrate", "BitrateKbps", "Codec", "CodecDescription", "TrackId", "TrackType", "id"]

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
        """Create an instance of MediaTrack from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MediaTrack from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "Bitrate": obj.get("Bitrate"),
                        "BitrateKbps": obj.get("BitrateKbps"),
                        "Codec": obj.get("Codec"),
                        "CodecDescription": obj.get("CodecDescription"),
                        "TrackId": obj.get("TrackId"),
                        "TrackType": obj.get("TrackType"),
                        "id": obj.get("id")
            ,
            "links": obj.get("links")
        })
        return _obj


