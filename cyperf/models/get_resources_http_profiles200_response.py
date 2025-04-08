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
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from cyperf.models.get_resources_http_profiles200_response_one_of import GetResourcesHttpProfiles200ResponseOneOf
from cyperf.models.http_profile import HTTPProfile
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

GETRESOURCESHTTPPROFILES200RESPONSE_ONE_OF_SCHEMAS = ["GetResourcesHttpProfiles200ResponseOneOf", "List[HTTPProfile]"]

class GetResourcesHttpProfiles200Response(BaseModel):
    """
    GetResourcesHttpProfiles200Response
    """
    # data type: List[HTTPProfile]
    oneof_schema_1_validator: Optional[List[HTTPProfile]] = None
    # data type: GetResourcesHttpProfiles200ResponseOneOf
    oneof_schema_2_validator: Optional[GetResourcesHttpProfiles200ResponseOneOf] = None
    actual_instance: Optional[Union[GetResourcesHttpProfiles200ResponseOneOf, List[HTTPProfile]]] = None
    one_of_schemas: Set[str] = { "GetResourcesHttpProfiles200ResponseOneOf", "List[HTTPProfile]" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = GetResourcesHttpProfiles200Response.model_construct()
        error_messages = []
        match = 0
        # validate data type: List[HTTPProfile]
        try:
            instance.oneof_schema_1_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: GetResourcesHttpProfiles200ResponseOneOf
        if not isinstance(v, GetResourcesHttpProfiles200ResponseOneOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetResourcesHttpProfiles200ResponseOneOf`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in GetResourcesHttpProfiles200Response with oneOf schemas: GetResourcesHttpProfiles200ResponseOneOf, List[HTTPProfile]. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in GetResourcesHttpProfiles200Response with oneOf schemas: GetResourcesHttpProfiles200ResponseOneOf, List[HTTPProfile]. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
#        instance.api_client = client
        error_messages = []
        match = 0

        # deserialize data into List[HTTPProfile]
        try:
            # validation
            instance.oneof_schema_1_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_1_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GetResourcesHttpProfiles200ResponseOneOf
        try:
            instance.actual_instance = GetResourcesHttpProfiles200ResponseOneOf.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into GetResourcesHttpProfiles200Response with oneOf schemas: GetResourcesHttpProfiles200ResponseOneOf, List[HTTPProfile]. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into GetResourcesHttpProfiles200Response with oneOf schemas: GetResourcesHttpProfiles200ResponseOneOf, List[HTTPProfile]. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], GetResourcesHttpProfiles200ResponseOneOf, List[HTTPProfile]]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


