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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from cyperf.models.api_link import APILink
from cyperf.models.objective_value_entry import ObjectiveValueEntry
from cyperf.models.segment_type import SegmentType
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field

class TimelineSegment(BaseModel):
    """
    TimelineSegment
    """ # noqa: E501
    duration: StrictInt = Field(description="The duration of the timeline segment (default: 600).", alias="Duration")
    segment_type: SegmentType = Field(description="The segment's type. Must be one of: SteadySegment, StepUpSegment, StepDownSegment.", alias="SegmentType")
    warm_up_period: Optional[StrictInt] = Field(default=None, description="Deprecated. Use ObjectivesAndTimeline.WarmUp instead. The time that servers may need to warm up, when clients should wait (default: 0 seconds).", alias="WarmUpPeriod")
    id: StrictStr
    objective_unit: Optional[StrictStr] = Field(default=None, description="The measurement unit for the objective value. Only applicable for Throughput objectives.", alias="ObjectiveUnit")
    objective_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The objective value for this timeline segment.", alias="ObjectiveValue")
    primary_objective_unit: StrictStr = Field(description="Deprecated. Use PrimaryObjective.Timeline[].ObjectiveUnit instead. The primary objective unit. (default: Gbps)", alias="PrimaryObjectiveUnit")
    primary_objective_value: Union[StrictFloat, StrictInt] = Field(description="Deprecated. Use PrimaryObjective.Timeline[].ObjectiveValue instead. The primary objective value (default: 1).", alias="PrimaryObjectiveValue")
    secondary_objective_values: Optional[List[ObjectiveValueEntry]] = Field(default=None, description="Deprecated. Use SecondaryObjective.ObjectiveValue/ObjectiveUnit instead. The secondary objectives values.", alias="SecondaryObjectiveValues")
    links: Optional[List[APILink]] = None
    __properties: ClassVar[List[str]] = ["Duration", "SegmentType", "WarmUpPeriod", "id", "ObjectiveUnit", "ObjectiveValue", "PrimaryObjectiveUnit", "PrimaryObjectiveValue", "SecondaryObjectiveValues", "links"]

    @field_validator('objective_unit')
    def objective_unit_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['', 'bps', 'Kbps', 'Mbps', 'Gbps']):
            raise ValueError("must be one of enum values ('', 'bps', 'Kbps', 'Mbps', 'Gbps')")
        return value

    @field_validator('primary_objective_unit')
    def primary_objective_unit_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['', 'bps', 'Kbps', 'Mbps', 'Gbps']):
            raise ValueError("must be one of enum values ('', 'bps', 'Kbps', 'Mbps', 'Gbps')")
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
        """Create an instance of TimelineSegment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in secondary_objective_values (list)
        _items = []
        if self.secondary_objective_values:
            for _item in self.secondary_objective_values:
                if _item:
                    _items.append(_item.to_dict())
            _dict['SecondaryObjectiveValues'] = _items
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
        """Create an instance of TimelineSegment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "Duration": obj.get("Duration"),
                        "SegmentType": obj.get("SegmentType"),
                        "WarmUpPeriod": obj.get("WarmUpPeriod"),
                        "id": obj.get("id"),
                        "ObjectiveUnit": obj.get("ObjectiveUnit"),
                        "ObjectiveValue": obj.get("ObjectiveValue"),
                        "PrimaryObjectiveUnit": obj.get("PrimaryObjectiveUnit"),
                        "PrimaryObjectiveValue": obj.get("PrimaryObjectiveValue"),
                        "SecondaryObjectiveValues": [ObjectiveValueEntry.from_dict(_item) for _item in obj["SecondaryObjectiveValues"]] if obj.get("SecondaryObjectiveValues") is not None else None,
                        "links": [APILink.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None
            ,
            "links": obj.get("links")
        })
        return _obj


