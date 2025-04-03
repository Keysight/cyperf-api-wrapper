# AppFlowInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_flow_id** | **str** |  | [optional] 
**exchanges** | **List[str]** |  | [optional] 

## Example

```python
from cyperf.models.app_flow_input import AppFlowInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppFlowInput from a JSON string
app_flow_input_instance = AppFlowInput.from_json(json)
# print the JSON string representation of the object
print(AppFlowInput.to_json())

# convert the object into a dict
app_flow_input_dict = app_flow_input_instance.to_dict()
# create an instance of AppFlowInput from a dict
app_flow_input_from_dict = AppFlowInput.from_dict(app_flow_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


