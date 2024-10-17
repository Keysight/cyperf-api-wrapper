# ExpectedDiskSpace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | [**ExpectedDiskSpaceMessage**](ExpectedDiskSpaceMessage.md) |  | 
**pretty_size** | [**ExpectedDiskSpacePrettySize**](ExpectedDiskSpacePrettySize.md) |  | 
**size** | [**ExpectedDiskSpaceSize**](ExpectedDiskSpaceSize.md) |  | 

## Example

```python
from cyperf.models.expected_disk_space import ExpectedDiskSpace

# TODO update the JSON string below
json = "{}"
# create an instance of ExpectedDiskSpace from a JSON string
expected_disk_space_instance = ExpectedDiskSpace.from_json(json)
# print the JSON string representation of the object
print(ExpectedDiskSpace.to_json())

# convert the object into a dict
expected_disk_space_dict = expected_disk_space_instance.to_dict()
# create an instance of ExpectedDiskSpace from a dict
expected_disk_space_from_dict = ExpectedDiskSpace.from_dict(expected_disk_space_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


