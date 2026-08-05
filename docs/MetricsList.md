# MetricsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard_id** | **str** | The id of the dashboard with these metrics | [optional] 
**metrics** | [**List[AdvancedMetric]**](AdvancedMetric.md) | The list of metrics in the specified dashboard | [optional] 

## Example

```python
from cyperf.models.metrics_list import MetricsList

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsList from a JSON string
metrics_list_instance = MetricsList.from_json(json)
# print the JSON string representation of the object
print(MetricsList.to_json())

# convert the object into a dict
metrics_list_dict = metrics_list_instance.to_dict()
# create an instance of MetricsList from a dict
metrics_list_from_dict = MetricsList.from_dict(metrics_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


