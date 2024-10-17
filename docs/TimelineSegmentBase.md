# TimelineSegmentBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **int** | The duration of the timeline segment (default: 600). | 
**id** | **str** |  | 
**segment_type** | [**SegmentType**](SegmentType.md) | The segment&#39;s type. Must be one of: SteadySegment, StepUpSegment, StepDownSegment. | 
**warm_up_period** | **int** | Deprecated. Use ObjectivesAndTimeline.WarmUp instead. The time that servers may need to warm up, when clients should wait (default: 0 seconds). | [optional] 

## Example

```python
from cyperf.models.timeline_segment_base import TimelineSegmentBase

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineSegmentBase from a JSON string
timeline_segment_base_instance = TimelineSegmentBase.from_json(json)
# print the JSON string representation of the object
print(TimelineSegmentBase.to_json())

# convert the object into a dict
timeline_segment_base_dict = timeline_segment_base_instance.to_dict()
# create an instance of TimelineSegmentBase from a dict
timeline_segment_base_from_dict = TimelineSegmentBase.from_dict(timeline_segment_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


