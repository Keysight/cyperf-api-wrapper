# AgentsGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agents** | **List[str]** | The IDs of the agents that are part of the group | [optional] [readonly] 
**available** | **bool** | Indicates whether each agent in the group is not reserved | [optional] [readonly] 
**name** | **str** | The name of the agent group | [optional] [readonly] 
**online** | **bool** | Indicates whether each agent in the group has been updated in the last 5 minutes | [optional] [readonly] 

## Example

```python
from cyperf.models.agents_group import AgentsGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AgentsGroup from a JSON string
agents_group_instance = AgentsGroup.from_json(json)
# print the JSON string representation of the object
print(AgentsGroup.to_json())

# convert the object into a dict
agents_group_dict = agents_group_instance.to_dict()
# create an instance of AgentsGroup from a dict
agents_group_from_dict = AgentsGroup.from_dict(agents_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


