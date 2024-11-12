# AttackAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dst_host** | **str** | The destination host of the action. | [optional] 
**exchanges** | [**List[Exchange]**](Exchange.md) |  | [optional] 
**index** | **int** | The index of the action. | [optional] 
**is_banner** | **bool** | Indicates if this is a required action, can only be add once and also must be the first | [optional] 
**is_deprecated** | **bool** | A value that indicates if the action is deprecated. | [optional] 
**is_hostname** | **int** |  | [optional] 
**is_strike** | **bool** | A value that indicates if the action is a strike. | [optional] 
**name** | **str** | The name of the action. | [optional] 
**params** | [**List[Params]**](Params.md) |  | [optional] 
**port** | **int** | The port of the destination host. | [optional] 
**protocol_id** | **str** |  | [optional] 
**requires_uniqueness** | **bool** | If true, for applications with the same protocol id, application/attack must have been uniquely identified in previous commands. | [optional] 
**id** | **str** |  | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.attack_action import AttackAction

# TODO update the JSON string below
json = "{}"
# create an instance of AttackAction from a JSON string
attack_action_instance = AttackAction.from_json(json)
# print the JSON string representation of the object
print(AttackAction.to_json())

# convert the object into a dict
attack_action_dict = attack_action_instance.to_dict()
# create an instance of AttackAction from a dict
attack_action_from_dict = AttackAction.from_dict(attack_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


