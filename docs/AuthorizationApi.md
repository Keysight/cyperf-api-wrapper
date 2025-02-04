# cyperf.AuthorizationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_realms_keysight_protocol_openid_connect_token_post**](AuthorizationApi.md#auth_realms_keysight_protocol_openid_connect_token_post) | **POST** /auth/realms/keysight/protocol/openid-connect/token | 


# **auth_realms_keysight_protocol_openid_connect_token_post**
> AuthRealmsKeysightProtocolOpenidConnectTokenPost200Response auth_realms_keysight_protocol_openid_connect_token_post(client_id=client_id, grant_type=grant_type, password=password, refresh_token=refresh_token, scope=scope, username=username)



Get an access_token and refresh_token with a username+password, or use a refresh_token to generate a new access_token. You can also get a refresh_token from the UI, from Gear Menu > Administration > Offline Tokens. The access_token should be supplied in the Authorization header for all API requests.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.auth_realms_keysight_protocol_openid_connect_token_post200_response import AuthRealmsKeysightProtocolOpenidConnectTokenPost200Response
from cyperf.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cyperf.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["REFRESH_TOKEN"]

configuration.refresh_token = os.environ["REFRESH_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.AuthorizationApi(api_client)
    client_id = 'client_id_example' # str |  (optional)
    grant_type = 'grant_type_example' # str | Controls the type of credentials to be used for authentication. (optional)
    password = 'password_example' # str | (only for grant_type: password) The password to use. (optional)
    refresh_token = 'refresh_token_example' # str | (only for grant_type: refresh_token) The refresh token. You can obtain this from Gear Menu > Administration > Offline Tokens. (optional)
    scope = 'scope_example' # str |  (optional)
    username = 'username_example' # str | (only for grant_type: password) The username to use. (optional)

    try:
        api_response = api_instance.auth_realms_keysight_protocol_openid_connect_token_post(client_id=client_id, grant_type=grant_type, password=password, refresh_token=refresh_token, scope=scope, username=username)
        print("The response of AuthorizationApi->auth_realms_keysight_protocol_openid_connect_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationApi->auth_realms_keysight_protocol_openid_connect_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | [optional] 
 **grant_type** | **str**| Controls the type of credentials to be used for authentication. | [optional] 
 **password** | **str**| (only for grant_type: password) The password to use. | [optional] 
 **refresh_token** | **str**| (only for grant_type: refresh_token) The refresh token. You can obtain this from Gear Menu &gt; Administration &gt; Offline Tokens. | [optional] 
 **scope** | **str**|  | [optional] 
 **username** | **str**| (only for grant_type: password) The username to use. | [optional] 

### Return type

[**AuthRealmsKeysightProtocolOpenidConnectTokenPost200Response**](AuthRealmsKeysightProtocolOpenidConnectTokenPost200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A new token. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

