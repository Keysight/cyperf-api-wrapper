# SetLinkStateOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controllers** | [**List[PortsByController]**](PortsByController.md) | The controllers that the ports are part of. | [optional] 
**link** | **str** | The desired link state. | [optional] 

## Example

```python
from cyperf.models.set_link_state_operation import SetLinkStateOperation

# TODO update the JSON string below
json = "{}"
# create an instance of SetLinkStateOperation from a JSON string
set_link_state_operation_instance = SetLinkStateOperation.from_json(json)
# print the JSON string representation of the object
print(SetLinkStateOperation.to_json())

# convert the object into a dict
set_link_state_operation_dict = set_link_state_operation_instance.to_dict()
# create an instance of SetLinkStateOperation from a dict
set_link_state_operation_from_dict = SetLinkStateOperation.from_dict(set_link_state_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


