# ActionBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dst_host** | **str** | The destination host of the action. | [optional] 
**exchanges** | [**List[Exchange]**](Exchange.md) |  | [optional] 
**id** | **str** |  | [optional] 
**index** | **int** | The index of the action. | [optional] 
**is_banner** | **bool** | Indicates if this is a required action, can only be add once and also must be the first | [optional] 
**is_deprecated** | **bool** | A value that indicates if the action is deprecated. | [optional] 
**is_hostname** | **int** |  | [optional] 
**is_strike** | **bool** | A value that indicates if the action is a strike. | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**name** | **str** | The name of the action. | [optional] 
**params** | [**List[Params]**](Params.md) |  | [optional] 
**port** | **int** | The port of the destination host. | [optional] 
**protocol_id** | **str** |  | [optional] 
**requires_uniqueness** | **bool** | If true, for applications with the same protocol id, application/attack must have been uniquely identified in previous commands. | [optional] 

## Example

```python
from cyperf.models.action_base import ActionBase

# TODO update the JSON string below
json = "{}"
# create an instance of ActionBase from a JSON string
action_base_instance = ActionBase.from_json(json)
# print the JSON string representation of the object
print(ActionBase.to_json())

# convert the object into a dict
action_base_dict = action_base_instance.to_dict()
# create an instance of ActionBase from a dict
action_base_from_dict = ActionBase.from_dict(action_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


