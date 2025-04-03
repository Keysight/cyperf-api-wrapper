# SelectedEnv


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** |  | [optional] [readonly] 
**test_interface** | [**List[Interface]**](Interface.md) |  | [optional] [readonly] 
**token** | **str** |  | [optional] [readonly] 

## Example

```python
from cyperf.models.selected_env import SelectedEnv

# TODO update the JSON string below
json = "{}"
# create an instance of SelectedEnv from a JSON string
selected_env_instance = SelectedEnv.from_json(json)
# print the JSON string representation of the object
print(SelectedEnv.to_json())

# convert the object into a dict
selected_env_dict = selected_env_instance.to_dict()
# create an instance of SelectedEnv from a dict
selected_env_from_dict = SelectedEnv.from_dict(selected_env_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


