# cyperf.DashboardsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_stats_dashboard_changes**](DashboardsApi.md#create_stats_dashboard_changes) | **POST** /api/v2/stats-dashboards/{statsDashboardId}/changes | 
[**create_stats_dashboards**](DashboardsApi.md#create_stats_dashboards) | **POST** /api/v2/stats-dashboards | 
[**delete_stats_dashboard**](DashboardsApi.md#delete_stats_dashboard) | **DELETE** /api/v2/stats-dashboards/{statsDashboardId} | 
[**get_stats_dashboard_by_id**](DashboardsApi.md#get_stats_dashboard_by_id) | **GET** /api/v2/stats-dashboards/{statsDashboardId} | 
[**get_stats_dashboard_changes**](DashboardsApi.md#get_stats_dashboard_changes) | **GET** /api/v2/stats-dashboards/{statsDashboardId}/changes | 
[**get_stats_dashboard_metrics**](DashboardsApi.md#get_stats_dashboard_metrics) | **GET** /api/v2/stats-dashboards/{statsDashboardId}/metrics | 
[**get_stats_dashboards**](DashboardsApi.md#get_stats_dashboards) | **GET** /api/v2/stats-dashboards | 
[**start_stats_dashboards_convert**](DashboardsApi.md#start_stats_dashboards_convert) | **POST** /api/v2/stats-dashboards/operations/convert | 
[**update_stats_dashboard**](DashboardsApi.md#update_stats_dashboard) | **PUT** /api/v2/stats-dashboards/{statsDashboardId} | 


# **create_stats_dashboard_changes**
> List[ChangeEvent] create_stats_dashboard_changes(stats_dashboard_id, stats_dashboard_changes=stats_dashboard_changes)



Register a change event.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.change_event import ChangeEvent
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
    api_instance = cyperf.DashboardsApi(api_client)
    stats_dashboard_id = 'stats_dashboard_id_example' # str | The ID of the stats dashboard.
    stats_dashboard_changes = [cyperf.ChangeEvent()] # List[ChangeEvent] |  (optional)

    try:
        api_response = api_instance.create_stats_dashboard_changes(stats_dashboard_id, stats_dashboard_changes=stats_dashboard_changes)
        print("The response of DashboardsApi->create_stats_dashboard_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsApi->create_stats_dashboard_changes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stats_dashboard_id** | **str**| The ID of the stats dashboard. | 
 **stats_dashboard_changes** | [**List[ChangeEvent]**](ChangeEvent.md)|  | [optional] 

### Return type

[**List[ChangeEvent]**](ChangeEvent.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The change event was successfully registered. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_stats_dashboards**
> List[StatsDashboard] create_stats_dashboards(stats_dashboards=stats_dashboards)



Add a new dashboard.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.stats_dashboard import StatsDashboard
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
    api_instance = cyperf.DashboardsApi(api_client)
    stats_dashboards = [cyperf.StatsDashboard()] # List[StatsDashboard] |  (optional)

    try:
        api_response = api_instance.create_stats_dashboards(stats_dashboards=stats_dashboards)
        print("The response of DashboardsApi->create_stats_dashboards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsApi->create_stats_dashboards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stats_dashboards** | [**List[StatsDashboard]**](StatsDashboard.md)|  | [optional] 

### Return type

[**List[StatsDashboard]**](StatsDashboard.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The dashboard was successfully added. |  -  |
**409** | The request could not be completed due to a conflict with the current state of the target resource. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_stats_dashboard**
> delete_stats_dashboard(stats_dashboard_id)



Delete a particular dashboard.

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
    api_instance = cyperf.DashboardsApi(api_client)
    stats_dashboard_id = 'stats_dashboard_id_example' # str | The ID of the stats dashboard.

    try:
        api_instance.delete_stats_dashboard(stats_dashboard_id)
    except Exception as e:
        print("Exception when calling DashboardsApi->delete_stats_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stats_dashboard_id** | **str**| The ID of the stats dashboard. | 

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
**204** | The dashboard was successfully deleted. |  -  |
**403** | The initiator of the request does not have enough privileges to perform the action. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stats_dashboard_by_id**
> StatsDashboard get_stats_dashboard_by_id(stats_dashboard_id)



Get a particular dashboard.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.stats_dashboard import StatsDashboard
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
    api_instance = cyperf.DashboardsApi(api_client)
    stats_dashboard_id = 'stats_dashboard_id_example' # str | The ID of the stats dashboard.

    try:
        api_response = api_instance.get_stats_dashboard_by_id(stats_dashboard_id)
        print("The response of DashboardsApi->get_stats_dashboard_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsApi->get_stats_dashboard_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stats_dashboard_id** | **str**| The ID of the stats dashboard. | 

### Return type

[**StatsDashboard**](StatsDashboard.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested dashboard |  -  |
**403** | The initiator of the request does not have enough privileges to perform the action. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stats_dashboard_changes**
> GetStatsDashboardChanges200Response get_stats_dashboard_changes(stats_dashboard_id, take=take, skip=skip)



Get the list of change events.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.get_stats_dashboard_changes200_response import GetStatsDashboardChanges200Response
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
    api_instance = cyperf.DashboardsApi(api_client)
    stats_dashboard_id = 'stats_dashboard_id_example' # str | The ID of the stats dashboard.
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.get_stats_dashboard_changes(stats_dashboard_id, take=take, skip=skip)
        print("The response of DashboardsApi->get_stats_dashboard_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsApi->get_stats_dashboard_changes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stats_dashboard_id** | **str**| The ID of the stats dashboard. | 
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**GetStatsDashboardChanges200Response**](GetStatsDashboardChanges200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of change events. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stats_dashboard_metrics**
> MetricsList get_stats_dashboard_metrics(stats_dashboard_id)



Get the list of metrics.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.metrics_list import MetricsList
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
    api_instance = cyperf.DashboardsApi(api_client)
    stats_dashboard_id = 'stats_dashboard_id_example' # str | The ID of the stats dashboard.

    try:
        api_response = api_instance.get_stats_dashboard_metrics(stats_dashboard_id)
        print("The response of DashboardsApi->get_stats_dashboard_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsApi->get_stats_dashboard_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stats_dashboard_id** | **str**| The ID of the stats dashboard. | 

### Return type

[**MetricsList**](MetricsList.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested metrics |  -  |
**403** | The initiator of the request does not have enough privileges to perform the action. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stats_dashboards**
> GetStatsDashboards200Response get_stats_dashboards(take=take, skip=skip)



Get all the dashboards.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.get_stats_dashboards200_response import GetStatsDashboards200Response
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
    api_instance = cyperf.DashboardsApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.get_stats_dashboards(take=take, skip=skip)
        print("The response of DashboardsApi->get_stats_dashboards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsApi->get_stats_dashboards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**GetStatsDashboards200Response**](GetStatsDashboards200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of available dashboards |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_stats_dashboards_convert**
> AsyncContext start_stats_dashboards_convert(convert_dashboards_operation=convert_dashboards_operation)



Converts dashboards to specified types of results.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.convert_dashboards_operation import ConvertDashboardsOperation
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
    api_instance = cyperf.DashboardsApi(api_client)
    convert_dashboards_operation = cyperf.ConvertDashboardsOperation() # ConvertDashboardsOperation |  (optional)

    try:
        api_response = api_instance.start_stats_dashboards_convert(convert_dashboards_operation=convert_dashboards_operation)
        print("The response of DashboardsApi->start_stats_dashboards_convert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsApi->start_stats_dashboards_convert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **convert_dashboards_operation** | [**ConvertDashboardsOperation**](ConvertDashboardsOperation.md)|  | [optional] 

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

# **update_stats_dashboard**
> StatsDashboard update_stats_dashboard(stats_dashboard_id, stats_dashboard=stats_dashboard)



Update a dashboard.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.stats_dashboard import StatsDashboard
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
    api_instance = cyperf.DashboardsApi(api_client)
    stats_dashboard_id = 'stats_dashboard_id_example' # str | The ID of the stats dashboard.
    stats_dashboard = cyperf.StatsDashboard() # StatsDashboard |  (optional)

    try:
        api_response = api_instance.update_stats_dashboard(stats_dashboard_id, stats_dashboard=stats_dashboard)
        print("The response of DashboardsApi->update_stats_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsApi->update_stats_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stats_dashboard_id** | **str**| The ID of the stats dashboard. | 
 **stats_dashboard** | [**StatsDashboard**](StatsDashboard.md)|  | [optional] 

### Return type

[**StatsDashboard**](StatsDashboard.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated dashboard |  -  |
**403** | The initiator of the request does not have enough privileges to perform the action. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

