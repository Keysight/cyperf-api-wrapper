# GetNotifications200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Notification]**](Notification.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from cyperf.models.get_notifications200_response_one_of import GetNotifications200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetNotifications200ResponseOneOf from a JSON string
get_notifications200_response_one_of_instance = GetNotifications200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(GetNotifications200ResponseOneOf.to_json())

# convert the object into a dict
get_notifications200_response_one_of_dict = get_notifications200_response_one_of_instance.to_dict()
# create an instance of GetNotifications200ResponseOneOf from a dict
get_notifications200_response_one_of_from_dict = GetNotifications200ResponseOneOf.from_dict(get_notifications200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


