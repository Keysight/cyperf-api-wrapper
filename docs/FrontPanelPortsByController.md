# FrontPanelPortsByController


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controller_id** | **str** | The id of the controller that the front panel ports are part of. | [optional] 
**front_panels** | [**List[PortsByPanel]**](PortsByPanel.md) | The front panels that the ports are part of. | [optional] 

## Example

```python
from cyperf.models.front_panel_ports_by_controller import FrontPanelPortsByController

# TODO update the JSON string below
json = "{}"
# create an instance of FrontPanelPortsByController from a JSON string
front_panel_ports_by_controller_instance = FrontPanelPortsByController.from_json(json)
# print the JSON string representation of the object
print(FrontPanelPortsByController.to_json())

# convert the object into a dict
front_panel_ports_by_controller_dict = front_panel_ports_by_controller_instance.to_dict()
# create an instance of FrontPanelPortsByController from a dict
front_panel_ports_by_controller_from_dict = FrontPanelPortsByController.from_dict(front_panel_ports_by_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


