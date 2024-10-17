# GetHttpProfiles200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[HTTPProfile]**](HTTPProfile.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from cyperf.models.get_http_profiles200_response import GetHttpProfiles200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetHttpProfiles200Response from a JSON string
get_http_profiles200_response_instance = GetHttpProfiles200Response.from_json(json)
# print the JSON string representation of the object
print(GetHttpProfiles200Response.to_json())

# convert the object into a dict
get_http_profiles200_response_dict = get_http_profiles200_response_instance.to_dict()
# create an instance of GetHttpProfiles200Response from a dict
get_http_profiles200_response_from_dict = GetHttpProfiles200Response.from_dict(get_http_profiles200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


