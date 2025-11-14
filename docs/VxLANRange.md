# VxLANRange

The VxLAN IP Ranges assigned to the current test configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hacked_inner_remote_ip_incr** | **str** |  | 
**hacked_inner_remote_ip_start** | **str** |  | 
**md2_tlvs** | [**List[Md2Tlv]**](Md2Tlv.md) |  | [optional] 
**remote_vtep_ip_local_count** | **int** | The number of remote VTEP IPs generated (default: 1). | 
**remote_vtep_ip_local_incr** | **str** | The remote VTEP IP incrementation rule (default: 0.0.0.1). | 
**remote_vtep_ip_range_incr** | **str** | The remote VTEP IP range incrementation rule (default: 0.0.1.0). | 
**remote_vtep_ip_start** | **str** | The start IP for the remote VTEP (default: 10.0.0.10). | 
**total_tunnel_count** | **int** | Outer IP Count * Remote VTEP IP Local Count * VxLAN ID per VTEP Pair Count | 
**use_vx_lan_ids** | **bool** |  | 
**vx_lanid_incr** | **int** | The VxLAN id incrementation rule (default: 1). | 
**vx_lanid_per_vtep_pair_count** | **int** |  | 
**vx_lanid_start** | **int** | The VxLAN start identifier (default: 1). | 
**vx_lan_ids** | [**List[VxLANId]**](VxLANId.md) |  | [optional] 
**vx_lan_range_name** | **str** |  | 
**id** | **str** |  | 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.vx_lan_range import VxLANRange

# TODO update the JSON string below
json = "{}"
# create an instance of VxLANRange from a JSON string
vx_lan_range_instance = VxLANRange.from_json(json)
# print the JSON string representation of the object
print(VxLANRange.to_json())

# convert the object into a dict
vx_lan_range_dict = vx_lan_range_instance.to_dict()
# create an instance of VxLANRange from a dict
vx_lan_range_from_dict = VxLANRange.from_dict(vx_lan_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


