# ObjectivesAndTimeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advanced_settings** | [**AdvancedSettings**](AdvancedSettings.md) |  | [optional] 
**primary_objective** | [**SpecificObjective**](SpecificObjective.md) |  | [optional] 
**secondary_objective** | [**SecondaryObjective**](SecondaryObjective.md) |  | [optional] 
**secondary_objectives** | [**List[SpecificObjective]**](SpecificObjective.md) | Deprecated. Use SecondaryObjective instead. | [optional] 
**timeline_segments** | [**List[TimelineSegment]**](TimelineSegment.md) | Deprecated. Use PrimaryObjective.Timeline instead. | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.objectives_and_timeline import ObjectivesAndTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectivesAndTimeline from a JSON string
objectives_and_timeline_instance = ObjectivesAndTimeline.from_json(json)
# print the JSON string representation of the object
print(ObjectivesAndTimeline.to_json())

# convert the object into a dict
objectives_and_timeline_dict = objectives_and_timeline_instance.to_dict()
# create an instance of ObjectivesAndTimeline from a dict
objectives_and_timeline_from_dict = ObjectivesAndTimeline.from_dict(objectives_and_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


