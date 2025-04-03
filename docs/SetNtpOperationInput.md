# SetNtpOperationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_ids** | **List[str]** | The IDs of the agents whose NTP configuration will be updated | [optional] 
**servers** | **List[str]** | The list of NTP servers to be configured on each agent | [optional] 

## Example

```python
from cyperf.models.set_ntp_operation_input import SetNtpOperationInput

# TODO update the JSON string below
json = "{}"
# create an instance of SetNtpOperationInput from a JSON string
set_ntp_operation_input_instance = SetNtpOperationInput.from_json(json)
# print the JSON string representation of the object
print(SetNtpOperationInput.to_json())

# convert the object into a dict
set_ntp_operation_input_dict = set_ntp_operation_input_instance.to_dict()
# create an instance of SetNtpOperationInput from a dict
set_ntp_operation_input_from_dict = SetNtpOperationInput.from_dict(set_ntp_operation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


