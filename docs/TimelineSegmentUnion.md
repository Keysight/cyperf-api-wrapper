# TimelineSegmentUnion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **int** | The duration of the timeline segment (default: 600). | 
**segment_type** | [**SegmentType**](SegmentType.md) | The segment&#39;s type. Must be one of: SteadySegment, StepUpSegment, StepDownSegment. | 
**warm_up_period** | **int** | Deprecated. Use ObjectivesAndTimeline.WarmUp instead. The time that servers may need to warm up, when clients should wait (default: 0 seconds). | [optional] 
**id** | **str** |  | 
**objective_unit** | **str** |  | 
**objective_value** | **float** |  | 
**enabled** | **bool** | Whether this timeline segment will be used. | 
**number_of_steps** | **int** | The number of steps to execute. The step value will be computed based on the SteadySegment with the following formula: StepObjectiveValue &#x3D; SteadySegment.ObjectiveValue / NumberOfSteps. | 

## Example

```python
from cyperf.models.timeline_segment_union import TimelineSegmentUnion

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineSegmentUnion from a JSON string
timeline_segment_union_instance = TimelineSegmentUnion.from_json(json)
# print the JSON string representation of the object
print(TimelineSegmentUnion.to_json())

# convert the object into a dict
timeline_segment_union_dict = timeline_segment_union_instance.to_dict()
# create an instance of TimelineSegmentUnion from a dict
timeline_segment_union_from_dict = TimelineSegmentUnion.from_dict(timeline_segment_union_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


