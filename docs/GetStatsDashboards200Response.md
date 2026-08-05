# GetStatsDashboards200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[StatsDashboard]**](StatsDashboard.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from cyperf.models.get_stats_dashboards200_response import GetStatsDashboards200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatsDashboards200Response from a JSON string
get_stats_dashboards200_response_instance = GetStatsDashboards200Response.from_json(json)
# print the JSON string representation of the object
print(GetStatsDashboards200Response.to_json())

# convert the object into a dict
get_stats_dashboards200_response_dict = get_stats_dashboards200_response_instance.to_dict()
# create an instance of GetStatsDashboards200Response from a dict
get_stats_dashboards200_response_from_dict = GetStatsDashboards200Response.from_dict(get_stats_dashboards200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


