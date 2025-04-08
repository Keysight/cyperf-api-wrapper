# Parameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matches** | [**List[ParameterMatch]**](ParameterMatch.md) |  | [optional] 
**name** | **str** |  | [optional] 
**var_field** | **str** | The name of the ES document field | [optional] 
**operator** | **str** | The operator that the parameter supports | [optional] 
**query_param** | **str** | The corresponding query param | [optional] 

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


