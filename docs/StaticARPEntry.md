# StaticARPEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**remote_ip** | **str** |  | [optional] 
**remote_ip_incr** | **str** |  | [optional] 
**remote_mac** | **str** |  | [optional] 
**remote_mac_incr** | **str** |  | [optional] 
**static_arp_entry_name** | **str** |  | 
**id** | **str** |  | 

## Example

```python
from cyperf.models.static_arp_entry import StaticARPEntry

# TODO update the JSON string below
json = "{}"
# create an instance of StaticARPEntry from a JSON string
static_arp_entry_instance = StaticARPEntry.from_json(json)
# print the JSON string representation of the object
print(StaticARPEntry.to_json())

# convert the object into a dict
static_arp_entry_dict = static_arp_entry_instance.to_dict()
# create an instance of StaticARPEntry from a dict
static_arp_entry_from_dict = StaticARPEntry.from_dict(static_arp_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


