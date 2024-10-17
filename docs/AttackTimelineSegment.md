# AttackTimelineSegment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **int** | The duration of the timeline segment (default: 600). | 
**id** | **str** |  | 
**segment_type** | [**SegmentType**](SegmentType.md) | The segment&#39;s type. Must be one of: SteadySegment, StepUpSegment, StepDownSegment. | 
**warm_up_period** | **int** | Deprecated. Use ObjectivesAndTimeline.WarmUp instead. The time that servers may need to warm up, when clients should wait (default: 0 seconds). | [optional] 
**attack_rate** | **int** | The attack rate of the attack (default: 1). | 
**connection_graceful_stop_timeout** | **int** | The time the test will wait all connections to be graceful stopped (default: 15 seconds). | [optional] 
**iteration_count** | **int** | The number of iterations to run (default: 1). | [optional] 
**max_concurrent_attack** | **int** | The maximum number of concurrent attacks (default: 1). | 

## Example

```python
from cyperf.models.attack_timeline_segment import AttackTimelineSegment

# TODO update the JSON string below
json = "{}"
# create an instance of AttackTimelineSegment from a JSON string
attack_timeline_segment_instance = AttackTimelineSegment.from_json(json)
# print the JSON string representation of the object
print(AttackTimelineSegment.to_json())

# convert the object into a dict
attack_timeline_segment_dict = attack_timeline_segment_instance.to_dict()
# create an instance of AttackTimelineSegment from a dict
attack_timeline_segment_from_dict = AttackTimelineSegment.from_dict(attack_timeline_segment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


