# SystemInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chassis_info** | [**ChassisInfo**](ChassisInfo.md) |  | [optional] 
**kernel_version** | **str** |  | [optional] [readonly] 
**os_name** | **str** |  | [optional] [readonly] 
**port_manager_version** | **str** |  | [optional] [readonly] 
**traffic_agent_info** | [**List[TrafficAgentInfo]**](TrafficAgentInfo.md) |  | [optional] [readonly] 

## Example

```python
from cyperf.models.system_info import SystemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SystemInfo from a JSON string
system_info_instance = SystemInfo.from_json(json)
# print the JSON string representation of the object
print(SystemInfo.to_json())

# convert the object into a dict
system_info_dict = system_info_instance.to_dict()
# create an instance of SystemInfo from a dict
system_info_from_dict = SystemInfo.from_dict(system_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


