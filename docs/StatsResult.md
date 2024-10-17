# StatsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_filters** | [**List[Parameter]**](Parameter.md) | The list of available filters | [optional] 
**columns** | **List[str]** | The list of columns returned by the query | [optional] 
**name** | **str** | The name of the query | [optional] 
**snapshots** | [**List[Snapshot]**](Snapshot.md) | The list of snapshots returned by the query | [optional] 

## Example

```python
from cyperf.models.stats_result import StatsResult

# TODO update the JSON string below
json = "{}"
# create an instance of StatsResult from a JSON string
stats_result_instance = StatsResult.from_json(json)
# print the JSON string representation of the object
print(StatsResult.to_json())

# convert the object into a dict
stats_result_dict = stats_result_instance.to_dict()
# create an instance of StatsResult from a dict
stats_result_from_dict = StatsResult.from_dict(stats_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


