# TcpProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**close_with_reset** | **bool** |  | [optional] 
**defer_accept** | **bool** |  | [optional] 
**ecn_enabled** | **bool** |  | [optional] 
**max_rto** | **int** |  | 
**max_src_port** | **int** |  | 
**min_rto** | **int** |  | 
**min_src_port** | **int** |  | 
**ping_pong** | **bool** |  | [optional] 
**pmtu_disc_disabled** | **bool** |  | [optional] 
**recycle_tw_enabled** | **bool** |  | [optional] 
**reordering** | **bool** |  | [optional] 
**reuse_tw_enabled** | **bool** |  | [optional] 
**rx_buffer** | **int** |  | 
**sack_enabled** | **bool** |  | [optional] 
**sock_group** | **str** |  | [optional] 
**timestamp_hdr_enabled** | **bool** |  | [optional] 
**tx_buffer** | **int** |  | 
**user_mss** | **int** |  | [optional] 
**wscale_enabled** | **bool** |  | [optional] 

## Example

```python
from cyperf.models.tcp_profile import TcpProfile

# TODO update the JSON string below
json = "{}"
# create an instance of TcpProfile from a JSON string
tcp_profile_instance = TcpProfile.from_json(json)
# print the JSON string representation of the object
print(TcpProfile.to_json())

# convert the object into a dict
tcp_profile_dict = tcp_profile_instance.to_dict()
# create an instance of TcpProfile from a dict
tcp_profile_from_dict = TcpProfile.from_dict(tcp_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


