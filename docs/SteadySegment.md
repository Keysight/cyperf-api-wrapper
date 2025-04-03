# SteadySegment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **int** | The duration of the timeline segment (default: 600). | 
**segment_type** | [**SegmentType**](SegmentType.md) | The segment&#39;s type. Must be one of: SteadySegment, StepUpSegment, StepDownSegment. | 
**warm_up_period** | **int** | Deprecated. Use ObjectivesAndTimeline.WarmUp instead. The time that servers may need to warm up, when clients should wait (default: 0 seconds). | [optional] 
**id** | **str** |  | 
**objective_unit** | **str** |  | 
**objective_value** | **float** |  | 

## Example

```python
from cyperf.models.steady_segment import SteadySegment

# TODO update the JSON string below
json = "{}"
# create an instance of SteadySegment from a JSON string
steady_segment_instance = SteadySegment.from_json(json)
# print the JSON string representation of the object
print(SteadySegment.to_json())

# convert the object into a dict
steady_segment_dict = steady_segment_instance.to_dict()
# create an instance of SteadySegment from a dict
steady_segment_from_dict = SteadySegment.from_dict(steady_segment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


