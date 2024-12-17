# cyperf.SessionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
l[**add_apps**](SessionsApi.md#add_apps) | **POST** /api/v2/sessions/{sessionId}/config/config/TrafficProfiles/1/operations/add-applications | 
[**add_attacks**](SessionsApi.md#add_attacks) | **POST** /api/v2/sessions/{sessionId}/config/config/AttackProfiles/1/operations/add-attacks | 
[**create_meta**](SessionsApi.md#create_meta) | **POST** /api/v2/sessions/{sessionId}/meta | 
[**create_sessions**](SessionsApi.md#create_sessions) | **POST** /api/v2/sessions | 
[**delete_meta**](SessionsApi.md#delete_meta) | **DELETE** /api/v2/sessions/{sessionId}/meta/{metaId} | 
[**delete_sessions**](SessionsApi.md#delete_sessions) | **DELETE** /api/v2/sessions/{sessionId} | 
[**get_appsec_ui_metadata**](SessionsApi.md#get_appsec_ui_metadata) | **GET** /api/v2/appsec-ui-metadata | 
[**get_config**](SessionsApi.md#get_config) | **GET** /api/v2/sessions/{sessionId}/config | 
[**get_docs**](SessionsApi.md#get_docs) | **GET** /api/v2/sessions/{sessionId}/config/$docs | 
[**get_granular_stats**](SessionsApi.md#get_granular_stats) | **GET** /api/v2/sessions/{sessionId}/config/granular-stats | 
[**get_granular_stats_filters**](SessionsApi.md#get_granular_stats_filters) | **GET** /api/v2/sessions/{sessionId}/config/granular-stats-filters | 
[**get_meta**](SessionsApi.md#get_meta) | **GET** /api/v2/sessions/{sessionId}/meta | 
[**get_meta_by_id**](SessionsApi.md#get_meta_by_id) | **GET** /api/v2/sessions/{sessionId}/meta/{metaId} | 
[**get_sessions**](SessionsApi.md#get_sessions) | **GET** /api/v2/sessions | 
[**get_sessions_by_id**](SessionsApi.md#get_sessions_by_id) | **GET** /api/v2/sessions/{sessionId} | 
[**get_test**](SessionsApi.md#get_test) | **GET** /api/v2/sessions/{sessionId}/test | 
[**patch_meta**](SessionsApi.md#patch_meta) | **PATCH** /api/v2/sessions/{sessionId}/meta/{metaId} | 
[**patch_sessions**](SessionsApi.md#patch_sessions) | **PATCH** /api/v2/sessions/{sessionId} | 
[**patch_test**](SessionsApi.md#patch_test) | **PATCH** /api/v2/sessions/{sessionId}/test | 
[**poll_config_add_applications**](SessionsApi.md#poll_config_add_applications) | **GET** /api/v2/sessions/{sessionId}/config/config/TrafficProfiles/{trafficProfileId}/operations/add-applications/{id} | 
[**poll_config_granular_stats_default_dashboards**](SessionsApi.md#poll_config_granular_stats_default_dashboards) | **GET** /api/v2/sessions/{sessionId}/config/operations/granular-stats-default-dashboards/{id} | 
[**poll_config_save**](SessionsApi.md#poll_config_save) | **GET** /api/v2/sessions/{sessionId}/config/operations/save/{id} | 
[**poll_prepare_test**](SessionsApi.md#poll_prepare_test) | **GET** /api/v2/sessions/{sessionId}/operations/prepareTest/{id} | 
[**poll_sessions_batch_delete**](SessionsApi.md#poll_sessions_batch_delete) | **GET** /api/v2/sessions/operations/batch-delete/{id} | 
[**poll_sessions_load_config**](SessionsApi.md#poll_sessions_load_config) | **GET** /api/v2/sessions/{sessionId}/operations/loadConfig/{id} | 
[**poll_sessions_touch**](SessionsApi.md#poll_sessions_touch) | **GET** /api/v2/sessions/{sessionId}/operations/touch/{id} | 
[**poll_test_end**](SessionsApi.md#poll_test_end) | **GET** /api/v2/sessions/{sessionId}/operations/testEnd/{id} | 
[**poll_test_init**](SessionsApi.md#poll_test_init) | **GET** /api/v2/sessions/{sessionId}/operations/testInit/{id} | 
[**start_config_add_applications**](SessionsApi.md#start_config_add_applications) | **POST** /api/v2/sessions/{sessionId}/config/config/TrafficProfiles/{trafficProfileId}/operations/add-applications | 
[**start_config_granular_stats_default_dashboards**](SessionsApi.md#start_config_granular_stats_default_dashboards) | **POST** /api/v2/sessions/{sessionId}/config/operations/granular-stats-default-dashboards | 
[**start_config_save**](SessionsApi.md#start_config_save) | **POST** /api/v2/sessions/{sessionId}/config/operations/save | 
[**start_prepare_test**](SessionsApi.md#start_prepare_test) | **POST** /api/v2/sessions/{sessionId}/operations/prepareTest | 
[**start_sessions_batch_delete**](SessionsApi.md#start_sessions_batch_delete) | **POST** /api/v2/sessions/operations/batch-delete | 
[**start_sessions_load_config**](SessionsApi.md#start_sessions_load_config) | **POST** /api/v2/sessions/{sessionId}/operations/loadConfig | 
[**start_sessions_touch**](SessionsApi.md#start_sessions_touch) | **POST** /api/v2/sessions/{sessionId}/operations/touch | 
[**start_test_end**](SessionsApi.md#start_test_end) | **POST** /api/v2/sessions/{sessionId}/operations/testEnd | 
[**start_test_init**](SessionsApi.md#start_test_init) | **POST** /api/v2/sessions/{sessionId}/operations/testInit | 
[**update_config**](SessionsApi.md#update_config) | **PUT** /api/v2/sessions/{sessionId}/config | 
[**update_meta**](SessionsApi.md#update_meta) | **PUT** /api/v2/sessions/{sessionId}/meta | 
[**update_sessions**](SessionsApi.md#update_sessions) | **PUT** /api/v2/sessions/{sessionId} | 
[**update_test**](SessionsApi.md#update_test) | **PUT** /api/v2/sessions/{sessionId}/test | 


# **add_apps**
> AsyncContext add_apps(session_id, external_resource_info=external_resource_info)



Start add-applications in traffic profile.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.external_resource_info import ExternalResourceInfo
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    external_resource_info = [cyperf.ExternalResourceInfo()] # List[ExternalResourceInfo] |  (optional)

    try:
        api_response = api_instance.add_apps(session_id, external_resource_info=external_resource_info)
        print("The response of SessionsApi->add_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->add_apps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **external_resource_info** | [**List[ExternalResourceInfo]**](ExternalResourceInfo.md)|  | [optional] 

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

# **add_attacks**
> AsyncContext add_attacks(session_id, external_resource_info=external_resource_info)



Start add-attacks in attack profile.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.external_resource_info import ExternalResourceInfo
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    external_resource_info = [cyperf.ExternalResourceInfo()] # List[ExternalResourceInfo] |  (optional)

    try:
        api_response = api_instance.add_attacks(session_id, external_resource_info=external_resource_info)
        print("The response of SessionsApi->add_attacks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->add_attacks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **external_resource_info** | [**List[ExternalResourceInfo]**](ExternalResourceInfo.md)|  | [optional] 

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

# **create_meta**
> List[Pair] create_meta(session_id, pair=pair)



Create a new session metadata.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.pair import Pair
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    pair = [cyperf.Pair()] # List[Pair] |  (optional)

    try:
        api_response = api_instance.create_meta(session_id, pair=pair)
        print("The response of SessionsApi->create_meta:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->create_meta: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **pair** | [**List[Pair]**](Pair.md)|  | [optional] 

### Return type

[**List[Pair]**](Pair.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Session metadata created successfully. |  -  |
**400** | Bad request |  -  |
**404** | A session with the specified ID was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sessions**
> List[Session] create_sessions(session=session)



Create a new session by providing the URL of the configuration to be loaded.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.session import Session
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session = [cyperf.Session()] # List[Session] |  (optional)

    try:
        api_response = api_instance.create_sessions(session=session)
        print("The response of SessionsApi->create_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->create_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session** | [**List[Session]**](Session.md)|  | [optional] 

### Return type

[**List[Session]**](Session.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Session created successfully. |  -  |
**400** | Bad request |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_meta**
> delete_meta(session_id, meta_id)



Delete a particular session metadata pair.

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    meta_id = 'meta_id_example' # str | The ID of the meta.

    try:
        api_instance.delete_meta(session_id, meta_id)
    except Exception as e:
        print("Exception when calling SessionsApi->delete_meta: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **meta_id** | **str**| The ID of the meta. | 

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
**204** | The session metadata was successfully deleted. |  -  |
**400** | Bad request |  -  |
**404** | A session or metadata with the specified IDs were not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sessions**
> delete_sessions(session_id)



Delete a particular session.

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.

    try:
        api_instance.delete_sessions(session_id)
    except Exception as e:
        print("Exception when calling SessionsApi->delete_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 

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
**204** | The session was successfully deleted. |  -  |
**400** | Bad request |  -  |
**403** | The initiator of the request does not have enough privileges to perform the action. |  -  |
**404** | A session with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appsec_ui_metadata**
> object get_appsec_ui_metadata()



Get the UI metadata

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)

    try:
        api_response = api_instance.get_appsec_ui_metadata()
        print("The response of SessionsApi->get_appsec_ui_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->get_appsec_ui_metadata: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The UI metadata |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config**
> AppsecConfig get_config(session_id, include=include)



Get the current session's configuration.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.appsec_config import AppsecConfig
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    include = 'include_example' # str | Specifies if the sub-fields that are objects should be included (eg. 'Config'). (optional)

    try:
        api_response = api_instance.get_config(session_id, include=include)
        print("The response of SessionsApi->get_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->get_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **include** | **str**| Specifies if the sub-fields that are objects should be included (eg. &#39;Config&#39;). | [optional] 

### Return type

[**AppsecConfig**](AppsecConfig.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current session&#39;s configuration |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_docs**
> OpenAPIDefinitions get_docs(session_id)



Get the OpenAPI definitions for CyPerf data model.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.open_api_definitions import OpenAPIDefinitions
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.

    try:
        api_response = api_instance.get_docs(session_id)
        print("The response of SessionsApi->get_docs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->get_docs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 

### Return type

[**OpenAPIDefinitions**](OpenAPIDefinitions.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The OpenAPI definitions for CyPerf data model |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_granular_stats**
> object get_granular_stats(session_id)



Get granular statistics based on the session configuration.

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.

    try:
        api_response = api_instance.get_granular_stats(session_id)
        print("The response of SessionsApi->get_granular_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->get_granular_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested granular statistics |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_granular_stats_filters**
> object get_granular_stats_filters(session_id)



Get the filters for the granular statistics based on the session configuration.

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.

    try:
        api_response = api_instance.get_granular_stats_filters(session_id)
        print("The response of SessionsApi->get_granular_stats_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->get_granular_stats_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested filters for the granular statistics |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_meta**
> GetMeta200Response get_meta(session_id, take=take, skip=skip)



Get the metadata of a particular session.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.get_meta200_response import GetMeta200Response
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.get_meta(session_id, take=take, skip=skip)
        print("The response of SessionsApi->get_meta:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->get_meta: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**GetMeta200Response**](GetMeta200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested session metadata |  -  |
**404** | A session with the specified ID was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_meta_by_id**
> Pair get_meta_by_id(session_id, meta_id)



Get a particular session metadata pair.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.pair import Pair
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    meta_id = 'meta_id_example' # str | The ID of the meta.

    try:
        api_response = api_instance.get_meta_by_id(session_id, meta_id)
        print("The response of SessionsApi->get_meta_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->get_meta_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **meta_id** | **str**| The ID of the meta. | 

### Return type

[**Pair**](Pair.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested session metadata pair |  -  |
**404** | A session or metadata with the specified IDs were not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sessions**
> GetSessions200Response get_sessions(take=take, skip=skip, search_col=search_col, search_val=search_val, filter_mode=filter_mode, sort=sort, include=include)



List all the sessions.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.get_sessions200_response import GetSessions200Response
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)
    search_col = 'search_col_example' # str | A list of comma-separated columns used to search for the supplied values (optional)
    search_val = 'search_val_example' # str | The keywords used to filter the items (optional)
    filter_mode = 'filter_mode_example' # str | The operator applied to the supplied values (optional)
    sort = 'sort_example' # str | A list of comma-separated field:direction pairs used to sort the items where direction must be asc or dsc (optional)
    include = 'include_example' # str | Specifies if the sub-fields that are objects should be included. (optional)

    try:
        api_response = api_instance.get_sessions(take=take, skip=skip, search_col=search_col, search_val=search_val, filter_mode=filter_mode, sort=sort, include=include)
        print("The response of SessionsApi->get_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->get_sessions: %s\n" % e)
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
 **include** | **str**| Specifies if the sub-fields that are objects should be included. | [optional] 

### Return type

[**GetSessions200Response**](GetSessions200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of available sessions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sessions_by_id**
> Session get_sessions_by_id(session_id, include=include)



Get a particular session.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.session import Session
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    include = 'include_example' # str | Specifies if the sub-fields that are objects should be included (eg. test). (optional)

    try:
        api_response = api_instance.get_sessions_by_id(session_id, include=include)
        print("The response of SessionsApi->get_sessions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->get_sessions_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **include** | **str**| Specifies if the sub-fields that are objects should be included (eg. test). | [optional] 

### Return type

[**Session**](Session.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested session |  -  |
**404** | A session with the specified ID was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test**
> TestInfo get_test(session_id)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.test_info import TestInfo
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.

    try:
        api_response = api_instance.get_test(session_id)
        print("The response of SessionsApi->get_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->get_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 

### Return type

[**TestInfo**](TestInfo.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_meta**
> patch_meta(session_id, meta_id, pair=pair)



Update a particular session metadata pair. Only non-null fields are updated.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.pair import Pair
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    meta_id = 'meta_id_example' # str | The ID of the meta.
    pair = cyperf.Pair() # Pair |  (optional)

    try:
        api_instance.patch_meta(session_id, meta_id, pair=pair)
    except Exception as e:
        print("Exception when calling SessionsApi->patch_meta: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **meta_id** | **str**| The ID of the meta. | 
 **pair** | [**Pair**](Pair.md)|  | [optional] 

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
**204** | The session metadata pair was successfully updated. |  -  |
**400** | Bad request |  -  |
**404** | A session or metadata with the specified IDs were not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sessions**
> patch_sessions(session_id, session=session)



Update a particular session. Only non-null fields are updated.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.session import Session
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    session = cyperf.Session() # Session |  (optional)

    try:
        api_instance.patch_sessions(session_id, session=session)
    except Exception as e:
        print("Exception when calling SessionsApi->patch_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **session** | [**Session**](Session.md)|  | [optional] 

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
**204** | The session was successfully updated. |  -  |
**404** | A session with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_test**
> patch_test(session_id, test_info=test_info)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.test_info import TestInfo
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    test_info = cyperf.TestInfo() # TestInfo |  (optional)

    try:
        api_instance.patch_test(session_id, test_info=test_info)
    except Exception as e:
        print("Exception when calling SessionsApi->patch_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **test_info** | [**TestInfo**](TestInfo.md)|  | [optional] 

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
**204** | The request was completed successfully. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poll_config_add_applications**
> AsyncContext poll_config_add_applications(session_id, traffic_profile_id, id)



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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    traffic_profile_id = 'traffic_profile_id_example' # str | The ID of the traffic profile.
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_config_add_applications(session_id, traffic_profile_id, id)
        print("The response of SessionsApi->poll_config_add_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->poll_config_add_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **traffic_profile_id** | **str**| The ID of the traffic profile. | 
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

# **poll_config_granular_stats_default_dashboards**
> AsyncContext poll_config_granular_stats_default_dashboards(session_id, id)



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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_config_granular_stats_default_dashboards(session_id, id)
        print("The response of SessionsApi->poll_config_granular_stats_default_dashboards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->poll_config_granular_stats_default_dashboards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
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

# **poll_config_save**
> AsyncContext poll_config_save(session_id, id)



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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_config_save(session_id, id)
        print("The response of SessionsApi->poll_config_save:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->poll_config_save: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
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

# **poll_prepare_test**
> AsyncContext poll_prepare_test(session_id, id)



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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_prepare_test(session_id, id)
        print("The response of SessionsApi->poll_prepare_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->poll_prepare_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
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

# **poll_sessions_batch_delete**
> AsyncContext poll_sessions_batch_delete(id)



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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_sessions_batch_delete(id)
        print("The response of SessionsApi->poll_sessions_batch_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->poll_sessions_batch_delete: %s\n" % e)
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

# **poll_sessions_load_config**
> AsyncContext poll_sessions_load_config(session_id, id)



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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_sessions_load_config(session_id, id)
        print("The response of SessionsApi->poll_sessions_load_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->poll_sessions_load_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
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

# **poll_sessions_touch**
> AsyncContext poll_sessions_touch(session_id, id)



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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_sessions_touch(session_id, id)
        print("The response of SessionsApi->poll_sessions_touch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->poll_sessions_touch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
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

# **poll_test_end**
> AsyncContext poll_test_end(session_id, id)



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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_test_end(session_id, id)
        print("The response of SessionsApi->poll_test_end:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->poll_test_end: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
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

# **poll_test_init**
> AsyncContext poll_test_init(session_id, id)



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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_test_init(session_id, id)
        print("The response of SessionsApi->poll_test_init:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->poll_test_init: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
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

# **start_config_add_applications**
> AsyncContext start_config_add_applications(session_id, traffic_profile_id, external_resource_info=external_resource_info)



Add applications in the traffic profile of the current session.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.external_resource_info import ExternalResourceInfo
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    traffic_profile_id = 'traffic_profile_id_example' # str | The ID of the traffic profile.
    external_resource_info = [cyperf.ExternalResourceInfo()] # List[ExternalResourceInfo] |  (optional)

    try:
        api_response = api_instance.start_config_add_applications(session_id, traffic_profile_id, external_resource_info=external_resource_info)
        print("The response of SessionsApi->start_config_add_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->start_config_add_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **traffic_profile_id** | **str**| The ID of the traffic profile. | 
 **external_resource_info** | [**List[ExternalResourceInfo]**](ExternalResourceInfo.md)|  | [optional] 

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

# **start_config_granular_stats_default_dashboards**
> AsyncContext start_config_granular_stats_default_dashboards(session_id)



Create granular statistics dashboards based on the session configuration.

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.

    try:
        api_response = api_instance.start_config_granular_stats_default_dashboards(session_id)
        print("The response of SessionsApi->start_config_granular_stats_default_dashboards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->start_config_granular_stats_default_dashboards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 

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

# **start_config_save**
> AsyncContext start_config_save(session_id, save_config_operation=save_config_operation)



Save the configuration of the current session using the specified name.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.save_config_operation import SaveConfigOperation
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    save_config_operation = cyperf.SaveConfigOperation() # SaveConfigOperation |  (optional)

    try:
        api_response = api_instance.start_config_save(session_id, save_config_operation=save_config_operation)
        print("The response of SessionsApi->start_config_save:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->start_config_save: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **save_config_operation** | [**SaveConfigOperation**](SaveConfigOperation.md)|  | [optional] 

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

# **start_prepare_test**
> AsyncContext start_prepare_test(session_id, prepare_test_operation=prepare_test_operation)



This operation returns the config processed as agent messages and any data necessary for UI and REST stats

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.prepare_test_operation import PrepareTestOperation
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    prepare_test_operation = [cyperf.PrepareTestOperation()] # List[PrepareTestOperation] |  (optional)

    try:
        api_response = api_instance.start_prepare_test(session_id, prepare_test_operation=prepare_test_operation)
        print("The response of SessionsApi->start_prepare_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->start_prepare_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **prepare_test_operation** | [**List[PrepareTestOperation]**](PrepareTestOperation.md)|  | [optional] 

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

# **start_sessions_batch_delete**
> AsyncContext start_sessions_batch_delete(start_batch_delete_request_inner=start_batch_delete_request_inner)



Remove multiple sessions.

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    start_batch_delete_request_inner = cyperf.StartBatchDeleteRequestInner() # StartBatchDeleteRequestInner |  (optional)

    try:
        api_response = api_instance.start_sessions_batch_delete(start_batch_delete_request_inner=start_batch_delete_request_inner)
        print("The response of SessionsApi->start_sessions_batch_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->start_sessions_batch_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_batch_delete_request_inner** | [**StartBatchDeleteRequestInner**](StartBatchDeleteRequestInner.md)|  | [optional] 

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

# **start_sessions_load_config**
> AsyncContext start_sessions_load_config(session_id, load_config_operation=load_config_operation)



Load a new test in the current session.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.load_config_operation import LoadConfigOperation
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    load_config_operation = cyperf.LoadConfigOperation() # LoadConfigOperation |  (optional)

    try:
        api_response = api_instance.start_sessions_load_config(session_id, load_config_operation=load_config_operation)
        print("The response of SessionsApi->start_sessions_load_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->start_sessions_load_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **load_config_operation** | [**LoadConfigOperation**](LoadConfigOperation.md)|  | [optional] 

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

# **start_sessions_touch**
> AsyncContext start_sessions_touch(session_id, start_batch_delete_request_inner=start_batch_delete_request_inner)



Update last visited field when session is touched.

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    start_batch_delete_request_inner = cyperf.StartBatchDeleteRequestInner() # StartBatchDeleteRequestInner |  (optional)

    try:
        api_response = api_instance.start_sessions_touch(session_id, start_batch_delete_request_inner=start_batch_delete_request_inner)
        print("The response of SessionsApi->start_sessions_touch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->start_sessions_touch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **start_batch_delete_request_inner** | [**StartBatchDeleteRequestInner**](StartBatchDeleteRequestInner.md)|  | [optional] 

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

# **start_test_end**
> AsyncContext start_test_end(session_id, test_state_changed_operation=test_state_changed_operation)



This is called from traffic controller to notify that a test has ended. It should return any information needed by the traffic controller to completely clean up the test.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.test_state_changed_operation import TestStateChangedOperation
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    test_state_changed_operation = [cyperf.TestStateChangedOperation()] # List[TestStateChangedOperation] |  (optional)

    try:
        api_response = api_instance.start_test_end(session_id, test_state_changed_operation=test_state_changed_operation)
        print("The response of SessionsApi->start_test_end:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->start_test_end: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **test_state_changed_operation** | [**List[TestStateChangedOperation]**](TestStateChangedOperation.md)|  | [optional] 

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

# **start_test_init**
> AsyncContext start_test_init(session_id, test_state_changed_operation=test_state_changed_operation)



This is called from traffic controller to notify that a new test is starting. It should return all the information needed by the traffic controller to start the test.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.test_state_changed_operation import TestStateChangedOperation
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    test_state_changed_operation = [cyperf.TestStateChangedOperation()] # List[TestStateChangedOperation] |  (optional)

    try:
        api_response = api_instance.start_test_init(session_id, test_state_changed_operation=test_state_changed_operation)
        print("The response of SessionsApi->start_test_init:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->start_test_init: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **test_state_changed_operation** | [**List[TestStateChangedOperation]**](TestStateChangedOperation.md)|  | [optional] 

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

# **update_config**
> AppsecConfig update_config(session_id, appsec_config=appsec_config)



Update the current session's configuration.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.appsec_config import AppsecConfig
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    appsec_config = cyperf.AppsecConfig() # AppsecConfig |  (optional)

    try:
        api_response = api_instance.update_config(session_id, appsec_config=appsec_config)
        print("The response of SessionsApi->update_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->update_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **appsec_config** | [**AppsecConfig**](AppsecConfig.md)|  | [optional] 

### Return type

[**AppsecConfig**](AppsecConfig.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated configuration |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_meta**
> List[Pair] update_meta(session_id, pair=pair)



Update the session metadata.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.pair import Pair
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    pair = [cyperf.Pair()] # List[Pair] |  (optional)

    try:
        api_response = api_instance.update_meta(session_id, pair=pair)
        print("The response of SessionsApi->update_meta:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->update_meta: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **pair** | [**List[Pair]**](Pair.md)|  | [optional] 

### Return type

[**List[Pair]**](Pair.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated session metadata |  -  |
**404** | A session with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sessions**
> Session update_sessions(session_id, session=session)



Update a particular session.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.session import Session
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    session = cyperf.Session() # Session |  (optional)

    try:
        api_response = api_instance.update_sessions(session_id, session=session)
        print("The response of SessionsApi->update_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->update_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **session** | [**Session**](Session.md)|  | [optional] 

### Return type

[**Session**](Session.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated session |  -  |
**400** | Bad request |  -  |
**404** | A session with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_test**
> TestInfo update_test(session_id, test_info=test_info)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.test_info import TestInfo
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.SessionsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    test_info = cyperf.TestInfo() # TestInfo |  (optional)

    try:
        api_response = api_instance.update_test(session_id, test_info=test_info)
        print("The response of SessionsApi->update_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->update_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **test_info** | [**TestInfo**](TestInfo.md)|  | [optional] 

### Return type

[**TestInfo**](TestInfo.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

