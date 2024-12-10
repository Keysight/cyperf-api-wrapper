# SetAppOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | The id of the app to activate on the controllers. | [optional] 
**controllers** | **List[str]** | The controller ids for which to activate the app. | [optional] 
**force** | **bool** | Whether the ownership information will be cleared or not. | [optional] 

## Example

```python
from cyperf.models.set_app_operation import SetAppOperation

# TODO update the JSON string below
json = "{}"
# create an instance of SetAppOperation from a JSON string
set_app_operation_instance = SetAppOperation.from_json(json)
# print the JSON string representation of the object
print(SetAppOperation.to_json())

# convert the object into a dict
set_app_operation_dict = set_app_operation_instance.to_dict()
# create an instance of SetAppOperation from a dict
set_app_operation_from_dict = SetAppOperation.from_dict(set_app_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


