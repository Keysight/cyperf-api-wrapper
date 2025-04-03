# DeleteInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_index_delete_at** | **int** |  | [optional] 
**exchange_delete_at** | **int** |  | [optional] 
**flow_index_delete_at** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from cyperf.models.delete_input import DeleteInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteInput from a JSON string
delete_input_instance = DeleteInput.from_json(json)
# print the JSON string representation of the object
print(DeleteInput.to_json())

# convert the object into a dict
delete_input_dict = delete_input_instance.to_dict()
# create an instance of DeleteInput from a dict
delete_input_from_dict = DeleteInput.from_dict(delete_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


