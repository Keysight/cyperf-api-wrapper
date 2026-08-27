# GetComputeNodeComputeResources200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ComputeResource]**](ComputeResource.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from cyperf.models.get_compute_node_compute_resources200_response import GetComputeNodeComputeResources200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetComputeNodeComputeResources200Response from a JSON string
get_compute_node_compute_resources200_response_instance = GetComputeNodeComputeResources200Response.from_json(json)
# print the JSON string representation of the object
print(GetComputeNodeComputeResources200Response.to_json())

# convert the object into a dict
get_compute_node_compute_resources200_response_dict = get_compute_node_compute_resources200_response_instance.to_dict()
# create an instance of GetComputeNodeComputeResources200Response from a dict
get_compute_node_compute_resources200_response_from_dict = GetComputeNodeComputeResources200Response.from_dict(get_compute_node_compute_resources200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


