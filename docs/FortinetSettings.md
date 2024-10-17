# FortinetSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_auth_settings** | [**AuthSettings**](AuthSettings.md) |  | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**outer_tcp_profile** | [**TcpProfile**](TcpProfile.md) |  | [optional] 
**fortinet_encapsulation** | [**FortinetEncapsulation**](FortinetEncapsulation.md) |  | [optional] 
**outer_tls_client_profile** | [**TLSProfile**](TLSProfile.md) |  | [optional] 
**vpn_gateway** | **str** |  | [optional] 

## Example

```python
from cyperf.models.fortinet_settings import FortinetSettings

# TODO update the JSON string below
json = "{}"
# create an instance of FortinetSettings from a JSON string
fortinet_settings_instance = FortinetSettings.from_json(json)
# print the JSON string representation of the object
print(FortinetSettings.to_json())

# convert the object into a dict
fortinet_settings_dict = fortinet_settings_instance.to_dict()
# create an instance of FortinetSettings from a dict
fortinet_settings_from_dict = FortinetSettings.from_dict(fortinet_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


