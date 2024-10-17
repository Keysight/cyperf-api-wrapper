# MediaFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_value** | [**FileValue**](FileValue.md) |  | [optional] 
**id** | **str** |  | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**media_tracks** | [**List[MediaTrack]**](MediaTrack.md) |  | [optional] 

## Example

```python
from cyperf.models.media_file import MediaFile

# TODO update the JSON string below
json = "{}"
# create an instance of MediaFile from a JSON string
media_file_instance = MediaFile.from_json(json)
# print the JSON string representation of the object
print(MediaFile.to_json())

# convert the object into a dict
media_file_dict = media_file_instance.to_dict()
# create an instance of MediaFile from a dict
media_file_from_dict = MediaFile.from_dict(media_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


