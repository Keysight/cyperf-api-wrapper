# DataTypeValuesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The name of the parameter. | [optional] 
**value_type** | **str** | The default value of the parameter. | [optional] 

## Example

```python
from cyperf.models.data_type_values_inner import DataTypeValuesInner

# TODO update the JSON string below
json = "{}"
# create an instance of DataTypeValuesInner from a JSON string
data_type_values_inner_instance = DataTypeValuesInner.from_json(json)
# print the JSON string representation of the object
print(DataTypeValuesInner.to_json())

# convert the object into a dict
data_type_values_inner_dict = data_type_values_inner_instance.to_dict()
# create an instance of DataTypeValuesInner from a dict
data_type_values_inner_from_dict = DataTypeValuesInner.from_dict(data_type_values_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


