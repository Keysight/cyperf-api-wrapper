# SetFrontPanelPortsLinkStateOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controllers** | [**List[FrontPanelPortsByController]**](FrontPanelPortsByController.md) | The controllers that the front panel ports are part of. | [optional] 
**link** | **str** | The desired link state. | [optional] 

## Example

```python
from cyperf.models.set_front_panel_ports_link_state_operation import SetFrontPanelPortsLinkStateOperation

# TODO update the JSON string below
json = "{}"
# create an instance of SetFrontPanelPortsLinkStateOperation from a JSON string
set_front_panel_ports_link_state_operation_instance = SetFrontPanelPortsLinkStateOperation.from_json(json)
# print the JSON string representation of the object
print(SetFrontPanelPortsLinkStateOperation.to_json())

# convert the object into a dict
set_front_panel_ports_link_state_operation_dict = set_front_panel_ports_link_state_operation_instance.to_dict()
# create an instance of SetFrontPanelPortsLinkStateOperation from a dict
set_front_panel_ports_link_state_operation_from_dict = SetFrontPanelPortsLinkStateOperation.from_dict(set_front_panel_ports_link_state_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


