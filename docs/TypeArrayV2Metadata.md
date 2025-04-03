# TypeArrayV2Metadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elements** | [**List[ArrayV2ElementMetadata]**](ArrayV2ElementMetadata.md) | The list of array_v2 elements | [optional] 

## Example

```python
from cyperf.models.type_array_v2_metadata import TypeArrayV2Metadata

# TODO update the JSON string below
json = "{}"
# create an instance of TypeArrayV2Metadata from a JSON string
type_array_v2_metadata_instance = TypeArrayV2Metadata.from_json(json)
# print the JSON string representation of the object
print(TypeArrayV2Metadata.to_json())

# convert the object into a dict
type_array_v2_metadata_dict = type_array_v2_metadata_instance.to_dict()
# create an instance of TypeArrayV2Metadata from a dict
type_array_v2_metadata_from_dict = TypeArrayV2Metadata.from_dict(type_array_v2_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


