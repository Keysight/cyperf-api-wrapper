# TransportProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_http_profile** | [**HTTPProfile**](HTTPProfile.md) | The client HTTP profile used in the Scenario. | [optional] 
**client_tls_profile** | [**TLSProfile**](TLSProfile.md) |  | [optional] 
**client_tcp_profile** | [**TcpProfile**](TcpProfile.md) |  | [optional] 
**ip_tos** | **int** |  | [optional] 
**rtp_profile** | [**RTPProfile**](RTPProfile.md) |  | [optional] 
**server_http_profile** | [**HTTPProfile**](HTTPProfile.md) | The server HTTP profile used in the Scenario. | [optional] 
**server_tls_profile** | [**TLSProfile**](TLSProfile.md) |  | [optional] 
**server_tcp_profile** | [**TcpProfile**](TcpProfile.md) |  | [optional] 
**udp_profile** | [**UdpProfile**](UdpProfile.md) |  | [optional] 
**vlan_prio** | **int** |  | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**l4_profile_name** | **str** |  | 

## Example

```python
from cyperf.models.transport_profile import TransportProfile

# TODO update the JSON string below
json = "{}"
# create an instance of TransportProfile from a JSON string
transport_profile_instance = TransportProfile.from_json(json)
# print the JSON string representation of the object
print(TransportProfile.to_json())

# convert the object into a dict
transport_profile_dict = transport_profile_instance.to_dict()
# create an instance of TransportProfile from a dict
transport_profile_from_dict = TransportProfile.from_dict(transport_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


