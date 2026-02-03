# SnowflakeExporter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Indicates whether the snowflake stats exporter is enabled or not. | 
**polling_interval** | **int** | Polling interval used for fetching and uploading data. | [optional] 
**profile** | [**Params**](Params.md) | The json snowflake profile. | [optional] 
**server_url** | **str** | Snowflake endpoint used for uploading data. | 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.snowflake_exporter import SnowflakeExporter

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeExporter from a JSON string
snowflake_exporter_instance = SnowflakeExporter.from_json(json)
# print the JSON string representation of the object
print(SnowflakeExporter.to_json())

# convert the object into a dict
snowflake_exporter_dict = snowflake_exporter_instance.to_dict()
# create an instance of SnowflakeExporter from a dict
snowflake_exporter_from_dict = SnowflakeExporter.from_dict(snowflake_exporter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


