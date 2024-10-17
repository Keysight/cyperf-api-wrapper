# ExpectedDiskSpaceMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**per_minute** | **str** | User friendly message with the expected disk size per agent per minute | 
**per_second** | **str** | User friendly message with the expected disk size per agent per second | 
**total** | **str** | User friendly message with the total expected disk size per agent | 

## Example

```python
from cyperf.models.expected_disk_space_message import ExpectedDiskSpaceMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ExpectedDiskSpaceMessage from a JSON string
expected_disk_space_message_instance = ExpectedDiskSpaceMessage.from_json(json)
# print the JSON string representation of the object
print(ExpectedDiskSpaceMessage.to_json())

# convert the object into a dict
expected_disk_space_message_dict = expected_disk_space_message_instance.to_dict()
# create an instance of ExpectedDiskSpaceMessage from a dict
expected_disk_space_message_from_dict = ExpectedDiskSpaceMessage.from_dict(expected_disk_space_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


