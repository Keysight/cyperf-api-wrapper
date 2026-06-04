# RemoteSubnetConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automatic** | **bool** |  | 
**hosts_increment** | **str** | The increment to be used for enumerating all the local subnets of the phase 2 tunnels that belong to each phase 1 (default: 0.0.0.1). | 
**hosts_prefix** | **int** | The Prefix specifies the length (in bits) of the subnet mask to be applied to all the addresses created in the range | 
**increment** | **str** | The increment to be used for enumerating all the local subnets in the range (default: 0.0.0.0). | 
**prefix** | **int** | The length (in bits) of the subnet mask to be applied to all the addresses created in the range. | 
**single_remote_subnet** | **bool** |  | 
**start** | **str** | The base address for enumerating all the local subnets in the range | 

## Example

```python
from cyperf.models.remote_subnet_config import RemoteSubnetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteSubnetConfig from a JSON string
remote_subnet_config_instance = RemoteSubnetConfig.from_json(json)
# print the JSON string representation of the object
print(RemoteSubnetConfig.to_json())

# convert the object into a dict
remote_subnet_config_dict = remote_subnet_config_instance.to_dict()
# create an instance of RemoteSubnetConfig from a dict
remote_subnet_config_from_dict = RemoteSubnetConfig.from_dict(remote_subnet_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


