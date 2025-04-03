# GetAuthProfiles200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AuthProfile]**](AuthProfile.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from cyperf.models.get_auth_profiles200_response import GetAuthProfiles200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAuthProfiles200Response from a JSON string
get_auth_profiles200_response_instance = GetAuthProfiles200Response.from_json(json)
# print the JSON string representation of the object
print(GetAuthProfiles200Response.to_json())

# convert the object into a dict
get_auth_profiles200_response_dict = get_auth_profiles200_response_instance.to_dict()
# create an instance of GetAuthProfiles200Response from a dict
get_auth_profiles200_response_from_dict = GetAuthProfiles200Response.from_dict(get_auth_profiles200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


