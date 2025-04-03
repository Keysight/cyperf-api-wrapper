# TypeStringMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charset** | **str** | The set of characters allowed in string value | [optional] 
**max_length** | **int** | The maximum length of the string value | [optional] 
**min_length** | **int** | The minimum length of the string value | [optional] 

## Example

```python
from cyperf.models.type_string_metadata import TypeStringMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of TypeStringMetadata from a JSON string
type_string_metadata_instance = TypeStringMetadata.from_json(json)
# print the JSON string representation of the object
print(TypeStringMetadata.to_json())

# convert the object into a dict
type_string_metadata_dict = type_string_metadata_instance.to_dict()
# create an instance of TypeStringMetadata from a dict
type_string_metadata_from_dict = TypeStringMetadata.from_dict(type_string_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


