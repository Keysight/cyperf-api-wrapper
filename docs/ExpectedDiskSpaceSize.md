# ExpectedDiskSpaceSize


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**per_minute** | **int** | Expected disk size that will be used by the current configuration per agent per minute | 
**per_second** | **int** | Expected disk size that will be used by the current configuration per agent per second | 
**total** | **int** | Total expected disk size that will be used by the current configuration per agent | 

## Example

```python
from cyperf.models.expected_disk_space_size import ExpectedDiskSpaceSize

# TODO update the JSON string below
json = "{}"
# create an instance of ExpectedDiskSpaceSize from a JSON string
expected_disk_space_size_instance = ExpectedDiskSpaceSize.from_json(json)
# print the JSON string representation of the object
print(ExpectedDiskSpaceSize.to_json())

# convert the object into a dict
expected_disk_space_size_dict = expected_disk_space_size_instance.to_dict()
# create an instance of ExpectedDiskSpaceSize from a dict
expected_disk_space_size_from_dict = ExpectedDiskSpaceSize.from_dict(expected_disk_space_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


