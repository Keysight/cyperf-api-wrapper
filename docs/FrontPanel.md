# FrontPanel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fan_out_mode** | **str** | The current fanOut mode of the front panel | [optional] 
**health_details** | [**List[HealthIssue]**](HealthIssue.md) | A list with more details regarding the health of the front panel | [optional] 
**healthy** | **bool** | Whether the front panel has any health issue or not | [optional] 
**id** | **str** | The unique identifier of the front panel | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**name** | **str** | A user-friendly display name for the front panel | [optional] 
**ports** | [**List[Port]**](Port.md) | The front panel ports of the front panel | [optional] 
**status** | **str** | The current status of the front panel: ready or not ready | [optional] 

## Example

```python
from cyperf.models.front_panel import FrontPanel

# TODO update the JSON string below
json = "{}"
# create an instance of FrontPanel from a JSON string
front_panel_instance = FrontPanel.from_json(json)
# print the JSON string representation of the object
print(FrontPanel.to_json())

# convert the object into a dict
front_panel_dict = front_panel_instance.to_dict()
# create an instance of FrontPanel from a dict
front_panel_from_dict = FrontPanel.from_dict(front_panel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


