# ClearFrontPanelPortsOwnershipOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controllers** | [**List[FrontPanelPortsByController]**](FrontPanelPortsByController.md) | The controllers that the front panel ports are part of. | [optional] 

## Example

```python
from cyperf.models.clear_front_panel_ports_ownership_operation import ClearFrontPanelPortsOwnershipOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ClearFrontPanelPortsOwnershipOperation from a JSON string
clear_front_panel_ports_ownership_operation_instance = ClearFrontPanelPortsOwnershipOperation.from_json(json)
# print the JSON string representation of the object
print(ClearFrontPanelPortsOwnershipOperation.to_json())

# convert the object into a dict
clear_front_panel_ports_ownership_operation_dict = clear_front_panel_ports_ownership_operation_instance.to_dict()
# create an instance of ClearFrontPanelPortsOwnershipOperation from a dict
clear_front_panel_ports_ownership_operation_from_dict = ClearFrontPanelPortsOwnershipOperation.from_dict(clear_front_panel_ports_ownership_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


