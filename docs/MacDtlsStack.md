# MacDtlsStack


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dtls_enabled** | **bool** |  | [optional] 
**dtls_range_name** | **str** |  | 
**epoch** | **int** |  | 
**epoch_incr** | **int** |  | [optional] 
**ip_range** | [**IPRange**](IPRange.md) |  | [optional] 
**in_iv** | **str** | The in IV start for the DTLSRange (default: 0x22222222). | 
**in_iv_incr** | **str** | The in IV increment for the DTLSRange (default: 0x00000001). | 
**in_key** | **str** | The in key start for the DTLSRange (default: 0xBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB). | 
**in_key_incr** | **str** | The in key increment for the DTLSRange (default: 0x0000000000000000000000000000000000000000000000000000000000000001). | 
**network_meshing** | [**NetworkMeshing**](NetworkMeshing.md) |  | [optional] 
**out_iv** | **str** | The out IV start for the DTLSRange (default: 0x11111111). | 
**out_iv_incr** | **str** | The out IV increment for the DTLSRange (default: 0x00000001). | 
**out_key** | **str** | The out key start for the DTLSRange (default: 0xAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA). | 
**out_key_incr** | **str** | The out key start for the DTLSRange (default: 0x0000000000000000000000000000000000000000000000000000000000000001). | 
**tunnel_count** | **int** |  | 
**tunnel_destination_mac_incr** | **str** | The MAC address increment rule for the DTLSRange (default: 00:00:00:00:00:01). | 
**tunnel_destination_mac_start** | **str** | The MAC start address for the DTLSRange (default: AA:BB:CC:DD:EE:FF). | 
**vlan_range** | [**VLANRange**](VLANRange.md) | The inner VLAN range assigned to the current DTLS Range configuration | [optional] 
**id** | **str** |  | 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.mac_dtls_stack import MacDtlsStack

# TODO update the JSON string below
json = "{}"
# create an instance of MacDtlsStack from a JSON string
mac_dtls_stack_instance = MacDtlsStack.from_json(json)
# print the JSON string representation of the object
print(MacDtlsStack.to_json())

# convert the object into a dict
mac_dtls_stack_dict = mac_dtls_stack_instance.to_dict()
# create an instance of MacDtlsStack from a dict
mac_dtls_stack_from_dict = MacDtlsStack.from_dict(mac_dtls_stack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


