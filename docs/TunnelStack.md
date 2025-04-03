# TunnelStack

The tunnel stack assigned to the current test configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inner_ip_range** | [**InnerIPRange**](InnerIPRange.md) |  | [optional] 
**outer_ip_range** | [**IPRange**](IPRange.md) |  | [optional] 
**tunnel_range** | [**TunnelRange**](TunnelRange.md) |  | [optional] 
**tunnel_stack_name** | **str** |  | 
**id** | **str** |  | 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.tunnel_stack import TunnelStack

# TODO update the JSON string below
json = "{}"
# create an instance of TunnelStack from a JSON string
tunnel_stack_instance = TunnelStack.from_json(json)
# print the JSON string representation of the object
print(TunnelStack.to_json())

# convert the object into a dict
tunnel_stack_dict = tunnel_stack_instance.to_dict()
# create an instance of TunnelStack from a dict
tunnel_stack_from_dict = TunnelStack.from_dict(tunnel_stack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


