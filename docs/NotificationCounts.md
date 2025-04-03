# NotificationCounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all** | **int** | The number of notifications, regardless of their type | [optional] [readonly] 
**error** | **int** | The number of error notifications | [optional] [readonly] 
**info** | **int** | The number of informational messages | [optional] [readonly] 
**warning** | **int** | The number of warnings | [optional] [readonly] 

## Example

```python
from cyperf.models.notification_counts import NotificationCounts

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationCounts from a JSON string
notification_counts_instance = NotificationCounts.from_json(json)
# print the JSON string representation of the object
print(NotificationCounts.to_json())

# convert the object into a dict
notification_counts_dict = notification_counts_instance.to_dict()
# create an instance of NotificationCounts from a dict
notification_counts_from_dict = NotificationCounts.from_dict(notification_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


