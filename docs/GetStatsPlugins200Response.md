# GetStatsPlugins200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Plugin]**](Plugin.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from cyperf.models.get_stats_plugins200_response import GetStatsPlugins200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatsPlugins200Response from a JSON string
get_stats_plugins200_response_instance = GetStatsPlugins200Response.from_json(json)
# print the JSON string representation of the object
print(GetStatsPlugins200Response.to_json())

# convert the object into a dict
get_stats_plugins200_response_dict = get_stats_plugins200_response_instance.to_dict()
# create an instance of GetStatsPlugins200Response from a dict
get_stats_plugins200_response_from_dict = GetStatsPlugins200Response.from_dict(get_stats_plugins200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


