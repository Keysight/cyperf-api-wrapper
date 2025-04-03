# AppMode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | The unique identifier of the active app | [optional] 
**ui_app_id** | **str** | A user-friendly display name of the active app | [optional] 

## Example

```python
from cyperf.models.app_mode import AppMode

# TODO update the JSON string below
json = "{}"
# create an instance of AppMode from a JSON string
app_mode_instance = AppMode.from_json(json)
# print the JSON string representation of the object
print(AppMode.to_json())

# convert the object into a dict
app_mode_dict = app_mode_instance.to_dict()
# create an instance of AppMode from a dict
app_mode_from_dict = AppMode.from_dict(app_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


