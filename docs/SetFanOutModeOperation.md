# SetFanOutModeOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controllers** | [**List[FrontPanelsByController]**](FrontPanelsByController.md) | The controllers that the front panels are part of. | [optional] 
**fan_out_mode** | **str** | The desired fanOut mode. | [optional] 
**force_clear_ownership** | **bool** | Whether the ownership information of reserved ports will be cleared before switching the fanOut mode. | [optional] 

## Example

```python
from cyperf.models.set_fan_out_mode_operation import SetFanOutModeOperation

# TODO update the JSON string below
json = "{}"
# create an instance of SetFanOutModeOperation from a JSON string
set_fan_out_mode_operation_instance = SetFanOutModeOperation.from_json(json)
# print the JSON string representation of the object
print(SetFanOutModeOperation.to_json())

# convert the object into a dict
set_fan_out_mode_operation_dict = set_fan_out_mode_operation_instance.to_dict()
# create an instance of SetFanOutModeOperation from a dict
set_fan_out_mode_operation_from_dict = SetFanOutModeOperation.from_dict(set_fan_out_mode_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


