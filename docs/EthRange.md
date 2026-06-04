# EthRange

The Ethernet Ranges assigned to the current test configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**mac_auto** | **bool** | A flag indicating if the MAC address for the EthRange should be determined automatically (default: true). | 
**mac_incr** | **str** | The MAC address increment rule for the EthRange (default: 00:00:00:00:00:01). | [optional] 
**mac_start** | **str** | The MAC start address for the EthRange (default: 00:11:01:00:00:01). | [optional] 
**one_mac_per_ip** | **bool** | A flag indicating if there is only one MAC address for the EthRange per IPRange (default: true). | [optional] 
**static_arp_table** | [**List[StaticARPEntry]**](StaticARPEntry.md) |  | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**max_count_per_agent** | **int** | The maximum number of MACs that should be assigned to each traffic agent for this Ethernet range segment in a valid test (default: 0, split equally between agents). | [optional] 

## Example

```python
from cyperf.models.eth_range import EthRange

# TODO update the JSON string below
json = "{}"
# create an instance of EthRange from a JSON string
eth_range_instance = EthRange.from_json(json)
# print the JSON string representation of the object
print(EthRange.to_json())

# convert the object into a dict
eth_range_dict = eth_range_instance.to_dict()
# create an instance of EthRange from a dict
eth_range_from_dict = EthRange.from_dict(eth_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


