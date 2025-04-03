# TrafficAgentInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [readonly] 
**version** | **str** |  | [optional] [readonly] 

## Example

```python
from cyperf.models.traffic_agent_info import TrafficAgentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TrafficAgentInfo from a JSON string
traffic_agent_info_instance = TrafficAgentInfo.from_json(json)
# print the JSON string representation of the object
print(TrafficAgentInfo.to_json())

# convert the object into a dict
traffic_agent_info_dict = traffic_agent_info_instance.to_dict()
# create an instance of TrafficAgentInfo from a dict
traffic_agent_info_from_dict = TrafficAgentInfo.from_dict(traffic_agent_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


