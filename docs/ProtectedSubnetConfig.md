# ProtectedSubnetConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automatic** | **bool** |  | 
**hosts_increment** | **str** | The increment to be used for enumerating all the emulated subnets of the phase 2 tunnels that belong to each phase 1 (default: 0.0.0.1). | 
**hosts_prefix** | **int** | The Prefix specifies the length (in bits) of the subnet mask to be applied to all the addresses created in the range | 
**increment** | **str** | The increment to be used for enumerating all the emulated subnets in the range (default: 0.0.0.0). | 
**prefix** | **int** | The length (in bits) of the subnet mask to be applied to all the addresses created in the range. | 
**single_protected_subnet** | **bool** |  | 
**start** | **str** | The base address for enumerating all the emulated subnets in the range | 

## Example

```python
from cyperf.models.protected_subnet_config import ProtectedSubnetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectedSubnetConfig from a JSON string
protected_subnet_config_instance = ProtectedSubnetConfig.from_json(json)
# print the JSON string representation of the object
print(ProtectedSubnetConfig.to_json())

# convert the object into a dict
protected_subnet_config_dict = protected_subnet_config_instance.to_dict()
# create an instance of ProtectedSubnetConfig from a dict
protected_subnet_config_from_dict = ProtectedSubnetConfig.from_dict(protected_subnet_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


