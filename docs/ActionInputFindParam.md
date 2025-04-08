# ActionInputFindParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**captures** | [**List[CaptureInputFindParam]**](CaptureInputFindParam.md) |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from cyperf.models.action_input_find_param import ActionInputFindParam

# TODO update the JSON string below
json = "{}"
# create an instance of ActionInputFindParam from a JSON string
action_input_find_param_instance = ActionInputFindParam.from_json(json)
# print the JSON string representation of the object
print(ActionInputFindParam.to_json())

# convert the object into a dict
action_input_find_param_dict = action_input_find_param_instance.to_dict()
# create an instance of ActionInputFindParam from a dict
action_input_find_param_from_dict = ActionInputFindParam.from_dict(action_input_find_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


