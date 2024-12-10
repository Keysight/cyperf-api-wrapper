# CreateAppOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[ActionInput]**](ActionInput.md) |  | [optional] 
**app_name** | **str** |  | [optional] 
**app_type** | **str** |  | [optional] 

## Example

```python
from cyperf.models.create_app_operation import CreateAppOperation

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAppOperation from a JSON string
create_app_operation_instance = CreateAppOperation.from_json(json)
# print the JSON string representation of the object
print(CreateAppOperation.to_json())

# convert the object into a dict
create_app_operation_dict = create_app_operation_instance.to_dict()
# create an instance of CreateAppOperation from a dict
create_app_operation_from_dict = CreateAppOperation.from_dict(create_app_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


