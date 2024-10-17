# MediaTrack


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bitrate** | **int** |  | [optional] 
**bitrate_kbps** | **int** |  | [optional] 
**codec** | **str** |  | [optional] 
**codec_description** | **str** |  | [optional] 
**id** | **str** |  | 
**track_id** | **str** |  | 
**track_type** | [**TrackType**](TrackType.md) |  | 

## Example

```python
from cyperf.models.media_track import MediaTrack

# TODO update the JSON string below
json = "{}"
# create an instance of MediaTrack from a JSON string
media_track_instance = MediaTrack.from_json(json)
# print the JSON string representation of the object
print(MediaTrack.to_json())

# convert the object into a dict
media_track_dict = media_track_instance.to_dict()
# create an instance of MediaTrack from a dict
media_track_from_dict = MediaTrack.from_dict(media_track_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


