# CountedFeatureConsumer

Counted feature consumer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | **str** | The application consuming the feature. | 
**client** | **str** | The client consuming the feature. | 
**consumed_count** | **int** | The count consumed. | 
**reserved_count** | **int** | The count reserved. | 
**reserved_remaining_duration** | **int** | Remaining reserved duration, in seconds. | 
**user** | **str** | The user consuming the feature. | 

## Example

```python
from cyperf.models.counted_feature_consumer import CountedFeatureConsumer

# TODO update the JSON string below
json = "{}"
# create an instance of CountedFeatureConsumer from a JSON string
counted_feature_consumer_instance = CountedFeatureConsumer.from_json(json)
# print the JSON string representation of the object
print(CountedFeatureConsumer.to_json())

# convert the object into a dict
counted_feature_consumer_dict = counted_feature_consumer_instance.to_dict()
# create an instance of CountedFeatureConsumer from a dict
counted_feature_consumer_from_dict = CountedFeatureConsumer.from_dict(counted_feature_consumer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


