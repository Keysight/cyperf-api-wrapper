# SingleValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bool_value** | **bool** |  | [optional] 
**float_value** | **float** |  | [optional] 
**integer_value** | **int** |  | [optional] 
**string_value** | **str** |  | [optional] 

## Example

```python
from cyperf.models.single_value import SingleValue

# TODO update the JSON string below
json = "{}"
# create an instance of SingleValue from a JSON string
single_value_instance = SingleValue.from_json(json)
# print the JSON string representation of the object
print(SingleValue.to_json())

# convert the object into a dict
single_value_dict = single_value_instance.to_dict()
# create an instance of SingleValue from a dict
single_value_from_dict = SingleValue.from_dict(single_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


