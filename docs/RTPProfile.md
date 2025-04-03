# RTPProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryption_mode** | [**RTPEncryptionMode**](RTPEncryptionMode.md) |  | 
**mos_mode** | [**MosMode**](MosMode.md) |  | 
**profile_id** | **str** | The ID of the RTP profile (default: VoiceProfile). | 

## Example

```python
from cyperf.models.rtp_profile import RTPProfile

# TODO update the JSON string below
json = "{}"
# create an instance of RTPProfile from a JSON string
rtp_profile_instance = RTPProfile.from_json(json)
# print the JSON string representation of the object
print(RTPProfile.to_json())

# convert the object into a dict
rtp_profile_dict = rtp_profile_instance.to_dict()
# create an instance of RTPProfile from a dict
rtp_profile_from_dict = RTPProfile.from_dict(rtp_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


