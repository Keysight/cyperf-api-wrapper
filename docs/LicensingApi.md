# cyperf.LicensingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_licenses**](LicensingApi.md#activate_licenses) | **POST** /api/v2/licensing/operations/activate | Performs an online request to KSM and activates the requested licenses.
[**deactivate_licenses**](LicensingApi.md#deactivate_licenses) | **POST** /api/v2/licensing/operations/deactivate | Performs an online request to KSM to deactivate the requested licenses.
[**generate_offline_request**](LicensingApi.md#generate_offline_request) | **GET** /api/v2/licensing/generate-offline-request | Generates an offline request that can be used on the offline licensing portal.
[**get_activation_code_info**](LicensingApi.md#get_activation_code_info) | **POST** /api/v2/licensing/operations/retrieve-activation-code-info | Retrieves the activation code info from KSM.
[**get_activation_code_info_list**](LicensingApi.md#get_activation_code_info_list) | **POST** /api/v2/licensing/operations/retrieve-activation-code-info-list | Retrieves the activation code info list from KSM.
[**get_async_operation_result**](LicensingApi.md#get_async_operation_result) | **GET** /api/v2/licensing/operations/{operationType}/{id}/result | Returns the result of async operation.
[**get_async_operation_status**](LicensingApi.md#get_async_operation_status) | **GET** /api/v2/licensing/operations/{operationType}/{id} | Returns the status of an ongoing async operation.
[**get_counted_feature_stats**](LicensingApi.md#get_counted_feature_stats) | **POST** /api/v2/licensing/operations/retrieve-counted-feature-stats | Retrieves the counted feature stats.
[**get_entitlement_code_info**](LicensingApi.md#get_entitlement_code_info) | **POST** /api/v2/licensing/operations/retrieve-entitlement-code-info | Retrieves the activations codes of the supplied entitlement code from KSM.
[**get_hostid**](LicensingApi.md#get_hostid) | **GET** /api/v2/licensing/hostid | Retrieves the host ID of the license server.
[**get_installed_licenses**](LicensingApi.md#get_installed_licenses) | **GET** /api/v2/licensing/licenses | Returns the installed licenses.
[**get_license**](LicensingApi.md#get_license) | **GET** /api/v2/licensing/licenses/{licenseId} | Returns the requested license.
[**get_license_async_operation_result**](LicensingApi.md#get_license_async_operation_result) | **GET** /api/v2/licensing/licenses/{licenseId}/operations/{operationType}/{id}/result | Returns the result of async operation.
[**get_license_async_operation_status**](LicensingApi.md#get_license_async_operation_status) | **GET** /api/v2/licensing/licenses/{licenseId}/operations/{operationType}/{id} | Returns the status of an ongoing async operation. 
[**import_offline_license**](LicensingApi.md#import_offline_license) | **POST** /api/v2/licensing/import-offline-license | Installs the offline license.
[**remove_reservation**](LicensingApi.md#remove_reservation) | **POST** /api/v2/licensing/licenses/{licenseId}/operations/reservation-remove | Remove previously reserved features, thus making them available for checkout by other users. 
[**sync_licenses**](LicensingApi.md#sync_licenses) | **POST** /api/v2/licensing/operations/synchronize-licenses | Synchronize local licenses with KSM.
[**test_backend_connectivity**](LicensingApi.md#test_backend_connectivity) | **POST** /api/v2/licensing/operations/test-backend-connectivity | Tests connection of the license server with KSM.
[**update_reservation**](LicensingApi.md#update_reservation) | **POST** /api/v2/licensing/licenses/{licenseId}/operations/reservation-reserve | Retain over a period of time specific counts of installed features, that can be consumed only by current user. 


# **activate_licenses**
> AsyncOperationResponse activate_licenses(fulfillment_request=fulfillment_request)

Performs an online request to KSM and activates the requested licenses.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_operation_response import AsyncOperationResponse
from cyperf.models.fulfillment_request import FulfillmentRequest
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
    api_instance = cyperf.LicensingApi(api_client)
    fulfillment_request = [cyperf.FulfillmentRequest()] # List[FulfillmentRequest] | fulfillments to activate (optional)

    try:
        # Performs an online request to KSM and activates the requested licenses.
        api_response = api_instance.activate_licenses(fulfillment_request=fulfillment_request)
        print("The response of LicensingApi->activate_licenses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicensingApi->activate_licenses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_request** | [**List[FulfillmentRequest]**](FulfillmentRequest.md)| fulfillments to activate | [optional] 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. |  -  |
**500** | An error occured. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_licenses**
> AsyncOperationResponse deactivate_licenses(fulfillment_request=fulfillment_request)

Performs an online request to KSM to deactivate the requested licenses.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_operation_response import AsyncOperationResponse
from cyperf.models.fulfillment_request import FulfillmentRequest
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
    api_instance = cyperf.LicensingApi(api_client)
    fulfillment_request = [cyperf.FulfillmentRequest()] # List[FulfillmentRequest] | fulfillments to activate (optional)

    try:
        # Performs an online request to KSM to deactivate the requested licenses.
        api_response = api_instance.deactivate_licenses(fulfillment_request=fulfillment_request)
        print("The response of LicensingApi->deactivate_licenses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicensingApi->deactivate_licenses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_request** | [**List[FulfillmentRequest]**](FulfillmentRequest.md)| fulfillments to activate | [optional] 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. |  -  |
**500** | An error occured. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_offline_request**
> bytearray generate_offline_request()

Generates an offline request that can be used on the offline licensing portal.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
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
    api_instance = cyperf.LicensingApi(api_client)

    try:
        # Generates an offline request that can be used on the offline licensing portal.
        api_response = api_instance.generate_offline_request()
        print("The response of LicensingApi->generate_offline_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicensingApi->generate_offline_request: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**bytearray**

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The offline request. |  -  |
**500** | An error ocurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activation_code_info**
> AsyncOperationResponse get_activation_code_info(activation_code_request=activation_code_request)

Retrieves the activation code info from KSM.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.activation_code_request import ActivationCodeRequest
from cyperf.models.async_operation_response import AsyncOperationResponse
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
    api_instance = cyperf.LicensingApi(api_client)
    activation_code_request = cyperf.ActivationCodeRequest() # ActivationCodeRequest | activation code request (optional)

    try:
        # Retrieves the activation code info from KSM.
        api_response = api_instance.get_activation_code_info(activation_code_request=activation_code_request)
        print("The response of LicensingApi->get_activation_code_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicensingApi->get_activation_code_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activation_code_request** | [**ActivationCodeRequest**](ActivationCodeRequest.md)| activation code request | [optional] 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. |  -  |
**500** | An error occured. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activation_code_info_list**
> AsyncOperationResponse get_activation_code_info_list(activation_code_list_request=activation_code_list_request)

Retrieves the activation code info list from KSM.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.activation_code_list_request import ActivationCodeListRequest
from cyperf.models.async_operation_response import AsyncOperationResponse
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
    api_instance = cyperf.LicensingApi(api_client)
    activation_code_list_request = cyperf.ActivationCodeListRequest() # ActivationCodeListRequest | activation codes request (optional)

    try:
        # Retrieves the activation code info list from KSM.
        api_response = api_instance.get_activation_code_info_list(activation_code_list_request=activation_code_list_request)
        print("The response of LicensingApi->get_activation_code_info_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicensingApi->get_activation_code_info_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activation_code_list_request** | [**ActivationCodeListRequest**](ActivationCodeListRequest.md)| activation codes request | [optional] 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. |  -  |
**500** | An error occured. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_async_operation_result**
> GetAsyncOperationResult200Response get_async_operation_result(operation_type, id)

Returns the result of async operation.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.get_async_operation_result200_response import GetAsyncOperationResult200Response
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
    api_instance = cyperf.LicensingApi(api_client)
    operation_type = 'operation_type_example' # str | The async operation type.
    id = 56 # int | The subresource id of the operation.

    try:
        # Returns the result of async operation.
        api_response = api_instance.get_async_operation_result(operation_type, id)
        print("The response of LicensingApi->get_async_operation_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicensingApi->get_async_operation_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation_type** | **str**| The async operation type. | 
 **id** | **int**| The subresource id of the operation. | 

### Return type

[**GetAsyncOperationResult200Response**](GetAsyncOperationResult200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Completed successfully. |  -  |
**204** | No content. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_async_operation_status**
> AsyncOperationResponse get_async_operation_status(operation_type, id)

Returns the status of an ongoing async operation.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_operation_response import AsyncOperationResponse
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
    api_instance = cyperf.LicensingApi(api_client)
    operation_type = 'operation_type_example' # str | The async operation type.
    id = 56 # int | The subresource id of the operation.

    try:
        # Returns the status of an ongoing async operation.
        api_response = api_instance.get_async_operation_status(operation_type, id)
        print("The response of LicensingApi->get_async_operation_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicensingApi->get_async_operation_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation_type** | **str**| The async operation type. | 
 **id** | **int**| The subresource id of the operation. | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Completed. |  -  |
**500** | An error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_counted_feature_stats**
> AsyncOperationResponse get_counted_feature_stats()

Retrieves the counted feature stats.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_operation_response import AsyncOperationResponse
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
    api_instance = cyperf.LicensingApi(api_client)

    try:
        # Retrieves the counted feature stats.
        api_response = api_instance.get_counted_feature_stats()
        print("The response of LicensingApi->get_counted_feature_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicensingApi->get_counted_feature_stats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. |  -  |
**500** | An error occured. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entitlement_code_info**
> AsyncOperationResponse get_entitlement_code_info(entitlement_code_request=entitlement_code_request)

Retrieves the activations codes of the supplied entitlement code from KSM.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_operation_response import AsyncOperationResponse
from cyperf.models.entitlement_code_request import EntitlementCodeRequest
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
    api_instance = cyperf.LicensingApi(api_client)
    entitlement_code_request = cyperf.EntitlementCodeRequest() # EntitlementCodeRequest | entitlment code request (optional)

    try:
        # Retrieves the activations codes of the supplied entitlement code from KSM.
        api_response = api_instance.get_entitlement_code_info(entitlement_code_request=entitlement_code_request)
        print("The response of LicensingApi->get_entitlement_code_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicensingApi->get_entitlement_code_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entitlement_code_request** | [**EntitlementCodeRequest**](EntitlementCodeRequest.md)| entitlment code request | [optional] 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. |  -  |
**500** | An error occured. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hostid**
> HostID get_hostid()

Retrieves the host ID of the license server.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.host_id import HostID
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
    api_instance = cyperf.LicensingApi(api_client)

    try:
        # Retrieves the host ID of the license server.
        api_response = api_instance.get_hostid()
        print("The response of LicensingApi->get_hostid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicensingApi->get_hostid: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HostID**](HostID.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The host ID of license server. |  -  |
**500** | An error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_installed_licenses**
> List[License] get_installed_licenses()

Returns the installed licenses.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.license import License
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
    api_instance = cyperf.LicensingApi(api_client)

    try:
        # Returns the installed licenses.
        api_response = api_instance.get_installed_licenses()
        print("The response of LicensingApi->get_installed_licenses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicensingApi->get_installed_licenses: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[License]**](License.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The installed licenses. |  -  |
**500** | An error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license**
> License get_license(license_id)

Returns the requested license.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.license import License
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
    api_instance = cyperf.LicensingApi(api_client)
    license_id = 56 # int | The subresource id of the operation.

    try:
        # Returns the requested license.
        api_response = api_instance.get_license(license_id)
        print("The response of LicensingApi->get_license:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicensingApi->get_license: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_id** | **int**| The subresource id of the operation. | 

### Return type

[**License**](License.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested license. |  -  |
**500** | An error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_async_operation_result**
> GetLicenseAsyncOperationResult200Response get_license_async_operation_result(license_id, operation_type, id)

Returns the result of async operation.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.get_license_async_operation_result200_response import GetLicenseAsyncOperationResult200Response
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
    api_instance = cyperf.LicensingApi(api_client)
    license_id = 'license_id_example' # str | The license resource id.
    operation_type = 'operation_type_example' # str | The async operation type.
    id = 56 # int | The subresource id of the operation.

    try:
        # Returns the result of async operation.
        api_response = api_instance.get_license_async_operation_result(license_id, operation_type, id)
        print("The response of LicensingApi->get_license_async_operation_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicensingApi->get_license_async_operation_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_id** | **str**| The license resource id. | 
 **operation_type** | **str**| The async operation type. | 
 **id** | **int**| The subresource id of the operation. | 

### Return type

[**GetLicenseAsyncOperationResult200Response**](GetLicenseAsyncOperationResult200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Completed successfully. |  -  |
**500** | An error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_async_operation_status**
> AsyncOperationResponse get_license_async_operation_status(license_id, operation_type, id)

Returns the status of an ongoing async operation. 

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_operation_response import AsyncOperationResponse
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
    api_instance = cyperf.LicensingApi(api_client)
    license_id = 'license_id_example' # str | The license resource id.
    operation_type = 'operation_type_example' # str | The async operation type.
    id = 56 # int | The subresource id of the operation.

    try:
        # Returns the status of an ongoing async operation. 
        api_response = api_instance.get_license_async_operation_status(license_id, operation_type, id)
        print("The response of LicensingApi->get_license_async_operation_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicensingApi->get_license_async_operation_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_id** | **str**| The license resource id. | 
 **operation_type** | **str**| The async operation type. | 
 **id** | **int**| The subresource id of the operation. | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Completed. |  -  |
**500** | An error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_offline_license**
> ImportOfflineLicenseResult import_offline_license(file_name=file_name)

Installs the offline license.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.import_offline_license_result import ImportOfflineLicenseResult
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
    api_instance = cyperf.LicensingApi(api_client)
    file_name = None # bytearray |  (optional)

    try:
        # Installs the offline license.
        api_response = api_instance.import_offline_license(file_name=file_name)
        print("The response of LicensingApi->import_offline_license:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicensingApi->import_offline_license: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **bytearray**|  | [optional] 

### Return type

[**ImportOfflineLicenseResult**](ImportOfflineLicenseResult.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Completed successfully. |  -  |
**500** | An error ocurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_reservation**
> AsyncOperationResponse remove_reservation(license_id, request_body=request_body)

Remove previously reserved features, thus making them available for checkout by other users. 

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_operation_response import AsyncOperationResponse
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
    api_instance = cyperf.LicensingApi(api_client)
    license_id = 56 # int | The subresource id of the operation.
    request_body = ['request_body_example'] # List[str] | Features remove reservations object. (optional)

    try:
        # Remove previously reserved features, thus making them available for checkout by other users. 
        api_response = api_instance.remove_reservation(license_id, request_body=request_body)
        print("The response of LicensingApi->remove_reservation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicensingApi->remove_reservation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_id** | **int**| The subresource id of the operation. | 
 **request_body** | [**List[str]**](str.md)| Features remove reservations object. | [optional] 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. |  -  |
**500** | An error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_licenses**
> AsyncOperationResponse sync_licenses()

Synchronize local licenses with KSM.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_operation_response import AsyncOperationResponse
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
    api_instance = cyperf.LicensingApi(api_client)

    try:
        # Synchronize local licenses with KSM.
        api_response = api_instance.sync_licenses()
        print("The response of LicensingApi->sync_licenses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicensingApi->sync_licenses: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. |  -  |
**500** | An error occured. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_backend_connectivity**
> AsyncOperationResponse test_backend_connectivity()

Tests connection of the license server with KSM.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_operation_response import AsyncOperationResponse
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
    api_instance = cyperf.LicensingApi(api_client)

    try:
        # Tests connection of the license server with KSM.
        api_response = api_instance.test_backend_connectivity()
        print("The response of LicensingApi->test_backend_connectivity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicensingApi->test_backend_connectivity: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. |  -  |
**500** | An error occured. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_reservation**
> AsyncOperationResponse update_reservation(license_id, feature_reservation_reserve=feature_reservation_reserve)

Retain over a period of time specific counts of installed features, that can be consumed only by current user. 

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_operation_response import AsyncOperationResponse
from cyperf.models.feature_reservation_reserve import FeatureReservationReserve
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
    api_instance = cyperf.LicensingApi(api_client)
    license_id = 56 # int | The subresource id of the operation.
    feature_reservation_reserve = [cyperf.FeatureReservationReserve()] # List[FeatureReservationReserve] | Reservation reserve object. (optional)

    try:
        # Retain over a period of time specific counts of installed features, that can be consumed only by current user. 
        api_response = api_instance.update_reservation(license_id, feature_reservation_reserve=feature_reservation_reserve)
        print("The response of LicensingApi->update_reservation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicensingApi->update_reservation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_id** | **int**| The subresource id of the operation. | 
 **feature_reservation_reserve** | [**List[FeatureReservationReserve]**](FeatureReservationReserve.md)| Reservation reserve object. | [optional] 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. |  -  |
**500** | An error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

