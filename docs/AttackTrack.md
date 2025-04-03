# AttackTrack


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[AttackAction]**](AttackAction.md) |  | [optional] 
**add_actions** | **List[bytearray]** |  | [optional] 
**id** | **str** |  | 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.attack_track import AttackTrack

# TODO update the JSON string below
json = "{}"
# create an instance of AttackTrack from a JSON string
attack_track_instance = AttackTrack.from_json(json)
# print the JSON string representation of the object
print(AttackTrack.to_json())

# convert the object into a dict
attack_track_dict = attack_track_instance.to_dict()
# create an instance of AttackTrack from a dict
attack_track_from_dict = AttackTrack.from_dict(attack_track_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


