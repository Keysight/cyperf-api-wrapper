# PSPStack

The PSP (PSP Security Protocol) stack for M×N tunnel mapping

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inner_ip_range** | [**IPRange**](IPRange.md) |  | [optional] 
**outer_ip_range** | [**IPRange**](IPRange.md) |  | [optional] 
**psp_range** | [**PSPRange**](PSPRange.md) |  | [optional] 
**psp_stack_name** | **str** |  | 
**id** | **str** |  | 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.psp_stack import PSPStack

# TODO update the JSON string below
json = "{}"
# create an instance of PSPStack from a JSON string
psp_stack_instance = PSPStack.from_json(json)
# print the JSON string representation of the object
print(PSPStack.to_json())

# convert the object into a dict
psp_stack_dict = psp_stack_instance.to_dict()
# create an instance of PSPStack from a dict
psp_stack_from_dict = PSPStack.from_dict(psp_stack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


