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
from typing_extensions import Annotated
from cyperf.models.api_link import APILink
from cyperf.models.auth_settings import AuthSettings
from cyperf.models.pangp_encapsulation import PANGPEncapsulation
from cyperf.models.tcp_profile import TcpProfile
from cyperf.models.tls_profile import TLSProfile
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field

class PANGPSettings(BaseModel):
    """
    PANGPSettings
    """ # noqa: E501
    var_auth_settings: Optional[AuthSettings] = Field(default=None, alias="AuthSettings")
    outer_tcp_profile: Optional[TcpProfile] = Field(default=None, alias="OuterTCPProfile")
    links: Optional[List[APILink]] = None
    esp_probe_retry_timeout: Optional[StrictInt] = Field(default=None, alias="ESPProbeRetryTimeout")
    esp_probe_timeout: Optional[StrictInt] = Field(default=None, alias="ESPProbeTimeout")
    gp_client_version: Optional[StrictStr] = Field(default=None, description="GP Client Version", alias="GPClientVersion")
    is_portal: Optional[StrictBool] = Field(default=None, description="A flag indicating if the tunnel is connected to PAN Portal instead of a direct connection to the PAN GP VPN Gateway (default: true).", alias="IsPortal")
    outer_tls_client_profile: Optional[TLSProfile] = Field(default=None, alias="OuterTLSClientProfile")
    pangp_encapsulation: Optional[PANGPEncapsulation] = Field(default=None, alias="PANGPEncapsulation")
    portal_hostname: Annotated[str, Field(strict=True)] = Field(alias="PortalHostname")
    vpn_gateway: Optional[StrictStr] = Field(default=None, alias="VPNGateway")
    vpn_gateways: List[StrictStr] = Field(alias="VPNGateways")
    __properties: ClassVar[List[str]] = ["AuthSettings", "OuterTCPProfile", "links", "ESPProbeRetryTimeout", "ESPProbeTimeout", "GPClientVersion", "IsPortal", "OuterTLSClientProfile", "PANGPEncapsulation", "PortalHostname", "VPNGateway", "VPNGateways"]

    @field_validator('portal_hostname')
    def portal_hostname_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"(^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)+([A-Za-z]|[A-Za-z][A-Za-z0-9\-]*[A-Za-z0-9]))|(^$)|^((((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(([0-9a-fA-F]{1,4}:){5,5}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}|([0-9a-fA-F]{1,4}:){1,4}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){2,2}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){3,3}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){4,4})|:(:[0-9a-fA-F]{1,4}){1,5}):((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))))$", value):
            raise ValueError(r"must validate the regular expression /(^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)+([A-Za-z]|[A-Za-z][A-Za-z0-9\-]*[A-Za-z0-9]))|(^$)|^((((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(([0-9a-fA-F]{1,4}:){5,5}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}|([0-9a-fA-F]{1,4}:){1,4}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){2,2}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){3,3}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){4,4})|:(:[0-9a-fA-F]{1,4}){1,5}):((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))))$/")
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
        """Create an instance of PANGPSettings from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of var_auth_settings
        if self.var_auth_settings:
            _dict['AuthSettings'] = self.var_auth_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of outer_tcp_profile
        if self.outer_tcp_profile:
            _dict['OuterTCPProfile'] = self.outer_tcp_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # override the default output from pydantic by calling `to_dict()` of outer_tls_client_profile
        if self.outer_tls_client_profile:
            _dict['OuterTLSClientProfile'] = self.outer_tls_client_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pangp_encapsulation
        if self.pangp_encapsulation:
            _dict['PANGPEncapsulation'] = self.pangp_encapsulation.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PANGPSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "AuthSettings": AuthSettings.from_dict(obj["AuthSettings"]) if obj.get("AuthSettings") is not None else None,
                        "OuterTCPProfile": TcpProfile.from_dict(obj["OuterTCPProfile"]) if obj.get("OuterTCPProfile") is not None else None,
                        "links": [APILink.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
                        "ESPProbeRetryTimeout": obj.get("ESPProbeRetryTimeout"),
                        "ESPProbeTimeout": obj.get("ESPProbeTimeout"),
                        "GPClientVersion": obj.get("GPClientVersion"),
                        "IsPortal": obj.get("IsPortal"),
                        "OuterTLSClientProfile": TLSProfile.from_dict(obj["OuterTLSClientProfile"]) if obj.get("OuterTLSClientProfile") is not None else None,
                        "PANGPEncapsulation": PANGPEncapsulation.from_dict(obj["PANGPEncapsulation"]) if obj.get("PANGPEncapsulation") is not None else None,
                        "PortalHostname": obj.get("PortalHostname"),
                        "VPNGateway": obj.get("VPNGateway"),
                        "VPNGateways": obj.get("VPNGateways")
            ,
            "links": obj.get("links")
        })
        return _obj


