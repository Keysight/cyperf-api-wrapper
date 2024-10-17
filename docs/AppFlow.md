# AppFlow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dst_address** | **bytearray** |  | [optional] 
**dst_port** | **int** |  | [optional] 
**exchanges** | [**List[AppExchange]**](AppExchange.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**src_address** | **bytearray** |  | [optional] 
**src_port** | **int** |  | [optional] 
**transport_type** | **str** |  | [optional] 

## Example

```python
from cyperf.models.app_flow import AppFlow

# TODO update the JSON string below
json = "{}"
# create an instance of AppFlow from a JSON string
app_flow_instance = AppFlow.from_json(json)
# print the JSON string representation of the object
print(AppFlow.to_json())

# convert the object into a dict
app_flow_dict = app_flow_instance.to_dict()
# create an instance of AppFlow from a dict
app_flow_from_dict = AppFlow.from_dict(app_flow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


