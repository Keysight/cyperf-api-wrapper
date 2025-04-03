# TypeMediaMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**track_id** | **str** | The media profile track ID | [optional] 
**track_type** | **str** | The media profile track type | [optional] 

## Example

```python
from cyperf.models.type_media_metadata import TypeMediaMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of TypeMediaMetadata from a JSON string
type_media_metadata_instance = TypeMediaMetadata.from_json(json)
# print the JSON string representation of the object
print(TypeMediaMetadata.to_json())

# convert the object into a dict
type_media_metadata_dict = type_media_metadata_instance.to_dict()
# create an instance of TypeMediaMetadata from a dict
type_media_metadata_from_dict = TypeMediaMetadata.from_dict(type_media_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


