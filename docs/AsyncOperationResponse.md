# AsyncOperationResponse

The POST response for an async operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The subresource id of the status. | 
**message** | **str** | A message from the operation (optional). | 
**progress** | **int** | The progress of the operation (percent). | 
**result_url** | **str** | The URL where the archive is available. | 
**state** | **str** | The state of the operation. | 
**type** | **str** | The name of the operation. | 
**url** | **str** | The status URI of the operation. | 

## Example

```python
from cyperf.models.async_operation_response import AsyncOperationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncOperationResponse from a JSON string
async_operation_response_instance = AsyncOperationResponse.from_json(json)
# print the JSON string representation of the object
print(AsyncOperationResponse.to_json())

# convert the object into a dict
async_operation_response_dict = async_operation_response_instance.to_dict()
# create an instance of AsyncOperationResponse from a dict
async_operation_response_from_dict = AsyncOperationResponse.from_dict(async_operation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


