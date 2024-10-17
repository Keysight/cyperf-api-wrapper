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
from cyperf.models.filtered_stat import FilteredStat
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field

class GenerateCSVReportsOperation(BaseModel):
    """
    GenerateCSVReportsOperation
    """ # noqa: E501
    force_generate: Optional[StrictBool] = Field(default=None, description="Generate a new CSV report replacing the cached one", alias="forceGenerate")
    var_from: Optional[StrictStr] = Field(default=None, description="(optional) UNIX time in milliseconds or milliseconds from the test start (based on useRelativeTime flag) as the query interval start. Defaults to 'now-5m' (in milliseconds) for false useRelativeTime, and 0 otherwise.", alias="from")
    interval: Optional[StrictStr] = Field(default=None, description="(optional) The interval used to aggregate the statistics snapshots")
    stats: Optional[List[FilteredStat]] = Field(default=None, description="The stat views for which a CSV report will be generated")
    to: Optional[StrictStr] = Field(default=None, description="(optional) UNIX time in milliseconds or milliseconds from the test start (based on useRelativeTime flag) as the query interval end. Defaults to 'now-7s' (in milliseconds).")
    use_relative_time: Optional[StrictBool] = Field(default=None, description="(optional) Specifies if the from/to params use milliseconds from test start or UNIX time in milliseconds.", alias="useRelativeTime")
    __properties: ClassVar[List[str]] = ["forceGenerate", "from", "interval", "stats", "to", "useRelativeTime"]

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
        """Create an instance of GenerateCSVReportsOperation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in stats (list)
        _items = []
        if self.stats:
            for _item in self.stats:
                if _item:
                    _items.append(_item.to_dict())
            _dict['stats'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GenerateCSVReportsOperation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "forceGenerate": obj.get("forceGenerate"),
                        "from": obj.get("from"),
                        "interval": obj.get("interval"),
                        "stats": [FilteredStat.from_dict(_item) for _item in obj["stats"]] if obj.get("stats") is not None else None,
                        "to": obj.get("to"),
                        "useRelativeTime": obj.get("useRelativeTime")
            ,
            "links": obj.get("links")
        })
        return _obj


