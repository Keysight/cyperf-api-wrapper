# TypeIntMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_value** | **int** | The maximum value of the integer | [optional] 
**min_value** | **int** | The minimum value of the integer | [optional] 

## Example

```python
from cyperf.models.type_int_metadata import TypeIntMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of TypeIntMetadata from a JSON string
type_int_metadata_instance = TypeIntMetadata.from_json(json)
# print the JSON string representation of the object
print(TypeIntMetadata.to_json())

# convert the object into a dict
type_int_metadata_dict = type_int_metadata_instance.to_dict()
# create an instance of TypeIntMetadata from a dict
type_int_metadata_from_dict = TypeIntMetadata.from_dict(type_int_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


