# NtpInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_server** | **str** | Active NTP server | [optional] [readonly] 
**servers** | **List[str]** | NTP servers defined in the systemd-timesyncd configuration file | [optional] 
**status** | **str** | NTP sync status | [optional] [readonly] 

## Example

```python
from cyperf.models.ntp_info import NtpInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NtpInfo from a JSON string
ntp_info_instance = NtpInfo.from_json(json)
# print the JSON string representation of the object
print(NtpInfo.to_json())

# convert the object into a dict
ntp_info_dict = ntp_info_instance.to_dict()
# create an instance of NtpInfo from a dict
ntp_info_from_dict = NtpInfo.from_dict(ntp_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


