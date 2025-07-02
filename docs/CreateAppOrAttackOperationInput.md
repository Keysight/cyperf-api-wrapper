# CreateAppOrAttackOperationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[AddActionInfo]**](AddActionInfo.md) |  | 
**resource_url** | **str** |  | [optional] 

## Example

```python
from cyperf.models.create_app_or_attack_operation_input import CreateAppOrAttackOperationInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAppOrAttackOperationInput from a JSON string
create_app_or_attack_operation_input_instance = CreateAppOrAttackOperationInput.from_json(json)
# print the JSON string representation of the object
print(CreateAppOrAttackOperationInput.to_json())

# convert the object into a dict
create_app_or_attack_operation_input_dict = create_app_or_attack_operation_input_instance.to_dict()
# create an instance of CreateAppOrAttackOperationInput from a dict
create_app_or_attack_operation_input_from_dict = CreateAppOrAttackOperationInput.from_dict(create_app_or_attack_operation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


