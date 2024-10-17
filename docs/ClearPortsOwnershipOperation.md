# ClearPortsOwnershipOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ports** | **List[str]** | The port ids for which to clear ownership. | [optional] 

## Example

```python
from cyperf.models.clear_ports_ownership_operation import ClearPortsOwnershipOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ClearPortsOwnershipOperation from a JSON string
clear_ports_ownership_operation_instance = ClearPortsOwnershipOperation.from_json(json)
# print the JSON string representation of the object
print(ClearPortsOwnershipOperation.to_json())

# convert the object into a dict
clear_ports_ownership_operation_dict = clear_ports_ownership_operation_instance.to_dict()
# create an instance of ClearPortsOwnershipOperation from a dict
clear_ports_ownership_operation_from_dict = ClearPortsOwnershipOperation.from_dict(clear_ports_ownership_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


