# TunnelSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_auth_settings** | [**AuthSettings**](AuthSettings.md) |  | [optional] 
**outer_tcp_profile** | [**TcpProfile**](TcpProfile.md) |  | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.tunnel_settings import TunnelSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TunnelSettings from a JSON string
tunnel_settings_instance = TunnelSettings.from_json(json)
# print the JSON string representation of the object
print(TunnelSettings.to_json())

# convert the object into a dict
tunnel_settings_dict = tunnel_settings_instance.to_dict()
# create an instance of TunnelSettings from a dict
tunnel_settings_from_dict = TunnelSettings.from_dict(tunnel_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


