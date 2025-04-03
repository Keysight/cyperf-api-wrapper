# ParameterMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | The category associated with the parameter | [optional] 
**category_index** | **int** | The position of the category in the category list | [optional] 
**default** | **str** | The default value of the parameter | [optional] 
**description** | **str** | The description of the parameter | [optional] 
**display_name** | **str** | The user friendly name of the parameter | [optional] 
**enum** | [**Enum**](Enum.md) |  | [optional] 
**flow_identifier** | **bool** | If true, the value of this parameter is used to uniquely identify an application/attack | [optional] 
**input** | **str** | The input of the parameter | [optional] 
**legacy_names** | **List[str]** | The names of the equivalent parameters | [optional] 
**mandatory** | **bool** | The mandatory status of the parameter | [optional] 
**payload** | [**PayloadMetadata**](PayloadMetadata.md) |  | [optional] 
**readonly** | **bool** | The read-only status of the parameter | [optional] 
**shared** | **bool** | The shared status of the parameter | [optional] 
**type** | **str** | The type of the parameter | [optional] 
**type_info** | [**TypeInfoMetadata**](TypeInfoMetadata.md) |  | [optional] 
**unique_value** | **bool** | If true, the value of this parameter must be unique across all Applications/Actions | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.parameter_metadata import ParameterMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterMetadata from a JSON string
parameter_metadata_instance = ParameterMetadata.from_json(json)
# print the JSON string representation of the object
print(ParameterMetadata.to_json())

# convert the object into a dict
parameter_metadata_dict = parameter_metadata_instance.to_dict()
# create an instance of ParameterMetadata from a dict
parameter_metadata_from_dict = ParameterMetadata.from_dict(parameter_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


