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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from cyperf.models.agent_cpu_info import AgentCPUInfo
from cyperf.models.agent_features import AgentFeatures
from cyperf.models.api_link import APILink
from cyperf.models.interface import Interface
from cyperf.models.ntp_info import NtpInfo
from cyperf.models.selected_env import SelectedEnv
from cyperf.models.system_info import SystemInfo
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field

class Agent(BaseModel):
    """
    Agent
    """ # noqa: E501
    agent_tags: Optional[List[StrictStr]] = Field(default=None, description="A list of tags", alias="AgentTags")
    ip: Optional[StrictStr] = Field(default=None, description="The management IP of the agent", alias="IP")
    interfaces: Optional[List[Interface]] = Field(default=None, description="A list of test interfaces available on the agent", alias="Interfaces")
    last_update: Optional[StrictInt] = Field(default=None, description="A Unix timestamp that indicates when the agent was last updated", alias="LastUpdate")
    reservation_id: Optional[StrictStr] = Field(default=None, description="The ID of the reservation", alias="ReservationID")
    selected_env: Optional[SelectedEnv] = Field(default=None, alias="SelectedEnv")
    selection_status: Optional[StrictStr] = Field(default=None, description="The current status of the selection operation", alias="SelectionStatus")
    session_name: Optional[StrictStr] = Field(default=None, description="The session's name where the agent is running", alias="SessionName")
    status: Optional[StrictStr] = Field(default=None, description="The current status of the agent", alias="Status")
    configured_proxy: Optional[StrictStr] = Field(default=None, description="The proxy the agent is connected to", alias="configuredProxy")
    cpu_info: Optional[List[AgentCPUInfo]] = Field(default=None, description="The CPU information from the agent", alias="cpuInfo")
    dpdk_enabled: Optional[StrictBool] = Field(default=None, description="A flag indicating whether DPDK is enabled", alias="dpdkEnabled")
    features: Optional[AgentFeatures] = None
    hostname: Optional[StrictStr] = Field(default=None, description="The hostname of the agent")
    id: Optional[StrictStr] = Field(default=None, description="The agent's unique identifier")
    memory_mb: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The memory (in mega bytes) of the agent", alias="memoryMB")
    mgmt_interface: Optional[Interface] = Field(default=None, alias="mgmtInterface")
    ntp_info: Optional[NtpInfo] = Field(default=None, alias="ntpInfo")
    offline: Optional[StrictBool] = Field(default=None, description="A flag indicating if the agent is considered online or offline")
    owner: Optional[StrictStr] = Field(default=None, description="A user-friendly display name for the agent's owner")
    owner_id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the agent's owner", alias="ownerId")
    package_version_status: Optional[StrictStr] = Field(default=None, description="A message with information about the current software version and user recommendations.", alias="packageVersionStatus")
    requires_updating: Optional[StrictBool] = Field(default=None, description="A flag indicating whether the agent is not using the recommended version", alias="requiresUpdating")
    system_info: Optional[SystemInfo] = Field(default=None, alias="systemInfo")
    links: Optional[List[APILink]] = None
    __properties: ClassVar[List[str]] = ["AgentTags", "IP", "Interfaces", "LastUpdate", "ReservationID", "SelectedEnv", "SelectionStatus", "SessionName", "Status", "configuredProxy", "cpuInfo", "dpdkEnabled", "features", "hostname", "id", "memoryMB", "mgmtInterface", "ntpInfo", "offline", "owner", "ownerId", "packageVersionStatus", "requiresUpdating", "systemInfo", "links"]

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
        """Create an instance of Agent from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "ip",
            "last_update",
            "reservation_id",
            "session_name",
            "status",
            "configured_proxy",
            "cpu_info",
            "hostname",
            "id",
            "memory_mb",
            "offline",
            "owner",
            "owner_id",
            "package_version_status",
            "requires_updating",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in interfaces (list)
        _items = []
        if self.interfaces:
            for _item in self.interfaces:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Interfaces'] = _items
        # override the default output from pydantic by calling `to_dict()` of selected_env
        if self.selected_env:
            _dict['SelectedEnv'] = self.selected_env.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in cpu_info (list)
        _items = []
        if self.cpu_info:
            for _item in self.cpu_info:
                if _item:
                    _items.append(_item.to_dict())
            _dict['cpuInfo'] = _items
        # override the default output from pydantic by calling `to_dict()` of features
        if self.features:
            _dict['features'] = self.features.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mgmt_interface
        if self.mgmt_interface:
            _dict['mgmtInterface'] = self.mgmt_interface.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ntp_info
        if self.ntp_info:
            _dict['ntpInfo'] = self.ntp_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of system_info
        if self.system_info:
            _dict['systemInfo'] = self.system_info.to_dict()
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
        """Create an instance of Agent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "AgentTags": obj.get("AgentTags"),
                        "IP": obj.get("IP"),
                        "Interfaces": [Interface.from_dict(_item) for _item in obj["Interfaces"]] if obj.get("Interfaces") is not None else None,
                        "LastUpdate": obj.get("LastUpdate"),
                        "ReservationID": obj.get("ReservationID"),
                        "SelectedEnv": SelectedEnv.from_dict(obj["SelectedEnv"]) if obj.get("SelectedEnv") is not None else None,
                        "SelectionStatus": obj.get("SelectionStatus"),
                        "SessionName": obj.get("SessionName"),
                        "Status": obj.get("Status"),
                        "configuredProxy": obj.get("configuredProxy"),
                        "cpuInfo": [AgentCPUInfo.from_dict(_item) for _item in obj["cpuInfo"]] if obj.get("cpuInfo") is not None else None,
                        "dpdkEnabled": obj.get("dpdkEnabled"),
                        "features": AgentFeatures.from_dict(obj["features"]) if obj.get("features") is not None else None,
                        "hostname": obj.get("hostname"),
                        "id": obj.get("id"),
                        "memoryMB": obj.get("memoryMB"),
                        "mgmtInterface": Interface.from_dict(obj["mgmtInterface"]) if obj.get("mgmtInterface") is not None else None,
                        "ntpInfo": NtpInfo.from_dict(obj["ntpInfo"]) if obj.get("ntpInfo") is not None else None,
                        "offline": obj.get("offline"),
                        "owner": obj.get("owner"),
                        "ownerId": obj.get("ownerId"),
                        "packageVersionStatus": obj.get("packageVersionStatus"),
                        "requiresUpdating": obj.get("requiresUpdating"),
                        "systemInfo": SystemInfo.from_dict(obj["systemInfo"]) if obj.get("systemInfo") is not None else None,
                        "links": [APILink.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None
            ,
            "links": obj.get("links")
        })
        return _obj


