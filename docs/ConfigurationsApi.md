# cyperf.ConfigurationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_configs**](ConfigurationsApi.md#create_configs) | **POST** /api/v2/configs | 
[**delete_configs**](ConfigurationsApi.md#delete_configs) | **DELETE** /api/v2/configs/{configId} | 
[**get_config_categories**](ConfigurationsApi.md#get_config_categories) | **GET** /api/v2/config-categories | 
[**get_configs**](ConfigurationsApi.md#get_configs) | **GET** /api/v2/configs | 
[**get_configs_by_id**](ConfigurationsApi.md#get_configs_by_id) | **GET** /api/v2/configs/{configId} | 
[**get_custom_import_operations**](ConfigurationsApi.md#get_custom_import_operations) | **GET** /api/v2/resources/custom-import-operations | 
[**patch_configs**](ConfigurationsApi.md#patch_configs) | **PATCH** /api/v2/configs/{configId} | 
[**poll_configs_batch_delete**](ConfigurationsApi.md#poll_configs_batch_delete) | **GET** /api/v2/configs/operations/batch-delete/{id} | 
[**poll_configs_export_all**](ConfigurationsApi.md#poll_configs_export_all) | **GET** /api/v2/configs/operations/exportAll/{id} | 
[**poll_configs_import**](ConfigurationsApi.md#poll_configs_import) | **GET** /api/v2/configs/operations/import/{id} | 
[**poll_configs_import_all**](ConfigurationsApi.md#poll_configs_import_all) | **GET** /api/v2/configs/operations/importAll/{id} | 
[**start_configs_batch_delete**](ConfigurationsApi.md#start_configs_batch_delete) | **POST** /api/v2/configs/operations/batch-delete | 
[**start_configs_export_all**](ConfigurationsApi.md#start_configs_export_all) | **POST** /api/v2/configs/operations/exportAll | 
[**start_configs_import**](ConfigurationsApi.md#start_configs_import) | **POST** /api/v2/configs/operations/import | 
[**start_configs_import_all**](ConfigurationsApi.md#start_configs_import_all) | **POST** /api/v2/configs/operations/importAll | 
[**update_configs**](ConfigurationsApi.md#update_configs) | **PUT** /api/v2/configs/{configId} | 


# **create_configs**
> List[ConfigMetadata] create_configs(config_metadata=config_metadata)



Save or import a new configuration. If the ConfigData field is not provided, this is implemented as a Save operation, only recording the metadata.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.config_metadata import ConfigMetadata
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
    api_instance = cyperf.ConfigurationsApi(api_client)
    config_metadata = [cyperf.ConfigMetadata()] # List[ConfigMetadata] |  (optional)

    try:
        api_response = api_instance.create_configs(config_metadata=config_metadata)
        print("The response of ConfigurationsApi->create_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->create_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_metadata** | [**List[ConfigMetadata]**](ConfigMetadata.md)|  | [optional] 

### Return type

[**List[ConfigMetadata]**](ConfigMetadata.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/x-zip, application/zip, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The configuration that was saved or imported |  -  |
**400** | Bad request |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_configs**
> delete_configs(config_id)



Delete a particular configuration.

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
    api_instance = cyperf.ConfigurationsApi(api_client)
    config_id = 'config_id_example' # str | The ID of the config.

    try:
        api_instance.delete_configs(config_id)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->delete_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The ID of the config. | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The configuration was successfully deleted. |  -  |
**403** | The initiator of the request does not have enough privileges to perform the action. |  -  |
**404** | A configuration with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_categories**
> GetConfigCategories200Response get_config_categories(take=take, skip=skip)



Get the list of available configuration categories.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.get_config_categories200_response import GetConfigCategories200Response
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
    api_instance = cyperf.ConfigurationsApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.get_config_categories(take=take, skip=skip)
        print("The response of ConfigurationsApi->get_config_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->get_config_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**GetConfigCategories200Response**](GetConfigCategories200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of configuration categories |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configs**
> GetConfigs200Response get_configs(take=take, skip=skip, search_col=search_col, search_val=search_val, filter_mode=filter_mode, sort=sort)



Get all the configurations available to the current user.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.get_configs200_response import GetConfigs200Response
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
    api_instance = cyperf.ConfigurationsApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)
    search_col = 'search_col_example' # str | A list of comma-separated columns used to search for the supplied values (optional)
    search_val = 'search_val_example' # str | The keywords used to filter the items (optional)
    filter_mode = 'filter_mode_example' # str | The operator applied to the supplied values (optional)
    sort = 'sort_example' # str | A list of comma-separated field:direction pairs used to sort the items where direction must be asc or dsc (optional)

    try:
        api_response = api_instance.get_configs(take=take, skip=skip, search_col=search_col, search_val=search_val, filter_mode=filter_mode, sort=sort)
        print("The response of ConfigurationsApi->get_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->get_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 
 **search_col** | **str**| A list of comma-separated columns used to search for the supplied values | [optional] 
 **search_val** | **str**| The keywords used to filter the items | [optional] 
 **filter_mode** | **str**| The operator applied to the supplied values | [optional] 
 **sort** | **str**| A list of comma-separated field:direction pairs used to sort the items where direction must be asc or dsc | [optional] 

### Return type

[**GetConfigs200Response**](GetConfigs200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of configurations |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configs_by_id**
> ConfigMetadata get_configs_by_id(config_id, include=include, resolve_dependencies=resolve_dependencies)



Get a particular configuration.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.config_metadata import ConfigMetadata
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
    api_instance = cyperf.ConfigurationsApi(api_client)
    config_id = 'config_id_example' # str | The ID of the config.
    include = 'include_example' # str | Specifies if the sub-fields that are objects should be included (eg. 'configData'). (optional)
    resolve_dependencies = 'resolve_dependencies_example' # str | Specifies if the content of the referenced files (action payloads and TLS files) should be included. (optional)

    try:
        api_response = api_instance.get_configs_by_id(config_id, include=include, resolve_dependencies=resolve_dependencies)
        print("The response of ConfigurationsApi->get_configs_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->get_configs_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The ID of the config. | 
 **include** | **str**| Specifies if the sub-fields that are objects should be included (eg. &#39;configData&#39;). | [optional] 
 **resolve_dependencies** | **str**| Specifies if the content of the referenced files (action payloads and TLS files) should be included. | [optional] 

### Return type

[**ConfigMetadata**](ConfigMetadata.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-zip, application/zip, multipart/form-data

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested configuration |  -  |
**404** | A configuration with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_import_operations**
> GetCustomImportOperations200Response get_custom_import_operations(take=take, skip=skip)



Get all the custom import config operations.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.get_custom_import_operations200_response import GetCustomImportOperations200Response
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
    api_instance = cyperf.ConfigurationsApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.get_custom_import_operations(take=take, skip=skip)
        print("The response of ConfigurationsApi->get_custom_import_operations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->get_custom_import_operations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**GetCustomImportOperations200Response**](GetCustomImportOperations200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of custom import config operations |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_configs**
> patch_configs(config_id, config_metadata=config_metadata)



Update a particular configuration. Only non-null fields are updated.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.config_metadata import ConfigMetadata
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
    api_instance = cyperf.ConfigurationsApi(api_client)
    config_id = 'config_id_example' # str | The ID of the config.
    config_metadata = cyperf.ConfigMetadata() # ConfigMetadata |  (optional)

    try:
        api_instance.patch_configs(config_id, config_metadata=config_metadata)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->patch_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The ID of the config. | 
 **config_metadata** | [**ConfigMetadata**](ConfigMetadata.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The configuration was successfully updated. |  -  |
**404** | A configuration with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poll_configs_batch_delete**
> AsyncContext poll_configs_batch_delete(id)



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
    api_instance = cyperf.ConfigurationsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_configs_batch_delete(id)
        print("The response of ConfigurationsApi->poll_configs_batch_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->poll_configs_batch_delete: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poll_configs_export_all**
> AsyncContext poll_configs_export_all(id)



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
    api_instance = cyperf.ConfigurationsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_configs_export_all(id)
        print("The response of ConfigurationsApi->poll_configs_export_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->poll_configs_export_all: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poll_configs_import**
> AsyncContext poll_configs_import(id)



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
    api_instance = cyperf.ConfigurationsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_configs_import(id)
        print("The response of ConfigurationsApi->poll_configs_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->poll_configs_import: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poll_configs_import_all**
> AsyncContext poll_configs_import_all(id)



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
    api_instance = cyperf.ConfigurationsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_configs_import_all(id)
        print("The response of ConfigurationsApi->poll_configs_import_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->poll_configs_import_all: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_configs_batch_delete**
> AsyncContext start_configs_batch_delete(start_batch_delete_request_inner=start_batch_delete_request_inner)



Remove multiple configurations.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.start_batch_delete_request_inner import StartBatchDeleteRequestInner
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
    api_instance = cyperf.ConfigurationsApi(api_client)
    start_batch_delete_request_inner = [cyperf.StartBatchDeleteRequestInner()] # List[StartBatchDeleteRequestInner] |  (optional)

    try:
        api_response = api_instance.start_configs_batch_delete(start_batch_delete_request_inner=start_batch_delete_request_inner)
        print("The response of ConfigurationsApi->start_configs_batch_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->start_configs_batch_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_batch_delete_request_inner** | [**List[StartBatchDeleteRequestInner]**](StartBatchDeleteRequestInner.md)|  | [optional] 

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

# **start_configs_export_all**
> AsyncContext start_configs_export_all(export_all_operation=export_all_operation)



Export all configurations owned by the current user. Optionally, provide a list of config IDs to export.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.export_all_operation import ExportAllOperation
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
    api_instance = cyperf.ConfigurationsApi(api_client)
    export_all_operation = cyperf.ExportAllOperation() # ExportAllOperation |  (optional)

    try:
        api_response = api_instance.start_configs_export_all(export_all_operation=export_all_operation)
        print("The response of ConfigurationsApi->start_configs_export_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->start_configs_export_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_all_operation** | [**ExportAllOperation**](ExportAllOperation.md)|  | [optional] 

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

# **start_configs_import**
> AsyncContext start_configs_import(body=body)



Import a single configuration from the specified file.

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
    api_instance = cyperf.ConfigurationsApi(api_client)
    body = None # bytearray |  (optional)

    try:
        api_response = api_instance.start_configs_import(body=body)
        print("The response of ConfigurationsApi->start_configs_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->start_configs_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **bytearray**|  | [optional] 

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/x-zip, application/zip, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Details about the operation that just started |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_configs_import_all**
> AsyncContext start_configs_import_all(import_all_operation=import_all_operation)



Import all configurations from the specified file.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.import_all_operation import ImportAllOperation
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
    api_instance = cyperf.ConfigurationsApi(api_client)
    import_all_operation = cyperf.ImportAllOperation() # ImportAllOperation |  (optional)

    try:
        api_response = api_instance.start_configs_import_all(import_all_operation=import_all_operation)
        print("The response of ConfigurationsApi->start_configs_import_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->start_configs_import_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_all_operation** | [**ImportAllOperation**](ImportAllOperation.md)|  | [optional] 

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

# **update_configs**
> ConfigMetadata update_configs(config_id, config_metadata=config_metadata)



Update a particular configuration.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.config_metadata import ConfigMetadata
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
    api_instance = cyperf.ConfigurationsApi(api_client)
    config_id = 'config_id_example' # str | The ID of the config.
    config_metadata = cyperf.ConfigMetadata() # ConfigMetadata |  (optional)

    try:
        api_response = api_instance.update_configs(config_id, config_metadata=config_metadata)
        print("The response of ConfigurationsApi->update_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->update_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The ID of the config. | 
 **config_metadata** | [**ConfigMetadata**](ConfigMetadata.md)|  | [optional] 

### Return type

[**ConfigMetadata**](ConfigMetadata.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated configuration |  -  |
**400** | Bad request |  -  |
**404** | A configuration with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

