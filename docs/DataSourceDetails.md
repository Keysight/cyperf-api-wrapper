# DataSourceDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra_filters** | **Dict[str, str]** | Extra filters to be applied to the data source of the panel | [optional] 
**name** | **str** | The name of the data source of the panel | [optional] 
**timestamp_field** | **str** | The name of the timestamp field of the data source of the panel | [optional] 

## Example

```python
from cyperf.models.data_source_details import DataSourceDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DataSourceDetails from a JSON string
data_source_details_instance = DataSourceDetails.from_json(json)
# print the JSON string representation of the object
print(DataSourceDetails.to_json())

# convert the object into a dict
data_source_details_dict = data_source_details_instance.to_dict()
# create an instance of DataSourceDetails from a dict
data_source_details_from_dict = DataSourceDetails.from_dict(data_source_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


