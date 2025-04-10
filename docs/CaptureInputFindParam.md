# CaptureInputFindParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capture_id** | **str** |  | [optional] 
**flows** | [**List[AppFlowInputFindParam]**](AppFlowInputFindParam.md) |  | [optional] 

## Example

```python
from cyperf.models.capture_input_find_param import CaptureInputFindParam

# TODO update the JSON string below
json = "{}"
# create an instance of CaptureInputFindParam from a JSON string
capture_input_find_param_instance = CaptureInputFindParam.from_json(json)
# print the JSON string representation of the object
print(CaptureInputFindParam.to_json())

# convert the object into a dict
capture_input_find_param_dict = capture_input_find_param_instance.to_dict()
# create an instance of CaptureInputFindParam from a dict
capture_input_find_param_from_dict = CaptureInputFindParam.from_dict(capture_input_find_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


