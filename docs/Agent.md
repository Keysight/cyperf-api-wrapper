# Agent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_tags** | **List[str]** | A list of tags | [optional] 
**ip** | **str** | The management IP of the agent | [optional] [readonly] 
**interfaces** | [**List[Interface]**](Interface.md) | A list of test interfaces available on the agent | [optional] 
**last_update** | **int** | A Unix timestamp that indicates when the agent was last updated | [optional] [readonly] 
**reservation_id** | **str** | The ID of the reservation | [optional] [readonly] 
**selected_env** | [**SelectedEnv**](SelectedEnv.md) |  | [optional] 
**selection_status** | **str** | The current status of the selection operation | [optional] 
**session_name** | **str** | The session&#39;s name where the agent is running | [optional] [readonly] 
**status** | **str** | The current status of the agent | [optional] [readonly] 
**configured_proxy** | **str** | The proxy the agent is connected to | [optional] [readonly] 
**cpu_info** | [**List[AgentCPUInfo]**](AgentCPUInfo.md) | The CPU information from the agent | [optional] [readonly] 
**dpdk_enabled** | **bool** | A flag indicating whether DPDK is enabled | [optional] 
**features** | [**AgentFeatures**](AgentFeatures.md) |  | [optional] 
**hostname** | **str** | The hostname of the agent | [optional] [readonly] 
**id** | **str** | The agent&#39;s unique identifier | [optional] [readonly] 
**memory_mb** | **float** | The memory (in mega bytes) of the agent | [optional] [readonly] 
**mgmt_interface** | [**Interface**](Interface.md) |  | [optional] 
**ntp_info** | [**NtpInfo**](NtpInfo.md) |  | [optional] 
**offline** | **bool** | A flag indicating if the agent is considered online or offline | [optional] [readonly] 
**owner** | **str** | A user-friendly display name for the agent&#39;s owner | [optional] [readonly] 
**owner_id** | **str** | The unique identifier of the agent&#39;s owner | [optional] [readonly] 
**package_version_status** | **str** | A message with information about the current software version and user recommendations. | [optional] [readonly] 
**requires_updating** | **bool** | A flag indicating whether the agent is not using the recommended version | [optional] [readonly] 
**system_info** | [**SystemInfo**](SystemInfo.md) |  | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.agent import Agent

# TODO update the JSON string below
json = "{}"
# create an instance of Agent from a JSON string
agent_instance = Agent.from_json(json)
# print the JSON string representation of the object
print(Agent.to_json())

# convert the object into a dict
agent_dict = agent_instance.to_dict()
# create an instance of Agent from a dict
agent_from_dict = Agent.from_dict(agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


