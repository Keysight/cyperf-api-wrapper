# ActionMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_index** | **Dict[str, int]** |  | [optional] 
**flows** | [**List[AppFlow]**](AppFlow.md) |  | [optional] 
**index** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**parameters** | [**List[Parameter]**](Parameter.md) |  | [optional] 

## Example

```python
from cyperf.models.action_metadata import ActionMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ActionMetadata from a JSON string
action_metadata_instance = ActionMetadata.from_json(json)
# print the JSON string representation of the object
print(ActionMetadata.to_json())

# convert the object into a dict
action_metadata_dict = action_metadata_instance.to_dict()
# create an instance of ActionMetadata from a dict
action_metadata_from_dict = ActionMetadata.from_dict(action_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


