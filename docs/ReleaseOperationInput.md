# ReleaseOperationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agents_data** | [**List[AgentRelease]**](AgentRelease.md) |  | [optional] 
**session_id** | **str** |  | [optional] 

## Example

```python
from cyperf.models.release_operation_input import ReleaseOperationInput

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseOperationInput from a JSON string
release_operation_input_instance = ReleaseOperationInput.from_json(json)
# print the JSON string representation of the object
print(ReleaseOperationInput.to_json())

# convert the object into a dict
release_operation_input_dict = release_operation_input_instance.to_dict()
# create an instance of ReleaseOperationInput from a dict
release_operation_input_from_dict = ReleaseOperationInput.from_dict(release_operation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


