# SwitchAppOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | The id of the app to activate on the controller. | [optional] 

## Example

```python
from cyperf.models.switch_app_operation import SwitchAppOperation

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchAppOperation from a JSON string
switch_app_operation_instance = SwitchAppOperation.from_json(json)
# print the JSON string representation of the object
print(SwitchAppOperation.to_json())

# convert the object into a dict
switch_app_operation_dict = switch_app_operation_instance.to_dict()
# create an instance of SwitchAppOperation from a dict
switch_app_operation_from_dict = SwitchAppOperation.from_dict(switch_app_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


