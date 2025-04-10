# ActionInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**captures** | [**List[CaptureInput]**](CaptureInput.md) |  | [optional] 
**name** | **str** |  | [optional] 
**parameters** | [**List[Parameter]**](Parameter.md) |  | [optional] 

## Example

```python
from cyperf.models.action_input import ActionInput

# TODO update the JSON string below
json = "{}"
# create an instance of ActionInput from a JSON string
action_input_instance = ActionInput.from_json(json)
# print the JSON string representation of the object
print(ActionInput.to_json())

# convert the object into a dict
action_input_dict = action_input_instance.to_dict()
# create an instance of ActionInput from a dict
action_input_from_dict = ActionInput.from_dict(action_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


