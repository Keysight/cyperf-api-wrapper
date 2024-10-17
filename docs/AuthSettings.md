# AuthSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_method** | [**AuthMethodType**](AuthMethodType.md) |  | [optional] 
**auth_param** | [**Params**](Params.md) |  | [optional] 
**certificate_file** | [**Params**](Params.md) | The authentication certificate file of the VPN tunnel. | [optional] 
**key_file** | [**Params**](Params.md) | The authentication key file of the VPN tunnel. | [optional] 
**key_file_password** | **str** | The key file password of the TLS VPN authentication. | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**passwords** | **List[str]** |  | [optional] 
**passwords_param** | [**Params**](Params.md) |  | [optional] 
**usernames** | **List[str]** |  | [optional] 
**usernames_param** | [**Params**](Params.md) |  | [optional] 

## Example

```python
from cyperf.models.auth_settings import AuthSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AuthSettings from a JSON string
auth_settings_instance = AuthSettings.from_json(json)
# print the JSON string representation of the object
print(AuthSettings.to_json())

# convert the object into a dict
auth_settings_dict = auth_settings_instance.to_dict()
# create an instance of AuthSettings from a dict
auth_settings_from_dict = AuthSettings.from_dict(auth_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


