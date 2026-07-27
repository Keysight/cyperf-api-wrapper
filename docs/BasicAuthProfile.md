# BasicAuthProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**params** | [**List[Params]**](Params.md) |  | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.basic_auth_profile import BasicAuthProfile

# TODO update the JSON string below
json = "{}"
# create an instance of BasicAuthProfile from a JSON string
basic_auth_profile_instance = BasicAuthProfile.from_json(json)
# print the JSON string representation of the object
print(BasicAuthProfile.to_json())

# convert the object into a dict
basic_auth_profile_dict = basic_auth_profile_instance.to_dict()
# create an instance of BasicAuthProfile from a dict
basic_auth_profile_from_dict = BasicAuthProfile.from_dict(basic_auth_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


