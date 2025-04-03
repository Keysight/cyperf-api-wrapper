# Capture


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capture_id** | **str** |  | [optional] 
**flows** | [**List[AppFlow]**](AppFlow.md) |  | [optional] 

## Example

```python
from cyperf.models.capture import Capture

# TODO update the JSON string below
json = "{}"
# create an instance of Capture from a JSON string
capture_instance = Capture.from_json(json)
# print the JSON string representation of the object
print(Capture.to_json())

# convert the object into a dict
capture_dict = capture_instance.to_dict()
# create an instance of Capture from a dict
capture_from_dict = Capture.from_dict(capture_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


