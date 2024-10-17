# ExpectedDiskSpacePrettySize


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**per_minute** | **str** | Total expected disk size per agent per minute in human-readable form | 
**per_second** | **str** | Total expected disk size per agent per second in human-readable form | 
**total** | **str** | Total expected disk size per agent in human-readable form | 

## Example

```python
from cyperf.models.expected_disk_space_pretty_size import ExpectedDiskSpacePrettySize

# TODO update the JSON string below
json = "{}"
# create an instance of ExpectedDiskSpacePrettySize from a JSON string
expected_disk_space_pretty_size_instance = ExpectedDiskSpacePrettySize.from_json(json)
# print the JSON string representation of the object
print(ExpectedDiskSpacePrettySize.to_json())

# convert the object into a dict
expected_disk_space_pretty_size_dict = expected_disk_space_pretty_size_instance.to_dict()
# create an instance of ExpectedDiskSpacePrettySize from a dict
expected_disk_space_pretty_size_from_dict = ExpectedDiskSpacePrettySize.from_dict(expected_disk_space_pretty_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


