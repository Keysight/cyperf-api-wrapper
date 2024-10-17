# UdpProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_src_port** | **int** |  | [optional] 
**min_src_port** | **int** |  | [optional] 
**recv_buff_size_ini** | **int** |  | [optional] 
**recv_buff_size_res** | **int** |  | [optional] 
**rx_buffer** | **int** |  | [optional] 
**sock_group** | **str** |  | [optional] 
**tx_buffer** | **int** |  | [optional] 

## Example

```python
from cyperf.models.udp_profile import UdpProfile

# TODO update the JSON string below
json = "{}"
# create an instance of UdpProfile from a JSON string
udp_profile_instance = UdpProfile.from_json(json)
# print the JSON string representation of the object
print(UdpProfile.to_json())

# convert the object into a dict
udp_profile_dict = udp_profile_instance.to_dict()
# create an instance of UdpProfile from a dict
udp_profile_from_dict = UdpProfile.from_dict(udp_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


