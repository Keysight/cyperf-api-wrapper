# PluginStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plugin** | **str** | The name of the plugin | [optional] 
**stats** | **List[Dict[str, ConfigMetadataConfigDataValue]]** | The statistics to be ingested | [optional] 
**version** | **str** | The version of the plugin | [optional] 

## Example

```python
from cyperf.models.plugin_stats import PluginStats

# TODO update the JSON string below
json = "{}"
# create an instance of PluginStats from a JSON string
plugin_stats_instance = PluginStats.from_json(json)
# print the JSON string representation of the object
print(PluginStats.to_json())

# convert the object into a dict
plugin_stats_dict = plugin_stats_instance.to_dict()
# create an instance of PluginStats from a dict
plugin_stats_from_dict = PluginStats.from_dict(plugin_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


