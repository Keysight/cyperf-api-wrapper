# GetAgentsTags200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AgentsGroup]**](AgentsGroup.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from cyperf.models.get_agents_tags200_response import GetAgentsTags200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAgentsTags200Response from a JSON string
get_agents_tags200_response_instance = GetAgentsTags200Response.from_json(json)
# print the JSON string representation of the object
print(GetAgentsTags200Response.to_json())

# convert the object into a dict
get_agents_tags200_response_dict = get_agents_tags200_response_instance.to_dict()
# create an instance of GetAgentsTags200Response from a dict
get_agents_tags200_response_from_dict = GetAgentsTags200Response.from_dict(get_agents_tags200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


