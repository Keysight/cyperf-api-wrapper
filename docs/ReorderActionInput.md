# ReorderActionInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_idx** | **int** |  | [optional] 
**action_name** | **str** |  | [optional] 

## Example

```python
from cyperf.models.reorder_action_input import ReorderActionInput

# TODO update the JSON string below
json = "{}"
# create an instance of ReorderActionInput from a JSON string
reorder_action_input_instance = ReorderActionInput.from_json(json)
# print the JSON string representation of the object
print(ReorderActionInput.to_json())

# convert the object into a dict
reorder_action_input_dict = reorder_action_input_instance.to_dict()
# create an instance of ReorderActionInput from a dict
reorder_action_input_from_dict = ReorderActionInput.from_dict(reorder_action_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


