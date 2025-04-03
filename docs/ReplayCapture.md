# ReplayCapture


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flows** | [**List[AppFlow]**](AppFlow.md) | The list of flows | [optional] 
**id** | **str** | The unique identifier of the application | [optional] [readonly] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**name** | **str** |  | [optional] 
**owner** | **str** | The user-visible name of the file&#39;s owner | [optional] [readonly] 
**owner_id** | **str** | The unique identifier of the file&#39;s owner | [optional] [readonly] 

## Example

```python
from cyperf.models.replay_capture import ReplayCapture

# TODO update the JSON string below
json = "{}"
# create an instance of ReplayCapture from a JSON string
replay_capture_instance = ReplayCapture.from_json(json)
# print the JSON string representation of the object
print(ReplayCapture.to_json())

# convert the object into a dict
replay_capture_dict = replay_capture_instance.to_dict()
# create an instance of ReplayCapture from a dict
replay_capture_from_dict = ReplayCapture.from_dict(replay_capture_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


