# ComputeResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** | Whether the compute resource is disabled or not | [optional] 
**id** | **str** | The compute resource&#39;s unique identifier | [optional] 
**link** | **str** | The link state of the compute resource: up or down | [optional] 
**name** | **str** | A user-friendly display name for the compute resource | [optional] 
**reserved_by** | **str** | The owner of the compute resource | [optional] 
**speed** | **str** | The compute resource&#39;s speed | [optional] 
**status** | **str** | The current status of the compute resource: ready or not ready | [optional] 
**traffic_status** | **str** | The traffic status of the compute resource | [optional] 

## Example

```python
from cyperf.models.compute_resource import ComputeResource

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeResource from a JSON string
compute_resource_instance = ComputeResource.from_json(json)
# print the JSON string representation of the object
print(ComputeResource.to_json())

# convert the object into a dict
compute_resource_dict = compute_resource_instance.to_dict()
# create an instance of ComputeResource from a dict
compute_resource_from_dict = ComputeResource.from_dict(compute_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


