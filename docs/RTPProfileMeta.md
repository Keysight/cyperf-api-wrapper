# RTPProfileMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_header_len_offset** | **int** | The offset where the custom header length field is present | [optional] 
**custom_header_len_size** | **int** | The length of the custom header length field is present | [optional] 
**custom_header_signature** | **bytearray** | The signature of the custom header | [optional] 
**custom_header_signature_offset** | **int** | The offset where the custom header signature can be found | [optional] 
**custom_header_size** | **int** | The max size of the custom header | [optional] 
**encryption_mode** | **str** | The desired encryption mode | [optional] 
**requires_rtp_profile** | **bool** | Indicates that this applicaiton type requires an RTP profile | [optional] 

## Example

```python
from cyperf.models.rtp_profile_meta import RTPProfileMeta

# TODO update the JSON string below
json = "{}"
# create an instance of RTPProfileMeta from a JSON string
rtp_profile_meta_instance = RTPProfileMeta.from_json(json)
# print the JSON string representation of the object
print(RTPProfileMeta.to_json())

# convert the object into a dict
rtp_profile_meta_dict = rtp_profile_meta_instance.to_dict()
# create an instance of RTPProfileMeta from a dict
rtp_profile_meta_from_dict = RTPProfileMeta.from_dict(rtp_profile_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


