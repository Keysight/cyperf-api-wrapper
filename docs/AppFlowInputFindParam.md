# AppFlowInputFindParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_flow_desc** | [**AppFlowDesc**](AppFlowDesc.md) |  | [optional] 
**app_flow_id** | **str** |  | [optional] 
**exchange_names** | **List[str]** |  | [optional] 
**exchanges** | **List[str]** |  | [optional] 

## Example

```python
from cyperf.models.app_flow_input_find_param import AppFlowInputFindParam

# TODO update the JSON string below
json = "{}"
# create an instance of AppFlowInputFindParam from a JSON string
app_flow_input_find_param_instance = AppFlowInputFindParam.from_json(json)
# print the JSON string representation of the object
print(AppFlowInputFindParam.to_json())

# convert the object into a dict
app_flow_input_find_param_dict = app_flow_input_find_param_instance.to_dict()
# create an instance of AppFlowInputFindParam from a dict
app_flow_input_find_param_from_dict = AppFlowInputFindParam.from_dict(app_flow_input_find_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


