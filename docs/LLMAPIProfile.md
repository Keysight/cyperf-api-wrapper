# LLMAPIProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connections** | [**List[Connection]**](Connection.md) |  | [optional] 
**id** | **str** |  | 
**is_enabled** | **bool** |  | 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**model_name** | **str** |  | 
**params** | [**List[Params]**](Params.md) |  | [optional] 

## Example

```python
from cyperf.models.llmapi_profile import LLMAPIProfile

# TODO update the JSON string below
json = "{}"
# create an instance of LLMAPIProfile from a JSON string
llmapi_profile_instance = LLMAPIProfile.from_json(json)
# print the JSON string representation of the object
print(LLMAPIProfile.to_json())

# convert the object into a dict
llmapi_profile_dict = llmapi_profile_instance.to_dict()
# create an instance of LLMAPIProfile from a dict
llmapi_profile_from_dict = LLMAPIProfile.from_dict(llmapi_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


