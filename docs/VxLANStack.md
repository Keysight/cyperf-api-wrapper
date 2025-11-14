# VxLANStack

The VxLAN stack assigned to the current test configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inner_ip_range** | [**IPRange**](IPRange.md) |  | [optional] 
**outer_ip_range** | [**IPRange**](IPRange.md) |  | [optional] 
**vx_lan_range** | [**VxLANRange**](VxLANRange.md) |  | [optional] 
**vx_lan_stack_name** | **str** |  | 
**id** | **str** |  | 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.vx_lan_stack import VxLANStack

# TODO update the JSON string below
json = "{}"
# create an instance of VxLANStack from a JSON string
vx_lan_stack_instance = VxLANStack.from_json(json)
# print the JSON string representation of the object
print(VxLANStack.to_json())

# convert the object into a dict
vx_lan_stack_dict = vx_lan_stack_instance.to_dict()
# create an instance of VxLANStack from a dict
vx_lan_stack_from_dict = VxLANStack.from_dict(vx_lan_stack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


