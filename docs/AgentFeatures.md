# AgentFeatures


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**debian_os** | **str** | A flag indicating whether the operating system is Debian-based | [optional] [readonly] 
**dpdk_usage** | **str** | A flag indicating whether DPDK usage is supported | [optional] [readonly] 
**update** | **str** | A flag indicating if update operation is supported | [optional] [readonly] 

## Example

```python
from cyperf.models.agent_features import AgentFeatures

# TODO update the JSON string below
json = "{}"
# create an instance of AgentFeatures from a JSON string
agent_features_instance = AgentFeatures.from_json(json)
# print the JSON string representation of the object
print(AgentFeatures.to_json())

# convert the object into a dict
agent_features_dict = agent_features_instance.to_dict()
# create an instance of AgentFeatures from a dict
agent_features_from_dict = AgentFeatures.from_dict(agent_features_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


