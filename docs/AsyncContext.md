# AsyncContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the async operation | [optional] 
**message** | **str** | A message to the user about the current state of the operation | [optional] 
**progress** | **int** | Number between 0 and 100 showing the current progress of the operation | [optional] 
**result** | **object** | The result of the operation. Appears only if the operation is completed. Not required if resultUrl is populated. The actual type of this field is operation specific. | [optional] 
**result_url** | **str** | The URL where the result of the operation is stored. Appears only if the operation is completed. Not required if the result is populated. | [optional] 
**state** | **str** | A string enum showing the state of the async operation | [optional] 
**type** | **str** | The async operation that is being executed | [optional] 
**url** | **str** | The URL where the user has to call GET requests until the async operation is completed | [optional] 

## Example

```python
from cyperf.models.async_context import AsyncContext

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncContext from a JSON string
async_context_instance = AsyncContext.from_json(json)
# print the JSON string representation of the object
print(AsyncContext.to_json())

# convert the object into a dict
async_context_dict = async_context_instance.to_dict()
# create an instance of AsyncContext from a dict
async_context_from_dict = AsyncContext.from_dict(async_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


