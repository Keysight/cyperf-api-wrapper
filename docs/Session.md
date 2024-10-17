# Session


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | **str** | The user-friendly name for the application that controls this session | [optional] 
**config** | [**AppsecConfig**](AppsecConfig.md) |  | [optional] 
**config_name** | **str** | The display name of the configuration loaded in the session | [optional] 
**config_url** | **str** | The external URL of the configuration loaded in the session | [optional] 
**created** | **int** | A Unix timestamp that indicates when the session was created | [optional] [readonly] 
**data_model_url** | **str** | The URL of the data model loaded in the session | [optional] [readonly] 
**id** | **str** | The unique identifier of the session | [optional] [readonly] 
**index** | **int** | The session&#39;s index | [optional] [readonly] 
**last_visited** | **int** | A Unix timestamp that indicates when the session was last visited | [optional] [readonly] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**meta** | [**List[Pair]**](Pair.md) | The session&#39;s metadata as a list of key-value pairs | [optional] 
**name** | **str** | The user-visible name of the session | [optional] 
**owner** | **str** | The user-visible name of the session&#39;s owner | [optional] [readonly] 
**owner_id** | **str** | The unique identifier of the session&#39;s owner | [optional] [readonly] 
**pinned** | **bool** | A flag that indicates if the session is pinned | [optional] 
**state** | **str** | The current state of the session | [optional] 
**test** | [**TestInfo**](TestInfo.md) |  | [optional] 

## Example

```python
from cyperf.models.session import Session

# TODO update the JSON string below
json = "{}"
# create an instance of Session from a JSON string
session_instance = Session.from_json(json)
# print the JSON string representation of the object
print(Session.to_json())

# convert the object into a dict
session_dict = session_instance.to_dict()
# create an instance of Session from a dict
session_from_dict = Session.from_dict(session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


