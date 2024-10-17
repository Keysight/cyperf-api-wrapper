# CountedFeatureStats

Counted feature stats.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_count** | **int** | Available count. | 
**consumers** | [**List[CountedFeatureConsumer]**](CountedFeatureConsumer.md) | Consumed by. | 
**feature_name** | **str** | The feature name. | 
**installed_count** | **int** | Total installed count. | 

## Example

```python
from cyperf.models.counted_feature_stats import CountedFeatureStats

# TODO update the JSON string below
json = "{}"
# create an instance of CountedFeatureStats from a JSON string
counted_feature_stats_instance = CountedFeatureStats.from_json(json)
# print the JSON string representation of the object
print(CountedFeatureStats.to_json())

# convert the object into a dict
counted_feature_stats_dict = counted_feature_stats_instance.to_dict()
# create an instance of CountedFeatureStats from a dict
counted_feature_stats_from_dict = CountedFeatureStats.from_dict(counted_feature_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


