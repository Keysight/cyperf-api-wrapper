# StepSegment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **int** | The duration of the timeline segment (default: 600). | 
**id** | **str** |  | 
**segment_type** | [**SegmentType**](SegmentType.md) | The segment&#39;s type. Must be one of: SteadySegment, StepUpSegment, StepDownSegment. | 
**warm_up_period** | **int** | Deprecated. Use ObjectivesAndTimeline.WarmUp instead. The time that servers may need to warm up, when clients should wait (default: 0 seconds). | [optional] 
**enabled** | **bool** | Whether this timeline segment will be used. | 
**number_of_steps** | **int** | The number of steps to execute. The step value will be computed based on the SteadySegment with the following formula: StepObjectiveValue &#x3D; SteadySegment.ObjectiveValue / NumberOfSteps. | 

## Example

```python
from cyperf.models.step_segment import StepSegment

# TODO update the JSON string below
json = "{}"
# create an instance of StepSegment from a JSON string
step_segment_instance = StepSegment.from_json(json)
# print the JSON string representation of the object
print(StepSegment.to_json())

# convert the object into a dict
step_segment_dict = step_segment_instance.to_dict()
# create an instance of StepSegment from a dict
step_segment_from_dict = StepSegment.from_dict(step_segment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


