# AgentAssignmentByPort

Details of an agent assignment by port

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capture_settings** | [**CaptureSettings**](CaptureSettings.md) | The capture settings of the port that is assigned. | [optional] 
**id** | **str** |  | 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**port_id** | **str** | The id of the port that is assigned. | [optional] 

## Example

```python
from cyperf.models.agent_assignment_by_port import AgentAssignmentByPort

# TODO update the JSON string below
json = "{}"
# create an instance of AgentAssignmentByPort from a JSON string
agent_assignment_by_port_instance = AgentAssignmentByPort.from_json(json)
# print the JSON string representation of the object
print(AgentAssignmentByPort.to_json())

# convert the object into a dict
agent_assignment_by_port_dict = agent_assignment_by_port_instance.to_dict()
# create an instance of AgentAssignmentByPort from a dict
agent_assignment_by_port_from_dict = AgentAssignmentByPort.from_dict(agent_assignment_by_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


