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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictBytes, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from cyperf.models.api_link import APILink
from cyperf.models.cert_config import CertConfig
from cyperf.models.cipher_tls12 import CipherTLS12
from cyperf.models.cipher_tls13 import CipherTLS13
from cyperf.models.conflict import Conflict
from cyperf.models.params import Params
from cyperf.models.session_reuse_method_tls12 import SessionReuseMethodTLS12
from cyperf.models.session_reuse_method_tls13 import SessionReuseMethodTLS13
from cyperf.models.supported_group_tls13 import SupportedGroupTLS13
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field

class TLSProfile(BaseModel):
    """
    TLSProfile
    """ # noqa: E501
    certificate_file: Optional[Params] = Field(default=None, description="The certificate file of the TLS profile.", alias="certificateFile")
    cipher: Optional[CipherTLS12] = None
    cipher12: Optional[CipherTLS12] = None
    cipher13: Optional[CipherTLS13] = None
    ciphers12: Optional[List[CipherTLS12]] = None
    ciphers13: Optional[List[CipherTLS13]] = None
    dh_file: Optional[Params] = Field(default=None, alias="dhFile")
    get_tls_conflicts: Optional[List[Union[StrictBytes, StrictStr]]] = Field(default=None, alias="get-tls-conflicts")
    immediate_close: Optional[StrictBool] = Field(default=None, description="The immediate FIN after close notify", alias="immediateClose")
    key_file: Optional[Params] = Field(default=None, description="The key file of the TLS profile.", alias="keyFile")
    key_file_password: Optional[StrictStr] = Field(default=None, description="The key file password of the TLS profile.", alias="keyFilePassword")
    links: Optional[List[APILink]] = None
    middle_box_enabled: Optional[StrictBool] = Field(default=None, description="If true, the middle box compatibility will be enabled", alias="middleBoxEnabled")
    profile_id: StrictStr = Field(description="The ID of the TLS profile (default: TLSProfile).", alias="profileId")
    resolve_tls_conflicts: Optional[List[Conflict]] = Field(default=None, alias="resolve-tls-conflicts")
    send_close_notify: Optional[StrictBool] = Field(default=None, description="If true, a TLS close-notify alert will be sent while closing the TLS session", alias="sendCloseNotify")
    session_reuse_count: Optional[StrictInt] = Field(default=None, alias="sessionReuseCount")
    session_reuse_method: Optional[SessionReuseMethodTLS12] = Field(default=None, alias="sessionReuseMethod")
    session_reuse_method12: Optional[SessionReuseMethodTLS12] = Field(default=None, alias="sessionReuseMethod12")
    session_reuse_method13: Optional[SessionReuseMethodTLS13] = Field(default=None, alias="sessionReuseMethod13")
    sni_cert_configs: Optional[List[CertConfig]] = Field(default=None, description="The certificate configs per SNI of the TLS profile.", alias="sniCertConfigs")
    sni_enabled: StrictBool = Field(description="The enable status of the SNI configuration (default: false).", alias="sniEnabled")
    supported_groups13: Optional[List[SupportedGroupTLS13]] = Field(default=None, alias="supportedGroups13")
    tls12_enabled: StrictBool = Field(alias="tls12Enabled")
    tls13_enabled: Optional[StrictBool] = Field(default=None, alias="tls13Enabled")
    use_tls_profile: Optional[StrictBool] = Field(default=None, description="When disabled, the connection is not TLS secured (default: true).", alias="useTlsProfile")
    version: StrictStr = Field(description="The version of the TLS profile (default: NONE). Must be one of: NONE or TLSv1.2 or TLSv1.3.")
    __properties: ClassVar[List[str]] = ["certificateFile", "cipher", "cipher12", "cipher13", "ciphers12", "ciphers13", "dhFile", "get-tls-conflicts", "immediateClose", "keyFile", "keyFilePassword", "links", "middleBoxEnabled", "profileId", "resolve-tls-conflicts", "sendCloseNotify", "sessionReuseCount", "sessionReuseMethod", "sessionReuseMethod12", "sessionReuseMethod13", "sniCertConfigs", "sniEnabled", "supportedGroups13", "tls12Enabled", "tls13Enabled", "useTlsProfile", "version"]

    @field_validator('version')
    def version_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['NONE', 'TLSv1.2', 'TLSv1.3']):
            raise ValueError("must be one of enum values ('NONE', 'TLSv1.2', 'TLSv1.3')")
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
        """Create an instance of TLSProfile from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of certificate_file
        if self.certificate_file:
            _dict['certificateFile'] = self.certificate_file.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dh_file
        if self.dh_file:
            _dict['dhFile'] = self.dh_file.to_dict()
        # override the default output from pydantic by calling `to_dict()` of key_file
        if self.key_file:
            _dict['keyFile'] = self.key_file.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in resolve_tls_conflicts (list)
        _items = []
        if self.resolve_tls_conflicts:
            for _item in self.resolve_tls_conflicts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['resolve-tls-conflicts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sni_cert_configs (list)
        _items = []
        if self.sni_cert_configs:
            for _item in self.sni_cert_configs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sniCertConfigs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TLSProfile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "certificateFile": Params.from_dict(obj["certificateFile"]) if obj.get("certificateFile") is not None else None,
                        "cipher": obj.get("cipher"),
                        "cipher12": obj.get("cipher12"),
                        "cipher13": obj.get("cipher13"),
                        "ciphers12": obj.get("ciphers12"),
                        "ciphers13": obj.get("ciphers13"),
                        "dhFile": Params.from_dict(obj["dhFile"]) if obj.get("dhFile") is not None else None,
                        "get-tls-conflicts": obj.get("get-tls-conflicts"),
                        "immediateClose": obj.get("immediateClose"),
                        "keyFile": Params.from_dict(obj["keyFile"]) if obj.get("keyFile") is not None else None,
                        "keyFilePassword": obj.get("keyFilePassword"),
                        "links": [APILink.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
                        "middleBoxEnabled": obj.get("middleBoxEnabled"),
                        "profileId": obj.get("profileId"),
                        "resolve-tls-conflicts": [Conflict.from_dict(_item) for _item in obj["resolve-tls-conflicts"]] if obj.get("resolve-tls-conflicts") is not None else None,
                        "sendCloseNotify": obj.get("sendCloseNotify"),
                        "sessionReuseCount": obj.get("sessionReuseCount"),
                        "sessionReuseMethod": obj.get("sessionReuseMethod"),
                        "sessionReuseMethod12": obj.get("sessionReuseMethod12"),
                        "sessionReuseMethod13": obj.get("sessionReuseMethod13"),
                        "sniCertConfigs": [CertConfig.from_dict(_item) for _item in obj["sniCertConfigs"]] if obj.get("sniCertConfigs") is not None else None,
                        "sniEnabled": obj.get("sniEnabled"),
                        "supportedGroups13": obj.get("supportedGroups13"),
                        "tls12Enabled": obj.get("tls12Enabled"),
                        "tls13Enabled": obj.get("tls13Enabled"),
                        "useTlsProfile": obj.get("useTlsProfile"),
                        "version": obj.get("version")
            ,
            "links": obj.get("links")
        })
        return _obj


