# PSPRange

The PSP tunnel range configuration for M×N tunnel mapping

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**master_key0** | **str** | Master key for phase 0 (256-bit hex string). | 
**master_key1** | **str** | Master key for phase 1 (256-bit hex string). | 
**psp_range_name** | **str** |  | 
**psp_version** | **str** | PSP version: AES-GCM-128, AES-GMAC-128 (default: AES-GCM-128). | 
**remote_inner_ip_count** | **int** | Total Remote Inner IP Count: RemoteTunnelIpCount * RemoteTunnelToInnerIpCountRatio | 
**remote_inner_ip_incr** | **str** | The remote inner IP increment (default: 0.0.0.1). | 
**remote_inner_ip_start** | **str** | The start IP for remote inner IPs. | 
**remote_tunnel_ip_count** | **int** | The number of remote tunnel IPs (default: 1). | 
**remote_tunnel_ip_incr** | **str** | The remote tunnel IP increment (default: 0.0.0.1). | 
**remote_tunnel_ip_start** | **str** | The start IP for the remote tunnel endpoint. | 
**remote_tunnel_to_inner_ip_count_ratio** | **int** | The ratio between the number of remote Tunnel IPs and Remote Inner IPs - (default: 1). | 
**spi_base** | **int** | Security Parameter Index base value (default: 256). | 
**spi_incr** | **int** | SPI increment per tunnel (default: 1). | 
**total_tunnel_count** | **int** | Total tunnel count: OuterIP.Count × RemoteTunnelIpCount (M×N). | 
**id** | **str** |  | 

## Example

```python
from cyperf.models.psp_range import PSPRange

# TODO update the JSON string below
json = "{}"
# create an instance of PSPRange from a JSON string
psp_range_instance = PSPRange.from_json(json)
# print the JSON string representation of the object
print(PSPRange.to_json())

# convert the object into a dict
psp_range_dict = psp_range_instance.to_dict()
# create an instance of PSPRange from a dict
psp_range_from_dict = PSPRange.from_dict(psp_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


