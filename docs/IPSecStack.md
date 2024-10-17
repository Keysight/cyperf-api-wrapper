# IPSecStack


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_certificate_file** | [**Params**](Params.md) | The authentication CA certificate file of the IPsec tunnel(s). | [optional] 
**emulated_sub_config** | [**EmulatedSubnetConfig**](EmulatedSubnetConfig.md) | Deeprecated. Use LocalSubConfig instead. | [optional] 
**enable_rekey** | **bool** |  | 
**id** | **str** |  | 
**ip_sec_range** | [**IPSecRange**](IPSecRange.md) |  | [optional] 
**ip_sec_stack_name** | **str** |  | 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**local_sub_config** | [**LocalSubnetConfig**](LocalSubnetConfig.md) |  | [optional] 
**log_keys** | **bool** |  | 
**max_initiation_rate** | **int** |  | 
**max_pending** | **int** |  | 
**outer_ip_range** | [**IPRange**](IPRange.md) |  | [optional] 
**rekey_margin** | **int** |  | 
**rekey_retry_count** | **int** |  | 
**retransmission_timeout** | **int** |  | 
**retry_count** | **int** |  | 
**retry_interval** | **int** |  | [optional] 
**retry_interval_increment** | **int** |  | [optional] 
**setup_timeout** | **int** |  | 
**stack_role** | **str** |  | 

## Example

```python
from cyperf.models.ip_sec_stack import IPSecStack

# TODO update the JSON string below
json = "{}"
# create an instance of IPSecStack from a JSON string
ip_sec_stack_instance = IPSecStack.from_json(json)
# print the JSON string representation of the object
print(IPSecStack.to_json())

# convert the object into a dict
ip_sec_stack_dict = ip_sec_stack_instance.to_dict()
# create an instance of IPSecStack from a dict
ip_sec_stack_from_dict = IPSecStack.from_dict(ip_sec_stack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


