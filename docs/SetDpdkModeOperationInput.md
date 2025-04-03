# SetDpdkModeOperationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_ids** | **List[str]** | The IDs of the agents for which DPDK mode will be set | [optional] 
**enabled** | **bool** | A flag indicating whether DPDK should be enabled | [optional] 

## Example

```python
from cyperf.models.set_dpdk_mode_operation_input import SetDpdkModeOperationInput

# TODO update the JSON string below
json = "{}"
# create an instance of SetDpdkModeOperationInput from a JSON string
set_dpdk_mode_operation_input_instance = SetDpdkModeOperationInput.from_json(json)
# print the JSON string representation of the object
print(SetDpdkModeOperationInput.to_json())

# convert the object into a dict
set_dpdk_mode_operation_input_dict = set_dpdk_mode_operation_input_instance.to_dict()
# create an instance of SetDpdkModeOperationInput from a dict
set_dpdk_mode_operation_input_from_dict = SetDpdkModeOperationInput.from_dict(set_dpdk_mode_operation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


