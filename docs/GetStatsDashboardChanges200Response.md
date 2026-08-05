# GetStatsDashboardChanges200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ChangeEvent]**](ChangeEvent.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from cyperf.models.get_stats_dashboard_changes200_response import GetStatsDashboardChanges200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatsDashboardChanges200Response from a JSON string
get_stats_dashboard_changes200_response_instance = GetStatsDashboardChanges200Response.from_json(json)
# print the JSON string representation of the object
print(GetStatsDashboardChanges200Response.to_json())

# convert the object into a dict
get_stats_dashboard_changes200_response_dict = get_stats_dashboard_changes200_response_instance.to_dict()
# create an instance of GetStatsDashboardChanges200Response from a dict
get_stats_dashboard_changes200_response_from_dict = GetStatsDashboardChanges200Response.from_dict(get_stats_dashboard_changes200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


