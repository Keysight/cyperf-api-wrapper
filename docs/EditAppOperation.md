# EditAppOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_inputs** | [**List[AddInput]**](AddInput.md) |  | [optional] 
**app_id** | **str** |  | [optional] 
**app_name** | **str** |  | [optional] 
**delete_inputs** | [**List[DeleteInput]**](DeleteInput.md) |  | [optional] 
**rename_inputs** | [**List[RenameInput]**](RenameInput.md) |  | [optional] 
**reorder_actions_inputs** | [**List[ReorderActionInput]**](ReorderActionInput.md) |  | [optional] 
**reorder_exchanges_inputs** | [**List[ReorderExchangesInput]**](ReorderExchangesInput.md) |  | [optional] 

## Example

```python
from cyperf.models.edit_app_operation import EditAppOperation

# TODO update the JSON string below
json = "{}"
# create an instance of EditAppOperation from a JSON string
edit_app_operation_instance = EditAppOperation.from_json(json)
# print the JSON string representation of the object
print(EditAppOperation.to_json())

# convert the object into a dict
edit_app_operation_dict = edit_app_operation_instance.to_dict()
# create an instance of EditAppOperation from a dict
edit_app_operation_from_dict = EditAppOperation.from_dict(edit_app_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


