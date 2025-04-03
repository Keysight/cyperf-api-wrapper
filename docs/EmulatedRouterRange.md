# EmulatedRouterRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automatic_ip_type** | [**AutomaticIpType**](AutomaticIpType.md) | The automatic IP types, either &#39;ONLY_IPV4&#39;, &#39;ONLY_IPV6&#39; or &#39;BOTH_IPV4_IPV6&#39;. | [optional] 
**count** | **int** | The number of IPs generated (default: 1). | [optional] 
**gw_auto** | **bool** | A flag indicating if the gateway settings for the IPRange should be determined automatically (default: true). | 
**gw_start** | **str** | The gateway start IP for the IPRange (default: 10.0.0.1). | [optional] 
**host_count** | **int** | The number of Host IPs generated (default: 1). | [optional] 
**inner_vlan_range** | [**VLANRange**](VLANRange.md) | The inner VLAN range assigned to the current IP range configuration | [optional] 
**ip_auto** | **bool** | A flag indicating if IP settings for the IPRange should be determined automatically (default: true). | 
**ip_incr** | **str** | The IP incrementation rule (default: 0.0.0.1). | [optional] 
**ip_range_name** | **str** |  | 
**ip_start** | **str** | The start IP for the IPRange (default: 10.0.0.10). | [optional] 
**ip_ver** | [**IpVer**](IpVer.md) | The type of the IP. &#39;IPV4&#39; and &#39;IPV6&#39; are both supported currently. | 
**is_emulated_router** | **bool** |  | [optional] 
**mss** | **int** | The maximum segment size of the TCP header. | 
**mss_auto** | **bool** | A flag indicating if Mss settings for the IPRange should be determined automatically (default: false). | 
**net_mask** | **int** | The network mask of the IP Range (default: 16). | [optional] 
**net_mask_auto** | **bool** | A flag indicating if the network mask of the IPRange should be determined automatically (default: true). | 
**id** | **str** |  | 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**max_count_per_agent** | **int** | The maximum number of IPs that should be assigned to each traffic agent for this IP range segment in a valid test (default: 1). | [optional] 
**network_tags** | **List[str]** | A list of tags. | [optional] 

## Example

```python
from cyperf.models.emulated_router_range import EmulatedRouterRange

# TODO update the JSON string below
json = "{}"
# create an instance of EmulatedRouterRange from a JSON string
emulated_router_range_instance = EmulatedRouterRange.from_json(json)
# print the JSON string representation of the object
print(EmulatedRouterRange.to_json())

# convert the object into a dict
emulated_router_range_dict = emulated_router_range_instance.to_dict()
# create an instance of EmulatedRouterRange from a dict
emulated_router_range_from_dict = EmulatedRouterRange.from_dict(emulated_router_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


