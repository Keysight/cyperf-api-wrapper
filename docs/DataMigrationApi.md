# cyperf.DataMigrationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**poll_controller_migration_export**](DataMigrationApi.md#poll_controller_migration_export) | **GET** /api/v2/controller-migration/operations/export/{id} | 
[**poll_controller_migration_import**](DataMigrationApi.md#poll_controller_migration_import) | **GET** /api/v2/controller-migration/operations/import/{id} | 
[**start_controller_migration_export**](DataMigrationApi.md#start_controller_migration_export) | **POST** /api/v2/controller-migration/operations/export | 
[**start_controller_migration_import**](DataMigrationApi.md#start_controller_migration_import) | **POST** /api/v2/controller-migration/operations/import | 


# **poll_controller_migration_export**
> AsyncContext poll_controller_migration_export(id)



Get the state of an ongoing operation.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
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
    api_instance = cyperf.DataMigrationApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_controller_migration_export(id)
        print("The response of DataMigrationApi->poll_controller_migration_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataMigrationApi->poll_controller_migration_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the async operation. | 

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details about the ongoing operation |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poll_controller_migration_import**
> AsyncContext poll_controller_migration_import(id)



Get the state of an ongoing operation.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
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
    api_instance = cyperf.DataMigrationApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_controller_migration_import(id)
        print("The response of DataMigrationApi->poll_controller_migration_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataMigrationApi->poll_controller_migration_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the async operation. | 

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details about the ongoing operation |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_controller_migration_export**
> AsyncContext start_controller_migration_export(export_package_operation=export_package_operation)



Export the data from the controller as a package.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.export_package_operation import ExportPackageOperation
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
    api_instance = cyperf.DataMigrationApi(api_client)
    export_package_operation = cyperf.ExportPackageOperation() # ExportPackageOperation |  (optional)

    try:
        api_response = api_instance.start_controller_migration_export(export_package_operation=export_package_operation)
        print("The response of DataMigrationApi->start_controller_migration_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataMigrationApi->start_controller_migration_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_package_operation** | [**ExportPackageOperation**](ExportPackageOperation.md)|  | [optional] 

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Details about the operation that just started |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_controller_migration_import**
> AsyncContext start_controller_migration_import()



Import the data from the supplied package into the controller.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
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
    api_instance = cyperf.DataMigrationApi(api_client)

    try:
        api_response = api_instance.start_controller_migration_import()
        print("The response of DataMigrationApi->start_controller_migration_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataMigrationApi->start_controller_migration_import: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Details about the operation that just started |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

