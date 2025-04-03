# Notification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerting** | **bool** | A flag indicating if the current notification should raise an alert | [optional] [readonly] 
**id** | **str** | The unique identifier of the notification | [optional] [readonly] 
**message** | **str** | A user friendly notification message | [optional] [readonly] 
**owner** | **str** | The friendly display name of the entity that created the notification | [optional] [readonly] 
**owner_id** | **str** | The unique identifier of the entity that created the notification | [optional] [readonly] 
**seen** | **bool** | A flag indicating if the current notification was already seen by an end user. Notifications that have been seen are automatically filtered. | [optional] [readonly] 
**severity** | **str** | The severity of the notification | [optional] [readonly] 
**sticky** | **bool** | A flag indicating that the current notification should not be automatically dismissed or hidden after a certain period | [optional] [readonly] 
**tags** | **Dict[str, str]** | A list of custom tags that provide additional information about the notification | [optional] [readonly] 
**timestamp** | **int** | A Unix timestamp that indicates when the notification was generated | [optional] [readonly] 

## Example

```python
from cyperf.models.notification import Notification

# TODO update the JSON string below
json = "{}"
# create an instance of Notification from a JSON string
notification_instance = Notification.from_json(json)
# print the JSON string representation of the object
print(Notification.to_json())

# convert the object into a dict
notification_dict = notification_instance.to_dict()
# create an instance of Notification from a dict
notification_from_dict = Notification.from_dict(notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


