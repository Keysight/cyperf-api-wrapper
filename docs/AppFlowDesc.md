# AppFlowDesc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dst_address** | **bytearray** |  | [optional] 
**dst_port** | **int** |  | [optional] 
**src_address** | **bytearray** |  | [optional] 
**src_port** | **int** |  | [optional] 

## Example

```python
from cyperf.models.app_flow_desc import AppFlowDesc

# TODO update the JSON string below
json = "{}"
# create an instance of AppFlowDesc from a JSON string
app_flow_desc_instance = AppFlowDesc.from_json(json)
# print the JSON string representation of the object
print(AppFlowDesc.to_json())

# convert the object into a dict
app_flow_desc_dict = app_flow_desc_instance.to_dict()
# create an instance of AppFlowDesc from a dict
app_flow_desc_from_dict = AppFlowDesc.from_dict(app_flow_desc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


