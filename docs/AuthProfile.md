# AuthProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connections** | [**List[Connection]**](Connection.md) | The connections included in the flow | [optional] [readonly] 
**data_types** | [**List[DataType]**](DataType.md) | The data types definition of the parameters | [optional] 
**endpoints** | [**List[Endpoint]**](Endpoint.md) | The list of endpoints used by the authentication profile | [optional] [readonly] 
**file_name** | **str** | The name of the XML file that contains the authentication profile definition | [optional] 
**metadata** | [**AuthProfileMetadata**](AuthProfileMetadata.md) |  | [optional] 
**parameters** | [**List[Parameter]**](Parameter.md) | The parameters of the authentication profile | [optional] [readonly] 
**description** | **str** | The user friendly description of the Auth Profile | [optional] [readonly] 
**id** | **str** | The unique identifier of the profile | [optional] [readonly] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**type** | **str** | The type of the authentication profile | [optional] [readonly] 

## Example

```python
from cyperf.models.auth_profile import AuthProfile

# TODO update the JSON string below
json = "{}"
# create an instance of AuthProfile from a JSON string
auth_profile_instance = AuthProfile.from_json(json)
# print the JSON string representation of the object
print(AuthProfile.to_json())

# convert the object into a dict
auth_profile_dict = auth_profile_instance.to_dict()
# create an instance of AuthProfile from a dict
auth_profile_from_dict = AuthProfile.from_dict(auth_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


