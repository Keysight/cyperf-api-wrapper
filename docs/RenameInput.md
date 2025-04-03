# RenameInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_action_name** | **str** |  | [optional] 
**old_action_name** | **str** |  | [optional] 

## Example

```python
from cyperf.models.rename_input import RenameInput

# TODO update the JSON string below
json = "{}"
# create an instance of RenameInput from a JSON string
rename_input_instance = RenameInput.from_json(json)
# print the JSON string representation of the object
print(RenameInput.to_json())

# convert the object into a dict
rename_input_dict = rename_input_instance.to_dict()
# create an instance of RenameInput from a dict
rename_input_from_dict = RenameInput.from_dict(rename_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


