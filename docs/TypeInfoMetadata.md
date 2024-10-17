# TypeInfoMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_v2** | [**TypeArrayV2Metadata**](TypeArrayV2Metadata.md) |  | [optional] 
**int** | [**TypeIntMetadata**](TypeIntMetadata.md) |  | [optional] 
**media** | [**TypeMediaMetadata**](TypeMediaMetadata.md) |  | [optional] 
**string** | [**TypeStringMetadata**](TypeStringMetadata.md) |  | [optional] 

## Example

```python
from cyperf.models.type_info_metadata import TypeInfoMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of TypeInfoMetadata from a JSON string
type_info_metadata_instance = TypeInfoMetadata.from_json(json)
# print the JSON string representation of the object
print(TypeInfoMetadata.to_json())

# convert the object into a dict
type_info_metadata_dict = type_info_metadata_instance.to_dict()
# create an instance of TypeInfoMetadata from a dict
type_info_metadata_from_dict = TypeInfoMetadata.from_dict(type_info_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


