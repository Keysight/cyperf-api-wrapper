# RebootComputeResourcesOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controllers** | [**List[ComputeResourcesByController]**](ComputeResourcesByController.md) | The controllers that the compute resources are part of. | [optional] 

## Example

```python
from cyperf.models.reboot_compute_resources_operation import RebootComputeResourcesOperation

# TODO update the JSON string below
json = "{}"
# create an instance of RebootComputeResourcesOperation from a JSON string
reboot_compute_resources_operation_instance = RebootComputeResourcesOperation.from_json(json)
# print the JSON string representation of the object
print(RebootComputeResourcesOperation.to_json())

# convert the object into a dict
reboot_compute_resources_operation_dict = reboot_compute_resources_operation_instance.to_dict()
# create an instance of RebootComputeResourcesOperation from a dict
reboot_compute_resources_operation_from_dict = RebootComputeResourcesOperation.from_dict(reboot_compute_resources_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


