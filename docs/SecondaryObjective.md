# SecondaryObjective


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | If false, the values of this objective will be ignored. | 
**max_pending_simulated_users** | **str** | Only applies if Type is SimulatedUsers. The maximum number or percentage of users that can be in the pending state (not yet connected and sending traffic) at any time. You can either specify a number or a percentage using the % sign. | 
**max_simulated_users_per_interval** | **int** | Only applies if Type is SimulatedUsers. The maximum number of simulated users at which new users are initiated and teardown per interval(1 second). Default value is 0 (no limit) | [optional] 
**objective_unit** | **str** | The objective&#39;s unit. | 
**objective_value** | **float** | The value of the secondary objective. This value will be used for the whole duration of the test. | 
**type** | [**ObjectiveType**](ObjectiveType.md) | The objective&#39;s type (default: SimulatedUsers). | 

## Example

```python
from cyperf.models.secondary_objective import SecondaryObjective

# TODO update the JSON string below
json = "{}"
# create an instance of SecondaryObjective from a JSON string
secondary_objective_instance = SecondaryObjective.from_json(json)
# print the JSON string representation of the object
print(SecondaryObjective.to_json())

# convert the object into a dict
secondary_objective_dict = secondary_objective_instance.to_dict()
# create an instance of SecondaryObjective from a dict
secondary_objective_from_dict = SecondaryObjective.from_dict(secondary_objective_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


