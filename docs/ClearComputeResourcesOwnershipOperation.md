# ClearComputeResourcesOwnershipOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controllers** | [**List[ComputeResourcesByController]**](ComputeResourcesByController.md) | The controllers that the compute resources are part of. | [optional] 

## Example

```python
from cyperf.models.clear_compute_resources_ownership_operation import ClearComputeResourcesOwnershipOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ClearComputeResourcesOwnershipOperation from a JSON string
clear_compute_resources_ownership_operation_instance = ClearComputeResourcesOwnershipOperation.from_json(json)
# print the JSON string representation of the object
print(ClearComputeResourcesOwnershipOperation.to_json())

# convert the object into a dict
clear_compute_resources_ownership_operation_dict = clear_compute_resources_ownership_operation_instance.to_dict()
# create an instance of ClearComputeResourcesOwnershipOperation from a dict
clear_compute_resources_ownership_operation_from_dict = ClearComputeResourcesOwnershipOperation.from_dict(clear_compute_resources_ownership_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


