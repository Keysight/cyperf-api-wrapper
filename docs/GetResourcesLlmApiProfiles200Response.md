# GetResourcesLlmApiProfiles200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[LLMAPIProfile]**](LLMAPIProfile.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from cyperf.models.get_resources_llm_api_profiles200_response import GetResourcesLlmApiProfiles200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetResourcesLlmApiProfiles200Response from a JSON string
get_resources_llm_api_profiles200_response_instance = GetResourcesLlmApiProfiles200Response.from_json(json)
# print the JSON string representation of the object
print(GetResourcesLlmApiProfiles200Response.to_json())

# convert the object into a dict
get_resources_llm_api_profiles200_response_dict = get_resources_llm_api_profiles200_response_instance.to_dict()
# create an instance of GetResourcesLlmApiProfiles200Response from a dict
get_resources_llm_api_profiles200_response_from_dict = GetResourcesLlmApiProfiles200Response.from_dict(get_resources_llm_api_profiles200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


