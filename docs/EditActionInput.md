# EditActionInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_index** | **int** |  | [optional] 
**parameters** | [**List[Parameter]**](Parameter.md) |  | [optional] 

## Example

```python
from cyperf.models.edit_action_input import EditActionInput

# TODO update the JSON string below
json = "{}"
# create an instance of EditActionInput from a JSON string
edit_action_input_instance = EditActionInput.from_json(json)
# print the JSON string representation of the object
print(EditActionInput.to_json())

# convert the object into a dict
edit_action_input_dict = edit_action_input_instance.to_dict()
# create an instance of EditActionInput from a dict
edit_action_input_from_dict = EditActionInput.from_dict(edit_action_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


