# DTLSSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**tls_client_profile** | [**TLSProfile**](TLSProfile.md) |  | [optional] 
**udp_profile** | [**UdpProfile**](UdpProfile.md) |  | [optional] 

## Example

```python
from cyperf.models.dtls_settings import DTLSSettings

# TODO update the JSON string below
json = "{}"
# create an instance of DTLSSettings from a JSON string
dtls_settings_instance = DTLSSettings.from_json(json)
# print the JSON string representation of the object
print(DTLSSettings.to_json())

# convert the object into a dict
dtls_settings_dict = dtls_settings_instance.to_dict()
# create an instance of DTLSSettings from a dict
dtls_settings_from_dict = DTLSSettings.from_dict(dtls_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


