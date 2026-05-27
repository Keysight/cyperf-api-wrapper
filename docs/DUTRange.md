# DUTRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**inner_vlan_range** | [**VLANRange**](VLANRange.md) | The inner VLAN range assigned to the current DTLS Range configuration | [optional] 
**ip** | [**SequenceValue**](SequenceValue.md) |  | [optional] 
**outer_vlan_range** | [**VLANRange**](VLANRange.md) | The inner VLAN range assigned to the current DTLS Range configuration | [optional] 
**vlan_type** | [**VLANType**](VLANType.md) | The type of VLAN used | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.dut_range import DUTRange

# TODO update the JSON string below
json = "{}"
# create an instance of DUTRange from a JSON string
dut_range_instance = DUTRange.from_json(json)
# print the JSON string representation of the object
print(DUTRange.to_json())

# convert the object into a dict
dut_range_dict = dut_range_instance.to_dict()
# create an instance of DUTRange from a dict
dut_range_from_dict = DUTRange.from_dict(dut_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


