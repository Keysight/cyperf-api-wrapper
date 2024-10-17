# Parameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_array_elements** | **List[Dict[str, str]]** | The default values of the parameter | [optional] 
**default_source** | **str** | The default source of the parameter | [optional] 
**default_value** | **str** | The default value of the parameter | [optional] 
**element_type** | **str** | The type of elements in the values array | [optional] 
**var_field** | **str** | The name of the ES document field | [optional] 
**id** | **str** | The unique identifier of the parameter | [optional] [readonly] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**metadata** | [**ParameterMetadata**](ParameterMetadata.md) |  | [optional] 
**operator** | **str** | The operator that the parameter supports | [optional] 
**query_param** | **str** | The corresponding query param | [optional] 
**sources** | **List[str]** | The sources of the parameter | [optional] 
**type** | **str** | The type of the parameter | [optional] 

## Example

```python
from cyperf.models.parameter import Parameter

# TODO update the JSON string below
json = "{}"
# create an instance of Parameter from a JSON string
parameter_instance = Parameter.from_json(json)
# print the JSON string representation of the object
print(Parameter.to_json())

# convert the object into a dict
parameter_dict = parameter_instance.to_dict()
# create an instance of Parameter from a dict
parameter_from_dict = Parameter.from_dict(parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


