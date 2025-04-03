# GetAuthProfiles200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AuthProfile]**](AuthProfile.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from cyperf.models.get_auth_profiles200_response_one_of import GetAuthProfiles200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetAuthProfiles200ResponseOneOf from a JSON string
get_auth_profiles200_response_one_of_instance = GetAuthProfiles200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(GetAuthProfiles200ResponseOneOf.to_json())

# convert the object into a dict
get_auth_profiles200_response_one_of_dict = get_auth_profiles200_response_one_of_instance.to_dict()
# create an instance of GetAuthProfiles200ResponseOneOf from a dict
get_auth_profiles200_response_one_of_from_dict = GetAuthProfiles200ResponseOneOf.from_dict(get_auth_profiles200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


