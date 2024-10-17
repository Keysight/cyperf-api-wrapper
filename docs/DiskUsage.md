# DiskUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **int** | The currently available disk space (in bytes) | [optional] [readonly] 
**consumers** | [**List[Consumer]**](Consumer.md) | A list of consumers for handling logs and diagnostics storage | [optional] 
**critical_disk_space** | **bool** | A flag indicating whether disk space is critical i.e the application may become unstable | [optional] [readonly] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**low_disk_space** | **bool** | A flag indicating whether disk space is low | [optional] [readonly] 
**message** | **str** | A user-friendly message about disk usage | [optional] [readonly] 
**pretty_available** | **str** | The currently available disk space in human-readable format | [optional] [readonly] 
**pretty_size** | **str** | The total disk size in human-readable format | [optional] [readonly] 
**size** | **int** | The total disk size (in bytes) | [optional] [readonly] 

## Example

```python
from cyperf.models.disk_usage import DiskUsage

# TODO update the JSON string below
json = "{}"
# create an instance of DiskUsage from a JSON string
disk_usage_instance = DiskUsage.from_json(json)
# print the JSON string representation of the object
print(DiskUsage.to_json())

# convert the object into a dict
disk_usage_dict = disk_usage_instance.to_dict()
# create an instance of DiskUsage from a dict
disk_usage_from_dict = DiskUsage.from_dict(disk_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


