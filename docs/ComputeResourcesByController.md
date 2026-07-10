# ComputeResourcesByController


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compute_nodes** | [**List[ComputeResourcesByNode]**](ComputeResourcesByNode.md) | The compute nodes that the compute resources are part of. | [optional] 
**controller_id** | **str** | The id of the controller that the compute resources are part of. | [optional] 

## Example

```python
from cyperf.models.compute_resources_by_controller import ComputeResourcesByController

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeResourcesByController from a JSON string
compute_resources_by_controller_instance = ComputeResourcesByController.from_json(json)
# print the JSON string representation of the object
print(ComputeResourcesByController.to_json())

# convert the object into a dict
compute_resources_by_controller_dict = compute_resources_by_controller_instance.to_dict()
# create an instance of ComputeResourcesByController from a dict
compute_resources_by_controller_from_dict = ComputeResourcesByController.from_dict(compute_resources_by_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


