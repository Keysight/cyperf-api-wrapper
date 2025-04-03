# cyperf.NotificationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_notifications**](NotificationsApi.md#delete_notifications) | **DELETE** /api/v2/notifications/{notificationId} | 
[**get_notification_counts**](NotificationsApi.md#get_notification_counts) | **GET** /api/v2/notification-counts | 
[**get_notifications**](NotificationsApi.md#get_notifications) | **GET** /api/v2/notifications | 
[**get_notifications_by_id**](NotificationsApi.md#get_notifications_by_id) | **GET** /api/v2/notifications/{notificationId} | 
[**poll_notifications_cleanup**](NotificationsApi.md#poll_notifications_cleanup) | **GET** /api/v2/notifications/operations/cleanup/{id} | 
[**poll_notifications_dismiss**](NotificationsApi.md#poll_notifications_dismiss) | **GET** /api/v2/notifications/operations/dismiss/{id} | 
[**start_notifications_cleanup**](NotificationsApi.md#start_notifications_cleanup) | **POST** /api/v2/notifications/operations/cleanup | 
[**start_notifications_dismiss**](NotificationsApi.md#start_notifications_dismiss) | **POST** /api/v2/notifications/operations/dismiss | 


# **delete_notifications**
> delete_notifications(notification_id)



Delete an existing notification.

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
    api_instance = cyperf.NotificationsApi(api_client)
    notification_id = 'notification_id_example' # str | The ID of the notification.

    try:
        api_instance.delete_notifications(notification_id)
    except Exception as e:
        print("Exception when calling NotificationsApi->delete_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**| The ID of the notification. | 

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
**204** | The notification was successfully deleted. |  -  |
**400** | Bad request |  -  |
**403** | The initiator of the request does not have enough privileges to perform the action. |  -  |
**404** | A notification with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_counts**
> NotificationCounts get_notification_counts(notification_id=notification_id, after_id=after_id, var_from=var_from, to=to, severity=severity, session_id=session_id, test_id=test_id, custom_tags=custom_tags, owner_id=owner_id, owner=owner, include_seen=include_seen, order=order, search=search)



Get the number of notifications that match the query.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.notification_counts import NotificationCounts
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
    api_instance = cyperf.NotificationsApi(api_client)
    notification_id = 'notification_id_example' # str |  (optional)
    after_id = 'after_id_example' # str |  (optional)
    var_from = 56 # int |  (optional)
    to = 56 # int |  (optional)
    severity = 'severity_example' # str |  (optional)
    session_id = 'session_id_example' # str |  (optional)
    test_id = 'test_id_example' # str |  (optional)
    custom_tags = 'custom_tags_example' # str |  (optional)
    owner_id = 'owner_id_example' # str |  (optional)
    owner = 'owner_example' # str |  (optional)
    include_seen = True # bool |  (optional)
    order = 'order_example' # str |  (optional)
    search = 'search_example' # str |  (optional)

    try:
        api_response = api_instance.get_notification_counts(notification_id=notification_id, after_id=after_id, var_from=var_from, to=to, severity=severity, session_id=session_id, test_id=test_id, custom_tags=custom_tags, owner_id=owner_id, owner=owner, include_seen=include_seen, order=order, search=search)
        print("The response of NotificationsApi->get_notification_counts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->get_notification_counts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**|  | [optional] 
 **after_id** | **str**|  | [optional] 
 **var_from** | **int**|  | [optional] 
 **to** | **int**|  | [optional] 
 **severity** | **str**|  | [optional] 
 **session_id** | **str**|  | [optional] 
 **test_id** | **str**|  | [optional] 
 **custom_tags** | **str**|  | [optional] 
 **owner_id** | **str**|  | [optional] 
 **owner** | **str**|  | [optional] 
 **include_seen** | **bool**|  | [optional] 
 **order** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 

### Return type

[**NotificationCounts**](NotificationCounts.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The number of notifications, aggregated by their severity |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notifications**
> GetNotifications200Response get_notifications(take=take, skip=skip, after_id=after_id, var_from=var_from, to=to, severity=severity, session_id=session_id, test_id=test_id, custom_tags=custom_tags, owner_id=owner_id, owner=owner, include_seen=include_seen, sticky=sticky, order=order, search=search)



Get all the notifications that match the query.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.get_notifications200_response import GetNotifications200Response
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
    api_instance = cyperf.NotificationsApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)
    after_id = 'after_id_example' # str |  (optional)
    var_from = 56 # int |  (optional)
    to = 56 # int |  (optional)
    severity = 'severity_example' # str |  (optional)
    session_id = 'session_id_example' # str |  (optional)
    test_id = 'test_id_example' # str |  (optional)
    custom_tags = 'custom_tags_example' # str |  (optional)
    owner_id = 'owner_id_example' # str |  (optional)
    owner = 'owner_example' # str |  (optional)
    include_seen = True # bool |  (optional)
    sticky = True # bool |  (optional)
    order = 'order_example' # str |  (optional)
    search = 'search_example' # str |  (optional)

    try:
        api_response = api_instance.get_notifications(take=take, skip=skip, after_id=after_id, var_from=var_from, to=to, severity=severity, session_id=session_id, test_id=test_id, custom_tags=custom_tags, owner_id=owner_id, owner=owner, include_seen=include_seen, sticky=sticky, order=order, search=search)
        print("The response of NotificationsApi->get_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->get_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 
 **after_id** | **str**|  | [optional] 
 **var_from** | **int**|  | [optional] 
 **to** | **int**|  | [optional] 
 **severity** | **str**|  | [optional] 
 **session_id** | **str**|  | [optional] 
 **test_id** | **str**|  | [optional] 
 **custom_tags** | **str**|  | [optional] 
 **owner_id** | **str**|  | [optional] 
 **owner** | **str**|  | [optional] 
 **include_seen** | **bool**|  | [optional] 
 **sticky** | **bool**|  | [optional] 
 **order** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 

### Return type

[**GetNotifications200Response**](GetNotifications200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of notifications that match the query |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notifications_by_id**
> Notification get_notifications_by_id(notification_id)



Get a particular notification.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.notification import Notification
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
    api_instance = cyperf.NotificationsApi(api_client)
    notification_id = 'notification_id_example' # str | The ID of the notification.

    try:
        api_response = api_instance.get_notifications_by_id(notification_id)
        print("The response of NotificationsApi->get_notifications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->get_notifications_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**| The ID of the notification. | 

### Return type

[**Notification**](Notification.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested notification |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poll_notifications_cleanup**
> AsyncContext poll_notifications_cleanup(id)



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
    api_instance = cyperf.NotificationsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_notifications_cleanup(id)
        print("The response of NotificationsApi->poll_notifications_cleanup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->poll_notifications_cleanup: %s\n" % e)
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

# **poll_notifications_dismiss**
> AsyncContext poll_notifications_dismiss(id)



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
    api_instance = cyperf.NotificationsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_notifications_dismiss(id)
        print("The response of NotificationsApi->poll_notifications_dismiss:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->poll_notifications_dismiss: %s\n" % e)
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

# **start_notifications_cleanup**
> AsyncContext start_notifications_cleanup()



Cleanup all notifications that match the specified filter.

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
    api_instance = cyperf.NotificationsApi(api_client)

    try:
        api_response = api_instance.start_notifications_cleanup()
        print("The response of NotificationsApi->start_notifications_cleanup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->start_notifications_cleanup: %s\n" % e)
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

# **start_notifications_dismiss**
> AsyncContext start_notifications_dismiss()



Dismiss all notifications that match the specified filter.

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
    api_instance = cyperf.NotificationsApi(api_client)

    try:
        api_response = api_instance.start_notifications_dismiss()
        print("The response of NotificationsApi->start_notifications_dismiss:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->start_notifications_dismiss: %s\n" % e)
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

