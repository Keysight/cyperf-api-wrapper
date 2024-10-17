# DataType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**values** | [**List[DataTypeValuesInner]**](DataTypeValuesInner.md) | A list of parameters for this data type. | [optional] 

## Example

```python
from cyperf.models.data_type import DataType

# TODO update the JSON string below
json = "{}"
# create an instance of DataType from a JSON string
data_type_instance = DataType.from_json(json)
# print the JSON string representation of the object
print(DataType.to_json())

# convert the object into a dict
data_type_dict = data_type_instance.to_dict()
# create an instance of DataType from a dict
data_type_from_dict = DataType.from_dict(data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


