# AttackObjectivesAndTimeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeline_segments** | [**List[AttackTimelineSegment]**](AttackTimelineSegment.md) |  | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.attack_objectives_and_timeline import AttackObjectivesAndTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of AttackObjectivesAndTimeline from a JSON string
attack_objectives_and_timeline_instance = AttackObjectivesAndTimeline.from_json(json)
# print the JSON string representation of the object
print(AttackObjectivesAndTimeline.to_json())

# convert the object into a dict
attack_objectives_and_timeline_dict = attack_objectives_and_timeline_instance.to_dict()
# create an instance of AttackObjectivesAndTimeline from a dict
attack_objectives_and_timeline_from_dict = AttackObjectivesAndTimeline.from_dict(attack_objectives_and_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


