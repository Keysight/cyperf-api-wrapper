# GetControllerComputeNodes200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ComputeNode]**](ComputeNode.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from cyperf.models.get_controller_compute_nodes200_response import GetControllerComputeNodes200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetControllerComputeNodes200Response from a JSON string
get_controller_compute_nodes200_response_instance = GetControllerComputeNodes200Response.from_json(json)
# print the JSON string representation of the object
print(GetControllerComputeNodes200Response.to_json())

# convert the object into a dict
get_controller_compute_nodes200_response_dict = get_controller_compute_nodes200_response_instance.to_dict()
# create an instance of GetControllerComputeNodes200Response from a dict
get_controller_compute_nodes200_response_from_dict = GetControllerComputeNodes200Response.from_dict(get_controller_compute_nodes200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


