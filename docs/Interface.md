# Interface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway** | **str** | The gateway address of the interface | [optional] [readonly] 
**ip** | [**List[IpMask]**](IpMask.md) | The list of IP addresses | [optional] [readonly] 
**mac** | **str** | The MAC address of the interface | [optional] [readonly] 
**mtu** | **int** | The maximum transmission unit of the interface | [optional] [readonly] 
**name** | **str** | The name of the interface | [optional] [readonly] 

## Example

```python
from cyperf.models.interface import Interface

# TODO update the JSON string below
json = "{}"
# create an instance of Interface from a JSON string
interface_instance = Interface.from_json(json)
# print the JSON string representation of the object
print(Interface.to_json())

# convert the object into a dict
interface_dict = interface_instance.to_dict()
# create an instance of Interface from a dict
interface_from_dict = Interface.from_dict(interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


