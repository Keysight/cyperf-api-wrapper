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
from typing import Any, ClassVar, Dict, List
from cyperf.models.counted_feature_consumer import CountedFeatureConsumer
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field

class CountedFeatureStats(BaseModel):
    """
    Counted feature stats.
    """ # noqa: E501
    available_count: StrictInt = Field(description="Available count.", alias="availableCount")
    consumers: List[CountedFeatureConsumer] = Field(description="Consumed by.")
    feature_name: StrictStr = Field(description="The feature name.", alias="featureName")
    installed_count: StrictInt = Field(description="Total installed count.", alias="installedCount")
    __properties: ClassVar[List[str]] = ["availableCount", "consumers", "featureName", "installedCount"]

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
        """Create an instance of CountedFeatureStats from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in consumers (list)
        _items = []
        if self.consumers:
            for _item in self.consumers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['consumers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CountedFeatureStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "availableCount": obj.get("availableCount"),
                        "consumers": [CountedFeatureConsumer.from_dict(_item) for _item in obj["consumers"]] if obj.get("consumers") is not None else None,
                        "featureName": obj.get("featureName"),
                        "installedCount": obj.get("installedCount")
            ,
            "links": obj.get("links")
        })
        return _obj


