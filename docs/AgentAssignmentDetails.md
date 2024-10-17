# AgentAssignmentDetails

Details of an agent assignment by ID

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** | The id of the agent that is assigned. | 
**capture_settings** | [**CaptureSettings**](CaptureSettings.md) | The capture settings of the agent that is assigned. | [optional] 
**id** | **str** |  | 
**interfaces** | **List[str]** | The names of the assigned test interfaces for the agent. | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.agent_assignment_details import AgentAssignmentDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AgentAssignmentDetails from a JSON string
agent_assignment_details_instance = AgentAssignmentDetails.from_json(json)
# print the JSON string representation of the object
print(AgentAssignmentDetails.to_json())

# convert the object into a dict
agent_assignment_details_dict = agent_assignment_details_instance.to_dict()
# create an instance of AgentAssignmentDetails from a dict
agent_assignment_details_from_dict = AgentAssignmentDetails.from_dict(agent_assignment_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


