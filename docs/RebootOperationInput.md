# RebootOperationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agents** | [**List[AgentToBeRebooted]**](AgentToBeRebooted.md) | The list of agents to be rebooted | [optional] 
**soft_reboot** | **bool** | A flag indicating whether a soft reboot is preferred | [optional] 

## Example

```python
from cyperf.models.reboot_operation_input import RebootOperationInput

# TODO update the JSON string below
json = "{}"
# create an instance of RebootOperationInput from a JSON string
reboot_operation_input_instance = RebootOperationInput.from_json(json)
# print the JSON string representation of the object
print(RebootOperationInput.to_json())

# convert the object into a dict
reboot_operation_input_dict = reboot_operation_input_instance.to_dict()
# create an instance of RebootOperationInput from a dict
reboot_operation_input_from_dict = RebootOperationInput.from_dict(reboot_operation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


