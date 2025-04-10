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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictBytes, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field

class RTPProfileMeta(BaseModel):
    """
    RTPProfileMeta
    """ # noqa: E501
    custom_header_len_offset: Optional[StrictInt] = Field(default=None, description="The offset where the custom header length field is present", alias="CustomHeaderLenOffset")
    custom_header_len_size: Optional[StrictInt] = Field(default=None, description="The length of the custom header length field is present", alias="CustomHeaderLenSize")
    custom_header_signature: Optional[Union[StrictBytes, StrictStr]] = Field(default=None, description="The signature of the custom header", alias="CustomHeaderSignature")
    custom_header_signature_offset: Optional[StrictInt] = Field(default=None, description="The offset where the custom header signature can be found", alias="CustomHeaderSignatureOffset")
    custom_header_size: Optional[StrictInt] = Field(default=None, description="The max size of the custom header", alias="CustomHeaderSize")
    encryption_mode: Optional[StrictStr] = Field(default=None, description="The desired encryption mode", alias="EncryptionMode")
    requires_rtp_profile: Optional[StrictBool] = Field(default=None, description="Indicates that this applicaiton type requires an RTP profile", alias="RequiresRTPProfile")
    __properties: ClassVar[List[str]] = ["CustomHeaderLenOffset", "CustomHeaderLenSize", "CustomHeaderSignature", "CustomHeaderSignatureOffset", "CustomHeaderSize", "EncryptionMode", "RequiresRTPProfile"]

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
        """Create an instance of RTPProfileMeta from a JSON string"""
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
        """Create an instance of RTPProfileMeta from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "CustomHeaderLenOffset": obj.get("CustomHeaderLenOffset"),
                        "CustomHeaderLenSize": obj.get("CustomHeaderLenSize"),
                        "CustomHeaderSignature": obj.get("CustomHeaderSignature"),
                        "CustomHeaderSignatureOffset": obj.get("CustomHeaderSignatureOffset"),
                        "CustomHeaderSize": obj.get("CustomHeaderSize"),
                        "EncryptionMode": obj.get("EncryptionMode"),
                        "RequiresRTPProfile": obj.get("RequiresRTPProfile")
            ,
            "links": obj.get("links")
        })
        return _obj


