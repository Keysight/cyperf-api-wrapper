# AuthRealmsKeysightProtocolOpenidConnectTokenPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The access token. Set this in the Authorization HTTP Header to authenticate requests. | [optional] 
**expires_in** | **float** | The access token lifetime. | [optional] 
**refresh_expires_in** | **float** | The refresh token lifetime. | [optional] 
**refresh_token** | **str** | Token that can be used with this request and grant_type: refresh_token to get a new access_token if the current one expires. | [optional] 

## Example

```python
from cyperf.models.auth_realms_keysight_protocol_openid_connect_token_post200_response import AuthRealmsKeysightProtocolOpenidConnectTokenPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AuthRealmsKeysightProtocolOpenidConnectTokenPost200Response from a JSON string
auth_realms_keysight_protocol_openid_connect_token_post200_response_instance = AuthRealmsKeysightProtocolOpenidConnectTokenPost200Response.from_json(json)
# print the JSON string representation of the object
print(AuthRealmsKeysightProtocolOpenidConnectTokenPost200Response.to_json())

# convert the object into a dict
auth_realms_keysight_protocol_openid_connect_token_post200_response_dict = auth_realms_keysight_protocol_openid_connect_token_post200_response_instance.to_dict()
# create an instance of AuthRealmsKeysightProtocolOpenidConnectTokenPost200Response from a dict
auth_realms_keysight_protocol_openid_connect_token_post200_response_from_dict = AuthRealmsKeysightProtocolOpenidConnectTokenPost200Response.from_dict(auth_realms_keysight_protocol_openid_connect_token_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


