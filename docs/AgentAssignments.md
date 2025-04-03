# AgentAssignments

The agents assigned to the current test configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**by_id** | [**List[AgentAssignmentDetails]**](AgentAssignmentDetails.md) | The agents statically assigned to the current test configuration. | [optional] 
**by_port** | [**List[AgentAssignmentByPort]**](AgentAssignmentByPort.md) | The ports assigned to the current test configuration. | [optional] 
**by_tag** | **List[str]** | The tags according to which the agents are dynamically assigned. | 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.agent_assignments import AgentAssignments

# TODO update the JSON string below
json = "{}"
# create an instance of AgentAssignments from a JSON string
agent_assignments_instance = AgentAssignments.from_json(json)
# print the JSON string representation of the object
print(AgentAssignments.to_json())

# convert the object into a dict
agent_assignments_dict = agent_assignments_instance.to_dict()
# create an instance of AgentAssignments from a dict
agent_assignments_from_dict = AgentAssignments.from_dict(agent_assignments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


