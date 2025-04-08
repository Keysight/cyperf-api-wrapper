# GetResourcesApplicationTypes200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApplicationType]**](ApplicationType.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from cyperf.models.get_resources_application_types200_response import GetResourcesApplicationTypes200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetResourcesApplicationTypes200Response from a JSON string
get_resources_application_types200_response_instance = GetResourcesApplicationTypes200Response.from_json(json)
# print the JSON string representation of the object
print(GetResourcesApplicationTypes200Response.to_json())

# convert the object into a dict
get_resources_application_types200_response_dict = get_resources_application_types200_response_instance.to_dict()
# create an instance of GetResourcesApplicationTypes200Response from a dict
get_resources_application_types200_response_from_dict = GetResourcesApplicationTypes200Response.from_dict(get_resources_application_types200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


