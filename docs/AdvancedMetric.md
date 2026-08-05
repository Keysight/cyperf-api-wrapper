# AdvancedMetric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the metric | [optional] 
**sort_type** | **str** | The sorting type of the metric | [optional] 
**value** | **str** | The value of the metric | [optional] 

## Example

```python
from cyperf.models.advanced_metric import AdvancedMetric

# TODO update the JSON string below
json = "{}"
# create an instance of AdvancedMetric from a JSON string
advanced_metric_instance = AdvancedMetric.from_json(json)
# print the JSON string representation of the object
print(AdvancedMetric.to_json())

# convert the object into a dict
advanced_metric_dict = advanced_metric_instance.to_dict()
# create an instance of AdvancedMetric from a dict
advanced_metric_from_dict = AdvancedMetric.from_dict(advanced_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


