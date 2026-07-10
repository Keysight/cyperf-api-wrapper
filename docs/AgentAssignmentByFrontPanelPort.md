# AgentAssignmentByFrontPanelPort

Details of an agent assignment by front panel port

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capture_settings** | [**CaptureSettings**](CaptureSettings.md) | The capture settings of the front panel port that is assigned. | [optional] 
**compute_resources_by_type** | **Dict[str, int]** | The number of compute resources to assign per compute node type. | [optional] 
**front_panel_port_id** | **str** | The id of the front panel port that is assigned. | 
**id** | **str** |  | 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.agent_assignment_by_front_panel_port import AgentAssignmentByFrontPanelPort

# TODO update the JSON string below
json = "{}"
# create an instance of AgentAssignmentByFrontPanelPort from a JSON string
agent_assignment_by_front_panel_port_instance = AgentAssignmentByFrontPanelPort.from_json(json)
# print the JSON string representation of the object
print(AgentAssignmentByFrontPanelPort.to_json())

# convert the object into a dict
agent_assignment_by_front_panel_port_dict = agent_assignment_by_front_panel_port_instance.to_dict()
# create an instance of AgentAssignmentByFrontPanelPort from a dict
agent_assignment_by_front_panel_port_from_dict = AgentAssignmentByFrontPanelPort.from_dict(agent_assignment_by_front_panel_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


