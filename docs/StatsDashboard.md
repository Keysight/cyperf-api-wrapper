# StatsDashboard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**List[ChangeEvent]**](ChangeEvent.md) | The changes hook | [optional] 
**group_id** | **str** | The group identifier of the dashboard | [optional] 
**id** | **str** | The unique identifier of the dashboard | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**metrics** | [**MetricsList**](MetricsList.md) |  | [optional] 
**name** | **str** | The name of the dashboard | [optional] 
**owner** | **str** | The friendly display name of the entity that created the dashboard | [optional] [readonly] 
**owner_id** | **str** | The unique identifier of the entity that created the dashboard | [optional] [readonly] 
**panels** | [**List[Panel]**](Panel.md) | The list of panels in the dashboard | [optional] 
**read_only** | **bool** | Is a read only dashboard | [optional] 
**type** | **str** | The application type of the dashboard | [optional] 

## Example

```python
from cyperf.models.stats_dashboard import StatsDashboard

# TODO update the JSON string below
json = "{}"
# create an instance of StatsDashboard from a JSON string
stats_dashboard_instance = StatsDashboard.from_json(json)
# print the JSON string representation of the object
print(StatsDashboard.to_json())

# convert the object into a dict
stats_dashboard_dict = stats_dashboard_instance.to_dict()
# create an instance of StatsDashboard from a dict
stats_dashboard_from_dict = StatsDashboard.from_dict(stats_dashboard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


