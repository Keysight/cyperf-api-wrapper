# ComputeNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregated_mode** | **bool** | Whether the ports of the compute node are aggregated or not | [optional] 
**app_mode** | [**AppMode**](AppMode.md) |  | [optional] 
**health_details** | [**List[HealthIssue]**](HealthIssue.md) | A list with more details regarding the health of the compute node | [optional] 
**healthy** | **bool** | Whether the compute node has any health issue or not | [optional] 
**id** | **str** | The unique identifier of the compute node | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**name** | **str** | A user-friendly display name for the compute node | [optional] 
**ports** | [**List[Port]**](Port.md) | The ports of the compute node | [optional] 
**serial** | **str** | The serial of the compute node | [optional] 
**slot_number** | **int** | The slot number of the compute node | [optional] 
**status** | **str** | The current status of the compute node: ready or not ready | [optional] 
**type** | **str** | The type of the compute node | [optional] 

## Example

```python
from cyperf.models.compute_node import ComputeNode

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeNode from a JSON string
compute_node_instance = ComputeNode.from_json(json)
# print the JSON string representation of the object
print(ComputeNode.to_json())

# convert the object into a dict
compute_node_dict = compute_node_instance.to_dict()
# create an instance of ComputeNode from a dict
compute_node_from_dict = ComputeNode.from_dict(compute_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


