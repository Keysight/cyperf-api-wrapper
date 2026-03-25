# SetControllerAppOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | The id of the app to activate on the controllers. | [optional] 
**controllers** | **List[str]** | The controller ids for which to activate the app. | [optional] 
**force** | **bool** | Whether the ownership information will be cleared or not. | [optional] 

## Example

```python
from cyperf.models.set_controller_app_operation import SetControllerAppOperation

# TODO update the JSON string below
json = "{}"
# create an instance of SetControllerAppOperation from a JSON string
set_controller_app_operation_instance = SetControllerAppOperation.from_json(json)
# print the JSON string representation of the object
print(SetControllerAppOperation.to_json())

# convert the object into a dict
set_controller_app_operation_dict = set_controller_app_operation_instance.to_dict()
# create an instance of SetControllerAppOperation from a dict
set_controller_app_operation_from_dict = SetControllerAppOperation.from_dict(set_controller_app_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


