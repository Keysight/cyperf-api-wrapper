# AddInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_index** | **int** |  | [optional] 
**action_name** | **str** |  | [optional] 
**captures** | [**List[Capture]**](Capture.md) |  | [optional] 
**exchange_index_insert_at** | **int** |  | [optional] 
**flow_index_insert_at** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from cyperf.models.add_input import AddInput

# TODO update the JSON string below
json = "{}"
# create an instance of AddInput from a JSON string
add_input_instance = AddInput.from_json(json)
# print the JSON string representation of the object
print(AddInput.to_json())

# convert the object into a dict
add_input_dict = add_input_instance.to_dict()
# create an instance of AddInput from a dict
add_input_from_dict = AddInput.from_dict(add_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


