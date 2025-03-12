# cyperf.DiagnosticsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_diagnostics_components_get**](DiagnosticsApi.md#api_v2_diagnostics_components_get) | **GET** /api/v2/diagnostics/components | 
[**api_v2_diagnostics_operations_delete_delete**](DiagnosticsApi.md#api_v2_diagnostics_operations_delete_delete) | **DELETE** /api/v2/diagnostics/operations/delete | 
[**api_v2_diagnostics_operations_delete_id_delete**](DiagnosticsApi.md#api_v2_diagnostics_operations_delete_id_delete) | **DELETE** /api/v2/diagnostics/operations/delete/{id} | 
[**api_v2_diagnostics_operations_export_get**](DiagnosticsApi.md#api_v2_diagnostics_operations_export_get) | **GET** /api/v2/diagnostics/operations/export | 
[**api_v2_diagnostics_operations_export_id_get**](DiagnosticsApi.md#api_v2_diagnostics_operations_export_id_get) | **GET** /api/v2/diagnostics/operations/export/{id} | 
[**api_v2_diagnostics_operations_export_id_result_get**](DiagnosticsApi.md#api_v2_diagnostics_operations_export_id_result_get) | **GET** /api/v2/diagnostics/operations/export/{id}/result | 
[**api_v2_diagnostics_operations_export_post**](DiagnosticsApi.md#api_v2_diagnostics_operations_export_post) | **POST** /api/v2/diagnostics/operations/export | 


# **api_v2_diagnostics_components_get**
> List[DiagnosticComponent] api_v2_diagnostics_components_get()



Get the list of diagnostic components.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.diagnostic_component import DiagnosticComponent
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

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_CYPERF_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_CYPERF_UI"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.DiagnosticsApi(api_client)

    try:
        api_response = api_instance.api_v2_diagnostics_components_get()
        print("The response of DiagnosticsApi->api_v2_diagnostics_components_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiagnosticsApi->api_v2_diagnostics_components_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[DiagnosticComponent]**](DiagnosticComponent.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of available components. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_diagnostics_operations_delete_delete**
> str api_v2_diagnostics_operations_delete_delete()



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

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_CYPERF_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_CYPERF_UI"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.DiagnosticsApi(api_client)

    try:
        api_response = api_instance.api_v2_diagnostics_operations_delete_delete()
        print("The response of DiagnosticsApi->api_v2_diagnostics_operations_delete_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiagnosticsApi->api_v2_diagnostics_operations_delete_delete: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete all the existing archives from the backend. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_diagnostics_operations_delete_id_delete**
> str api_v2_diagnostics_operations_delete_id_delete(id)



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

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_CYPERF_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_CYPERF_UI"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.DiagnosticsApi(api_client)
    id = 56 # int | The subresource id of the operation.

    try:
        api_response = api_instance.api_v2_diagnostics_operations_delete_id_delete(id)
        print("The response of DiagnosticsApi->api_v2_diagnostics_operations_delete_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiagnosticsApi->api_v2_diagnostics_operations_delete_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The subresource id of the operation. | 

### Return type

**str**

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete all the existing archives from the backend. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_diagnostics_operations_export_get**
> List[ArchiveInfo] api_v2_diagnostics_operations_export_get()



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.archive_info import ArchiveInfo
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

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_CYPERF_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_CYPERF_UI"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.DiagnosticsApi(api_client)

    try:
        api_response = api_instance.api_v2_diagnostics_operations_export_get()
        print("The response of DiagnosticsApi->api_v2_diagnostics_operations_export_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiagnosticsApi->api_v2_diagnostics_operations_export_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ArchiveInfo]**](ArchiveInfo.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of available archives. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_diagnostics_operations_export_id_get**
> AsyncOperationResponse api_v2_diagnostics_operations_export_id_get(id)



Get the state of an ongoing operation.

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

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_CYPERF_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_CYPERF_UI"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.DiagnosticsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_diagnostics_operations_export_id_get(id)
        print("The response of DiagnosticsApi->api_v2_diagnostics_operations_export_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiagnosticsApi->api_v2_diagnostics_operations_export_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the async operation. | 

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
**200** | Details about the ongoing operation. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_diagnostics_operations_export_id_result_get**
> bytearray api_v2_diagnostics_operations_export_id_result_get(id)



Download the diagnostics from the operation with the specified id.

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

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_CYPERF_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_CYPERF_UI"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.DiagnosticsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_diagnostics_operations_export_id_result_get(id)
        print("The response of DiagnosticsApi->api_v2_diagnostics_operations_export_id_result_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiagnosticsApi->api_v2_diagnostics_operations_export_id_result_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the async operation. | 

### Return type

**bytearray**

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully started the diagnostic download. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_diagnostics_operations_export_post**
> AsyncOperationResponse api_v2_diagnostics_operations_export_post(diagnostic_component_context=diagnostic_component_context)



Start the diagnostic export operation.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_operation_response import AsyncOperationResponse
from cyperf.models.diagnostic_component_context import DiagnosticComponentContext
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

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_CYPERF_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_CYPERF_UI"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.DiagnosticsApi(api_client)
    diagnostic_component_context = cyperf.DiagnosticComponentContext() # DiagnosticComponentContext | The list of diagnostic components to export. If the list is empty, all components will be exported. (optional)

    try:
        api_response = api_instance.api_v2_diagnostics_operations_export_post(diagnostic_component_context=diagnostic_component_context)
        print("The response of DiagnosticsApi->api_v2_diagnostics_operations_export_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiagnosticsApi->api_v2_diagnostics_operations_export_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **diagnostic_component_context** | [**DiagnosticComponentContext**](DiagnosticComponentContext.md)| The list of diagnostic components to export. If the list is empty, all components will be exported. | [optional] 

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
**202** | Details about the operation that just started. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

