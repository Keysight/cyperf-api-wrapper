# VLANRange

The VLAN range assigned to an IP range configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of VLANs generated (default: 1). | [optional] 
**count_per_agent** | **int** | The number of VLANs that should be assigned to each traffic agent for this VLAN range segment in a valid test (default: 1). | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**max_count_per_agent** | **int** | The maximum number of VLANs that should be assigned to each traffic agent for this VLAN range segment in a valid test (default: 1). | [optional] 
**priority** | **int** | The priority code point value (default: 0). | [optional] 
**static_arp_table** | [**List[StaticARPEntry]**](StaticARPEntry.md) |  | [optional] 
**tag_protocol_id** | **int** | The tag protocol identifier (default: 33024). | [optional] 
**vlan_auto** | **bool** | A flag indicating if VLAN settings for the VLANRange should be determined automatically (default: false). | 
**vlan_enabled** | **bool** | The enable status of the VLAN configuration, if not determined automatically (default: false). | [optional] 
**vlan_id** | **int** | The VLAN identifier (default: 1). | [optional] 
**vlan_incr** | **int** | The VLAN incrementation rule (default: 1). | [optional] 

## Example

```python
from cyperf.models.vlan_range import VLANRange

# TODO update the JSON string below
json = "{}"
# create an instance of VLANRange from a JSON string
vlan_range_instance = VLANRange.from_json(json)
# print the JSON string representation of the object
print(VLANRange.to_json())

# convert the object into a dict
vlan_range_dict = vlan_range_instance.to_dict()
# create an instance of VLANRange from a dict
vlan_range_from_dict = VLANRange.from_dict(vlan_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


