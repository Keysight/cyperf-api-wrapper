# PlaylistMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column** | **str** | The selected column | [optional] 
**file_name** | **str** | The path of the file | [optional] 

## Example

```python
from cyperf.models.playlist_metadata import PlaylistMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistMetadata from a JSON string
playlist_metadata_instance = PlaylistMetadata.from_json(json)
# print the JSON string representation of the object
print(PlaylistMetadata.to_json())

# convert the object into a dict
playlist_metadata_dict = playlist_metadata_instance.to_dict()
# create an instance of PlaylistMetadata from a dict
playlist_metadata_from_dict = PlaylistMetadata.from_dict(playlist_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


