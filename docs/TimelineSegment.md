# TimelineSegment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **int** | The duration of the timeline segment (default: 600). | 
**id** | **str** |  | 
**segment_type** | [**SegmentType**](SegmentType.md) | The segment&#39;s type. Must be one of: SteadySegment, StepUpSegment, StepDownSegment. | 
**warm_up_period** | **int** | Deprecated. Use ObjectivesAndTimeline.WarmUp instead. The time that servers may need to warm up, when clients should wait (default: 0 seconds). | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**objective_unit** | **str** | The measurement unit for the objective value. Only applicable for Throughput objectives. | [optional] 
**objective_value** | **float** | The objective value for this timeline segment. | [optional] 
**primary_objective_unit** | **str** | Deprecated. Use PrimaryObjective.Timeline[].ObjectiveUnit instead. The primary objective unit. (default: Gbps) | 
**primary_objective_value** | **float** | Deprecated. Use PrimaryObjective.Timeline[].ObjectiveValue instead. The primary objective value (default: 1). | 
**secondary_objective_values** | [**List[ObjectiveValueEntry]**](ObjectiveValueEntry.md) | Deprecated. Use SecondaryObjective.ObjectiveValue/ObjectiveUnit instead. The secondary objectives values. | [optional] 

## Example

```python
from cyperf.models.timeline_segment import TimelineSegment

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineSegment from a JSON string
timeline_segment_instance = TimelineSegment.from_json(json)
# print the JSON string representation of the object
print(TimelineSegment.to_json())

# convert the object into a dict
timeline_segment_dict = timeline_segment_instance.to_dict()
# create an instance of TimelineSegment from a dict
timeline_segment_from_dict = TimelineSegment.from_dict(timeline_segment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


