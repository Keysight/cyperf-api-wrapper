# Panel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | **List[Dict[str, AppsecAppMetadataKeywordsInner]]** | The filters to be applied to the panel stats | [optional] 
**group_by** | [**List[AdvancedMetric]**](AdvancedMetric.md) | The stats to be used as group by clauses | [optional] 
**limit** | **int** | The maximum number of stats to be generated in a certain interval | [optional] 
**metrics** | [**List[AdvancedMetric]**](AdvancedMetric.md) | The stats to be displayed in the panel | [optional] 
**panel_data_source** | [**DataSourceDetails**](DataSourceDetails.md) |  | [optional] 
**panel_type** | **str** | The type of the panel | [optional] 
**position** | [**GridPosition**](GridPosition.md) |  | [optional] 
**stats_sources** | **List[str]** | The sources of the statistics based on the panel configuration | [optional] 
**title** | **str** | The title of the panel | [optional] 

## Example

```python
from cyperf.models.panel import Panel

# TODO update the JSON string below
json = "{}"
# create an instance of Panel from a JSON string
panel_instance = Panel.from_json(json)
# print the JSON string representation of the object
print(Panel.to_json())

# convert the object into a dict
panel_dict = panel_instance.to_dict()
# create an instance of Panel from a dict
panel_from_dict = Panel.from_dict(panel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


