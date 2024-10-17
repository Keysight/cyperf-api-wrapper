# AgentCPUInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_core_count** | **int** |  | [optional] [readonly] 
**cpu_freq_mhz** | **float** |  | [optional] [readonly] 
**family** | **str** |  | [optional] [readonly] 
**model** | **str** |  | [optional] [readonly] 
**model_name** | **str** |  | [optional] [readonly] 
**vendor_id** | **str** |  | [optional] [readonly] 

## Example

```python
from cyperf.models.agent_cpu_info import AgentCPUInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AgentCPUInfo from a JSON string
agent_cpu_info_instance = AgentCPUInfo.from_json(json)
# print the JSON string representation of the object
print(AgentCPUInfo.to_json())

# convert the object into a dict
agent_cpu_info_dict = agent_cpu_info_instance.to_dict()
# create an instance of AgentCPUInfo from a dict
agent_cpu_info_from_dict = AgentCPUInfo.from_dict(agent_cpu_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


