# ComputeResourcesByNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compute_node_id** | **str** | The id of the compute node that the compute resources are part of. | [optional] 
**compute_resources** | **List[str]** | The compute resource ids. | [optional] 

## Example

```python
from cyperf.models.compute_resources_by_node import ComputeResourcesByNode

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeResourcesByNode from a JSON string
compute_resources_by_node_instance = ComputeResourcesByNode.from_json(json)
# print the JSON string representation of the object
print(ComputeResourcesByNode.to_json())

# convert the object into a dict
compute_resources_by_node_dict = compute_resources_by_node_instance.to_dict()
# create an instance of ComputeResourcesByNode from a dict
compute_resources_by_node_from_dict = ComputeResourcesByNode.from_dict(compute_resources_by_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


