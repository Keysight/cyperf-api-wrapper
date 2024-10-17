# AuthenticationSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_method** | **str** |  | [optional] 
**certificate_file** | [**Params**](Params.md) | The authentication certificate file of the IPsec tunnel(s). | [optional] 
**key_file** | [**Params**](Params.md) | The authentication key file of the IPsec tunnel(s). | [optional] 
**key_file_password** | **str** | The key file password of the IPsec authentication. | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**shared_key** | **str** |  | [optional] 

## Example

```python
from cyperf.models.authentication_settings import AuthenticationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationSettings from a JSON string
authentication_settings_instance = AuthenticationSettings.from_json(json)
# print the JSON string representation of the object
print(AuthenticationSettings.to_json())

# convert the object into a dict
authentication_settings_dict = authentication_settings_instance.to_dict()
# create an instance of AuthenticationSettings from a dict
authentication_settings_from_dict = AuthenticationSettings.from_dict(authentication_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


