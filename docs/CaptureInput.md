# CaptureInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capture_id** | **str** |  | [optional] 
**flows** | [**List[AppFlowInput]**](AppFlowInput.md) |  | [optional] 

## Example

```python
from cyperf.models.capture_input import CaptureInput

# TODO update the JSON string below
json = "{}"
# create an instance of CaptureInput from a JSON string
capture_input_instance = CaptureInput.from_json(json)
# print the JSON string representation of the object
print(CaptureInput.to_json())

# convert the object into a dict
capture_input_dict = capture_input_instance.to_dict()
# create an instance of CaptureInput from a dict
capture_input_from_dict = CaptureInput.from_dict(capture_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


