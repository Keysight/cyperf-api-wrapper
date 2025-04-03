# EmulatedSubnetConfig

The Inner IP Range assigned to the current test configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_count_per_tunnel** | **int** |  | 
**hosts_increment** | **str** | The IP incrementation rule (default: 0.0.0.1). | 
**hosts_prefix** | **int** | The network mask of the IP Range (default: 16). | 
**increment** | **str** | The IP incrementation rule (default: 0.0.1.0). | 
**prefix** | **int** | The network mask of the IP Range (default: 16). | 
**start** | **str** | The start IP for the IPRange (default: 10.0.0.10). | 
**total_host_count** | **str** |  | 
**network_tags** | **List[str]** | A list of tags. | 

## Example

```python
from cyperf.models.emulated_subnet_config import EmulatedSubnetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EmulatedSubnetConfig from a JSON string
emulated_subnet_config_instance = EmulatedSubnetConfig.from_json(json)
# print the JSON string representation of the object
print(EmulatedSubnetConfig.to_json())

# convert the object into a dict
emulated_subnet_config_dict = emulated_subnet_config_instance.to_dict()
# create an instance of EmulatedSubnetConfig from a dict
emulated_subnet_config_from_dict = EmulatedSubnetConfig.from_dict(emulated_subnet_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


