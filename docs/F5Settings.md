# F5Settings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_auth_settings** | [**AuthSettings**](AuthSettings.md) |  | [optional] 
**outer_tcp_profile** | [**TcpProfile**](TcpProfile.md) |  | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**f5_encapsulation** | [**F5Encapsulation**](F5Encapsulation.md) |  | [optional] 
**outer_tls_client_profile** | [**TLSProfile**](TLSProfile.md) |  | [optional] 
**vpn_gateway** | **str** |  | [optional] 

## Example

```python
from cyperf.models.f5_settings import F5Settings

# TODO update the JSON string below
json = "{}"
# create an instance of F5Settings from a JSON string
f5_settings_instance = F5Settings.from_json(json)
# print the JSON string representation of the object
print(F5Settings.to_json())

# convert the object into a dict
f5_settings_dict = f5_settings_instance.to_dict()
# create an instance of F5Settings from a dict
f5_settings_from_dict = F5Settings.from_dict(f5_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


