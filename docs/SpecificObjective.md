# SpecificObjective


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**max_pending_simulated_users** | **str** | Only applies if Type is SimulatedUsers. The maximum number or percentage of users that can be in the pending state (not yet connected and sending traffic) at any time. You can either specify a number or a percentage using the % sign. | 
**max_simulated_users_per_interval** | **int** | Only applies if Type is SimulatedUsers. The maximum number of simulated users at which new users are initiated and teardown per interval(1 second). Default value is 0 (no limit) | [optional] 
**timeline** | [**List[TimelineSegmentUnion]**](TimelineSegmentUnion.md) | The timeline of this objective. | [optional] 
**type** | [**ObjectiveType**](ObjectiveType.md) | The objective&#39;s type (default: Throughput). | 
**unit** | [**ObjectiveUnit**](ObjectiveUnit.md) | The objective&#39;s unit. Must be one of: bps or &#39;&#39;. | 

## Example

```python
from cyperf.models.specific_objective import SpecificObjective

# TODO update the JSON string below
json = "{}"
# create an instance of SpecificObjective from a JSON string
specific_objective_instance = SpecificObjective.from_json(json)
# print the JSON string representation of the object
print(SpecificObjective.to_json())

# convert the object into a dict
specific_objective_dict = specific_objective_instance.to_dict()
# create an instance of SpecificObjective from a dict
specific_objective_from_dict = SpecificObjective.from_dict(specific_objective_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


