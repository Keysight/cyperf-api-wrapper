# ChangeEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard_id** | **str** | The id of the changed dashboard | [optional] 
**session_id** | **str** | The id of the session where the change happened | [optional] 
**test_id** | **str** | The id of the test where the change happened | [optional] 

## Example

```python
from cyperf.models.change_event import ChangeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeEvent from a JSON string
change_event_instance = ChangeEvent.from_json(json)
# print the JSON string representation of the object
print(ChangeEvent.to_json())

# convert the object into a dict
change_event_dict = change_event_instance.to_dict()
# create an instance of ChangeEvent from a dict
change_event_from_dict = ChangeEvent.from_dict(change_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


