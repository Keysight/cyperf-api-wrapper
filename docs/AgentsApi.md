# cyperf.AgentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_agents**](AgentsApi.md#delete_agents) | **DELETE** /api/v2/agents/{agentId} | 
[**get_agent_tags**](AgentsApi.md#get_agent_tags) | **GET** /api/v2/tags | 
[**get_agents**](AgentsApi.md#get_agents) | **GET** /api/v2/agents | 
[**get_agents_by_id**](AgentsApi.md#get_agents_by_id) | **GET** /api/v2/agents/{agentId} | 
[**get_compute_nodes**](AgentsApi.md#get_compute_nodes) | **GET** /api/v2/controllers/{controllerId}/compute-nodes | 
[**get_compute_nodes_by_id**](AgentsApi.md#get_compute_nodes_by_id) | **GET** /api/v2/controllers/{controllerId}/compute-nodes/{computeNodeId} | 
[**get_controllers**](AgentsApi.md#get_controllers) | **GET** /api/v2/controllers | 
[**get_controllers_by_id**](AgentsApi.md#get_controllers_by_id) | **GET** /api/v2/controllers/{controllerId} | 
[**get_ports**](AgentsApi.md#get_ports) | **GET** /api/v2/controllers/{controllerId}/compute-nodes/{computeNodeId}/ports | 
[**get_ports_by_id**](AgentsApi.md#get_ports_by_id) | **GET** /api/v2/controllers/{controllerId}/compute-nodes/{computeNodeId}/ports/{portId} | 
[**patch_agents**](AgentsApi.md#patch_agents) | **PATCH** /api/v2/agents/{agentId} | 
[**poll_batch_delete**](AgentsApi.md#poll_batch_delete) | **GET** /api/v2/agents/operations/batch-delete/{id} | 
[**poll_controllers_clear_port_ownership**](AgentsApi.md#poll_controllers_clear_port_ownership) | **GET** /api/v2/controllers/operations/clear-port-ownership/{id} | 
[**poll_controllers_power_cycle_nodes**](AgentsApi.md#poll_controllers_power_cycle_nodes) | **GET** /api/v2/controllers/operations/power-cycle-nodes/{id} | 
[**poll_controllers_reboot_port**](AgentsApi.md#poll_controllers_reboot_port) | **GET** /api/v2/controllers/operations/reboot-port/{id} | 
[**poll_controllers_set_app**](AgentsApi.md#poll_controllers_set_app) | **GET** /api/v2/controllers/operations/set-app/{id} | 
[**poll_controllers_set_node_aggregation**](AgentsApi.md#poll_controllers_set_node_aggregation) | **GET** /api/v2/controllers/operations/set-node-aggregation/{id} | 
[**poll_controllers_set_port_link_state**](AgentsApi.md#poll_controllers_set_port_link_state) | **GET** /api/v2/controllers/operations/set-port-link-state/{id} | 
[**poll_export_files**](AgentsApi.md#poll_export_files) | **GET** /api/v2/agents/operations/exportFiles/{id} | 
[**poll_reboot**](AgentsApi.md#poll_reboot) | **GET** /api/v2/agents/operations/reboot/{id} | 
[**poll_release**](AgentsApi.md#poll_release) | **GET** /api/v2/agents/operations/release/{id} | 
[**poll_reserve**](AgentsApi.md#poll_reserve) | **GET** /api/v2/agents/operations/reserve/{id} | 
[**poll_set_dpdk_mode**](AgentsApi.md#poll_set_dpdk_mode) | **GET** /api/v2/agents/operations/set-dpdk-mode/{id} | 
[**poll_set_ntp**](AgentsApi.md#poll_set_ntp) | **GET** /api/v2/agents/operations/set-ntp/{id} | 
[**poll_update**](AgentsApi.md#poll_update) | **GET** /api/v2/agents/operations/update/{id} | 
[**start_batch_delete**](AgentsApi.md#start_batch_delete) | **POST** /api/v2/agents/operations/batch-delete | 
[**start_controllers_clear_port_ownership**](AgentsApi.md#start_controllers_clear_port_ownership) | **POST** /api/v2/controllers/operations/clear-port-ownership | 
[**start_controllers_power_cycle_nodes**](AgentsApi.md#start_controllers_power_cycle_nodes) | **POST** /api/v2/controllers/operations/power-cycle-nodes | 
[**start_controllers_reboot_port**](AgentsApi.md#start_controllers_reboot_port) | **POST** /api/v2/controllers/operations/reboot-port | 
[**start_controllers_set_app**](AgentsApi.md#start_controllers_set_app) | **POST** /api/v2/controllers/operations/set-app | 
[**start_controllers_set_node_aggregation**](AgentsApi.md#start_controllers_set_node_aggregation) | **POST** /api/v2/controllers/operations/set-node-aggregation | 
[**start_controllers_set_port_link_state**](AgentsApi.md#start_controllers_set_port_link_state) | **POST** /api/v2/controllers/operations/set-port-link-state | 
[**start_export_files**](AgentsApi.md#start_export_files) | **POST** /api/v2/agents/operations/exportFiles | 
[**start_reboot**](AgentsApi.md#start_reboot) | **POST** /api/v2/agents/operations/reboot | 
[**start_release**](AgentsApi.md#start_release) | **POST** /api/v2/agents/operations/release | 
[**start_reserve**](AgentsApi.md#start_reserve) | **POST** /api/v2/agents/operations/reserve | 
[**start_set_dpdk_mode**](AgentsApi.md#start_set_dpdk_mode) | **POST** /api/v2/agents/operations/set-dpdk-mode | 
[**start_set_ntp**](AgentsApi.md#start_set_ntp) | **POST** /api/v2/agents/operations/set-ntp | 
[**start_update**](AgentsApi.md#start_update) | **POST** /api/v2/agents/operations/update | 


# **delete_agents**
> delete_agents(agent_id)



Remove a particular agent.

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
    api_instance = cyperf.AgentsApi(api_client)
    agent_id = 'agent_id_example' # str | The ID of the agent.

    try:
        api_instance.delete_agents(agent_id)
    except Exception as e:
        print("Exception when calling AgentsApi->delete_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| The ID of the agent. | 

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
**204** | The agent was successfully removed. |  -  |
**404** | An agent with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_tags**
> GetAgentTags200Response get_agent_tags(take=take, skip=skip)



Get all the currently available agent groups.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.get_agent_tags200_response import GetAgentTags200Response
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
    api_instance = cyperf.AgentsApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.get_agent_tags(take=take, skip=skip)
        print("The response of AgentsApi->get_agent_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_agent_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**GetAgentTags200Response**](GetAgentTags200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of agent groups |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agents**
> GetAgents200Response get_agents(take=take, skip=skip, search_col=search_col, search_val=search_val, filter_mode=filter_mode, sort=sort, exclude_offline=exclude_offline)



Get all the currently available agents.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.get_agents200_response import GetAgents200Response
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
    api_instance = cyperf.AgentsApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)
    search_col = 'search_col_example' # str | A list of comma-separated columns used to search for the supplied values (optional)
    search_val = 'search_val_example' # str | The keywords used to filter the items (optional)
    filter_mode = 'filter_mode_example' # str | The operator applied to the supplied values (optional)
    sort = 'sort_example' # str | A list of comma-separated field:direction pairs used to sort the items where direction must be asc or dsc (optional)
    exclude_offline = 'exclude_offline_example' # str | Indicates whether offline agents should be excluded (optional)

    try:
        api_response = api_instance.get_agents(take=take, skip=skip, search_col=search_col, search_val=search_val, filter_mode=filter_mode, sort=sort, exclude_offline=exclude_offline)
        print("The response of AgentsApi->get_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_agents: %s\n" % e)
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
 **exclude_offline** | **str**| Indicates whether offline agents should be excluded | [optional] 

### Return type

[**GetAgents200Response**](GetAgents200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of agents |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agents_by_id**
> Agent get_agents_by_id(agent_id)



Get a particular agent.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.agent import Agent
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
    api_instance = cyperf.AgentsApi(api_client)
    agent_id = 'agent_id_example' # str | The ID of the agent.

    try:
        api_response = api_instance.get_agents_by_id(agent_id)
        print("The response of AgentsApi->get_agents_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_agents_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| The ID of the agent. | 

### Return type

[**Agent**](Agent.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested agent |  -  |
**404** | An agent with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compute_nodes**
> List[ComputeNode] get_compute_nodes(controller_id, take=take, skip=skip)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.compute_node import ComputeNode
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
    api_instance = cyperf.AgentsApi(api_client)
    controller_id = 'controller_id_example' # str | The ID of the controller.
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.get_compute_nodes(controller_id, take=take, skip=skip)
        print("The response of AgentsApi->get_compute_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_compute_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **controller_id** | **str**| The ID of the controller. | 
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**List[ComputeNode]**](ComputeNode.md)

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

# **get_compute_nodes_by_id**
> ComputeNode get_compute_nodes_by_id(controller_id, compute_node_id)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.compute_node import ComputeNode
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
    api_instance = cyperf.AgentsApi(api_client)
    controller_id = 'controller_id_example' # str | The ID of the controller.
    compute_node_id = 'compute_node_id_example' # str | The ID of the compute node.

    try:
        api_response = api_instance.get_compute_nodes_by_id(controller_id, compute_node_id)
        print("The response of AgentsApi->get_compute_nodes_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_compute_nodes_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **controller_id** | **str**| The ID of the controller. | 
 **compute_node_id** | **str**| The ID of the compute node. | 

### Return type

[**ComputeNode**](ComputeNode.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | A resource with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_controllers**
> GetControllers200Response get_controllers(take=take, skip=skip)



Get the controllers chain.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.get_controllers200_response import GetControllers200Response
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
    api_instance = cyperf.AgentsApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.get_controllers(take=take, skip=skip)
        print("The response of AgentsApi->get_controllers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_controllers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**GetControllers200Response**](GetControllers200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of controllers. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_controllers_by_id**
> Controller get_controllers_by_id(controller_id)



Get the controller chain.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.controller import Controller
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
    api_instance = cyperf.AgentsApi(api_client)
    controller_id = 'controller_id_example' # str | The ID of the controller.

    try:
        api_response = api_instance.get_controllers_by_id(controller_id)
        print("The response of AgentsApi->get_controllers_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_controllers_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **controller_id** | **str**| The ID of the controller. | 

### Return type

[**Controller**](Controller.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The controller chain. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ports**
> List[Port] get_ports(controller_id, compute_node_id, take=take, skip=skip)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.port import Port
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
    api_instance = cyperf.AgentsApi(api_client)
    controller_id = 'controller_id_example' # str | The ID of the controller.
    compute_node_id = 'compute_node_id_example' # str | The ID of the compute node.
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.get_ports(controller_id, compute_node_id, take=take, skip=skip)
        print("The response of AgentsApi->get_ports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_ports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **controller_id** | **str**| The ID of the controller. | 
 **compute_node_id** | **str**| The ID of the compute node. | 
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**List[Port]**](Port.md)

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

# **get_ports_by_id**
> Port get_ports_by_id(controller_id, compute_node_id, port_id)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.port import Port
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
    api_instance = cyperf.AgentsApi(api_client)
    controller_id = 'controller_id_example' # str | The ID of the controller.
    compute_node_id = 'compute_node_id_example' # str | The ID of the compute node.
    port_id = 'port_id_example' # str | The ID of the port.

    try:
        api_response = api_instance.get_ports_by_id(controller_id, compute_node_id, port_id)
        print("The response of AgentsApi->get_ports_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_ports_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **controller_id** | **str**| The ID of the controller. | 
 **compute_node_id** | **str**| The ID of the compute node. | 
 **port_id** | **str**| The ID of the port. | 

### Return type

[**Port**](Port.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | A resource with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_agents**
> patch_agents(agent_id, agent=agent)



Update a particular agent. Only non-null fields are updated.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.agent import Agent
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
    api_instance = cyperf.AgentsApi(api_client)
    agent_id = 'agent_id_example' # str | The ID of the agent.
    agent = cyperf.Agent() # Agent |  (optional)

    try:
        api_instance.patch_agents(agent_id, agent=agent)
    except Exception as e:
        print("Exception when calling AgentsApi->patch_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| The ID of the agent. | 
 **agent** | [**Agent**](Agent.md)|  | [optional] 

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
**204** | The agent was successfully updated. |  -  |
**404** | An agent with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poll_batch_delete**
> AsyncContext poll_batch_delete(id)



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
    api_instance = cyperf.AgentsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_batch_delete(id)
        print("The response of AgentsApi->poll_batch_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->poll_batch_delete: %s\n" % e)
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

# **poll_controllers_clear_port_ownership**
> AsyncContext poll_controllers_clear_port_ownership(id)



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
    api_instance = cyperf.AgentsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_controllers_clear_port_ownership(id)
        print("The response of AgentsApi->poll_controllers_clear_port_ownership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->poll_controllers_clear_port_ownership: %s\n" % e)
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

# **poll_controllers_power_cycle_nodes**
> AsyncContext poll_controllers_power_cycle_nodes(id)



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
    api_instance = cyperf.AgentsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_controllers_power_cycle_nodes(id)
        print("The response of AgentsApi->poll_controllers_power_cycle_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->poll_controllers_power_cycle_nodes: %s\n" % e)
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

# **poll_controllers_reboot_port**
> AsyncContext poll_controllers_reboot_port(id)



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
    api_instance = cyperf.AgentsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_controllers_reboot_port(id)
        print("The response of AgentsApi->poll_controllers_reboot_port:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->poll_controllers_reboot_port: %s\n" % e)
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

# **poll_controllers_set_app**
> AsyncContext poll_controllers_set_app(id)



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
    api_instance = cyperf.AgentsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_controllers_set_app(id)
        print("The response of AgentsApi->poll_controllers_set_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->poll_controllers_set_app: %s\n" % e)
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

# **poll_controllers_set_node_aggregation**
> AsyncContext poll_controllers_set_node_aggregation(id)



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
    api_instance = cyperf.AgentsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_controllers_set_node_aggregation(id)
        print("The response of AgentsApi->poll_controllers_set_node_aggregation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->poll_controllers_set_node_aggregation: %s\n" % e)
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

# **poll_controllers_set_port_link_state**
> AsyncContext poll_controllers_set_port_link_state(id)



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
    api_instance = cyperf.AgentsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_controllers_set_port_link_state(id)
        print("The response of AgentsApi->poll_controllers_set_port_link_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->poll_controllers_set_port_link_state: %s\n" % e)
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

# **poll_export_files**
> AsyncContext poll_export_files(id)



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
    api_instance = cyperf.AgentsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_export_files(id)
        print("The response of AgentsApi->poll_export_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->poll_export_files: %s\n" % e)
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

# **poll_reboot**
> AsyncContext poll_reboot(id)



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
    api_instance = cyperf.AgentsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_reboot(id)
        print("The response of AgentsApi->poll_reboot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->poll_reboot: %s\n" % e)
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

# **poll_release**
> AsyncContext poll_release(id)



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
    api_instance = cyperf.AgentsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_release(id)
        print("The response of AgentsApi->poll_release:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->poll_release: %s\n" % e)
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

# **poll_reserve**
> AsyncContext poll_reserve(id)



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
    api_instance = cyperf.AgentsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_reserve(id)
        print("The response of AgentsApi->poll_reserve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->poll_reserve: %s\n" % e)
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

# **poll_set_dpdk_mode**
> AsyncContext poll_set_dpdk_mode(id)



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
    api_instance = cyperf.AgentsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_set_dpdk_mode(id)
        print("The response of AgentsApi->poll_set_dpdk_mode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->poll_set_dpdk_mode: %s\n" % e)
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

# **poll_set_ntp**
> AsyncContext poll_set_ntp(id)



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
    api_instance = cyperf.AgentsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_set_ntp(id)
        print("The response of AgentsApi->poll_set_ntp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->poll_set_ntp: %s\n" % e)
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

# **poll_update**
> AsyncContext poll_update(id)



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
    api_instance = cyperf.AgentsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_update(id)
        print("The response of AgentsApi->poll_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->poll_update: %s\n" % e)
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

# **start_batch_delete**
> AsyncContext start_batch_delete(start_batch_delete_request_inner=start_batch_delete_request_inner)



Remove multiple agents.

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
    api_instance = cyperf.AgentsApi(api_client)
    start_batch_delete_request_inner = [cyperf.StartBatchDeleteRequestInner()] # List[StartBatchDeleteRequestInner] |  (optional)

    try:
        api_response = api_instance.start_batch_delete(start_batch_delete_request_inner=start_batch_delete_request_inner)
        print("The response of AgentsApi->start_batch_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->start_batch_delete: %s\n" % e)
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

# **start_controllers_clear_port_ownership**
> AsyncContext start_controllers_clear_port_ownership(clear_ports_ownership_operation=clear_ports_ownership_operation)



Clear the ownership of the ports.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.clear_ports_ownership_operation import ClearPortsOwnershipOperation
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
    api_instance = cyperf.AgentsApi(api_client)
    clear_ports_ownership_operation = cyperf.ClearPortsOwnershipOperation() # ClearPortsOwnershipOperation |  (optional)

    try:
        api_response = api_instance.start_controllers_clear_port_ownership(clear_ports_ownership_operation=clear_ports_ownership_operation)
        print("The response of AgentsApi->start_controllers_clear_port_ownership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->start_controllers_clear_port_ownership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clear_ports_ownership_operation** | [**ClearPortsOwnershipOperation**](ClearPortsOwnershipOperation.md)|  | [optional] 

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

# **start_controllers_power_cycle_nodes**
> AsyncContext start_controllers_power_cycle_nodes(nodes_power_cycle_operation=nodes_power_cycle_operation)



Power cycle the compute nodes.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.nodes_power_cycle_operation import NodesPowerCycleOperation
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
    api_instance = cyperf.AgentsApi(api_client)
    nodes_power_cycle_operation = cyperf.NodesPowerCycleOperation() # NodesPowerCycleOperation |  (optional)

    try:
        api_response = api_instance.start_controllers_power_cycle_nodes(nodes_power_cycle_operation=nodes_power_cycle_operation)
        print("The response of AgentsApi->start_controllers_power_cycle_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->start_controllers_power_cycle_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodes_power_cycle_operation** | [**NodesPowerCycleOperation**](NodesPowerCycleOperation.md)|  | [optional] 

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

# **start_controllers_reboot_port**
> AsyncContext start_controllers_reboot_port(reboot_ports_operation=reboot_ports_operation)



Reboot ports.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.reboot_ports_operation import RebootPortsOperation
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
    api_instance = cyperf.AgentsApi(api_client)
    reboot_ports_operation = cyperf.RebootPortsOperation() # RebootPortsOperation |  (optional)

    try:
        api_response = api_instance.start_controllers_reboot_port(reboot_ports_operation=reboot_ports_operation)
        print("The response of AgentsApi->start_controllers_reboot_port:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->start_controllers_reboot_port: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reboot_ports_operation** | [**RebootPortsOperation**](RebootPortsOperation.md)|  | [optional] 

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

# **start_controllers_set_app**
> AsyncContext start_controllers_set_app(set_app_operation=set_app_operation)



Set the active app of the controllers.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.set_app_operation import SetAppOperation
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
    api_instance = cyperf.AgentsApi(api_client)
    set_app_operation = cyperf.SetAppOperation() # SetAppOperation |  (optional)

    try:
        api_response = api_instance.start_controllers_set_app(set_app_operation=set_app_operation)
        print("The response of AgentsApi->start_controllers_set_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->start_controllers_set_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_app_operation** | [**SetAppOperation**](SetAppOperation.md)|  | [optional] 

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

# **start_controllers_set_node_aggregation**
> AsyncContext start_controllers_set_node_aggregation(set_aggregation_mode_operation=set_aggregation_mode_operation)



Set the aggregation mode of the compute nodes.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.set_aggregation_mode_operation import SetAggregationModeOperation
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
    api_instance = cyperf.AgentsApi(api_client)
    set_aggregation_mode_operation = cyperf.SetAggregationModeOperation() # SetAggregationModeOperation |  (optional)

    try:
        api_response = api_instance.start_controllers_set_node_aggregation(set_aggregation_mode_operation=set_aggregation_mode_operation)
        print("The response of AgentsApi->start_controllers_set_node_aggregation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->start_controllers_set_node_aggregation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_aggregation_mode_operation** | [**SetAggregationModeOperation**](SetAggregationModeOperation.md)|  | [optional] 

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

# **start_controllers_set_port_link_state**
> AsyncContext start_controllers_set_port_link_state(set_link_state_operation=set_link_state_operation)



Set the link state of the ports.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.set_link_state_operation import SetLinkStateOperation
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
    api_instance = cyperf.AgentsApi(api_client)
    set_link_state_operation = cyperf.SetLinkStateOperation() # SetLinkStateOperation |  (optional)

    try:
        api_response = api_instance.start_controllers_set_port_link_state(set_link_state_operation=set_link_state_operation)
        print("The response of AgentsApi->start_controllers_set_port_link_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->start_controllers_set_port_link_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_link_state_operation** | [**SetLinkStateOperation**](SetLinkStateOperation.md)|  | [optional] 

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

# **start_export_files**
> AsyncContext start_export_files(export_files_operation_input=export_files_operation_input)



Sends export files requests to a list of agents.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.export_files_operation_input import ExportFilesOperationInput
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
    api_instance = cyperf.AgentsApi(api_client)
    export_files_operation_input = cyperf.ExportFilesOperationInput() # ExportFilesOperationInput |  (optional)

    try:
        api_response = api_instance.start_export_files(export_files_operation_input=export_files_operation_input)
        print("The response of AgentsApi->start_export_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->start_export_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_files_operation_input** | [**ExportFilesOperationInput**](ExportFilesOperationInput.md)|  | [optional] 

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

# **start_reboot**
> AsyncContext start_reboot(reboot_operation_input=reboot_operation_input)



Reboot the agents specified in the request.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.reboot_operation_input import RebootOperationInput
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
    api_instance = cyperf.AgentsApi(api_client)
    reboot_operation_input = cyperf.RebootOperationInput() # RebootOperationInput |  (optional)

    try:
        api_response = api_instance.start_reboot(reboot_operation_input=reboot_operation_input)
        print("The response of AgentsApi->start_reboot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->start_reboot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reboot_operation_input** | [**RebootOperationInput**](RebootOperationInput.md)|  | [optional] 

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

# **start_release**
> AsyncContext start_release(release_operation_input=release_operation_input)



Releases all the agents from the given session.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.release_operation_input import ReleaseOperationInput
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
    api_instance = cyperf.AgentsApi(api_client)
    release_operation_input = cyperf.ReleaseOperationInput() # ReleaseOperationInput |  (optional)

    try:
        api_response = api_instance.start_release(release_operation_input=release_operation_input)
        print("The response of AgentsApi->start_release:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->start_release: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_operation_input** | [**ReleaseOperationInput**](ReleaseOperationInput.md)|  | [optional] 

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

# **start_reserve**
> AsyncContext start_reserve(reserve_operation_input=reserve_operation_input)



Reserves all the agents from the given session.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.reserve_operation_input import ReserveOperationInput
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
    api_instance = cyperf.AgentsApi(api_client)
    reserve_operation_input = cyperf.ReserveOperationInput() # ReserveOperationInput |  (optional)

    try:
        api_response = api_instance.start_reserve(reserve_operation_input=reserve_operation_input)
        print("The response of AgentsApi->start_reserve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->start_reserve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reserve_operation_input** | [**ReserveOperationInput**](ReserveOperationInput.md)|  | [optional] 

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

# **start_set_dpdk_mode**
> AsyncContext start_set_dpdk_mode(set_dpdk_mode_operation_input=set_dpdk_mode_operation_input)



Enable/disable DPDK for a list of agents.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.set_dpdk_mode_operation_input import SetDpdkModeOperationInput
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
    api_instance = cyperf.AgentsApi(api_client)
    set_dpdk_mode_operation_input = cyperf.SetDpdkModeOperationInput() # SetDpdkModeOperationInput |  (optional)

    try:
        api_response = api_instance.start_set_dpdk_mode(set_dpdk_mode_operation_input=set_dpdk_mode_operation_input)
        print("The response of AgentsApi->start_set_dpdk_mode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->start_set_dpdk_mode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_dpdk_mode_operation_input** | [**SetDpdkModeOperationInput**](SetDpdkModeOperationInput.md)|  | [optional] 

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

# **start_set_ntp**
> AsyncContext start_set_ntp(set_ntp_operation_input=set_ntp_operation_input)



Set the NTP servers for a list of agents.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.set_ntp_operation_input import SetNtpOperationInput
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
    api_instance = cyperf.AgentsApi(api_client)
    set_ntp_operation_input = cyperf.SetNtpOperationInput() # SetNtpOperationInput |  (optional)

    try:
        api_response = api_instance.start_set_ntp(set_ntp_operation_input=set_ntp_operation_input)
        print("The response of AgentsApi->start_set_ntp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->start_set_ntp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_ntp_operation_input** | [**SetNtpOperationInput**](SetNtpOperationInput.md)|  | [optional] 

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

# **start_update**
> AsyncContext start_update()



Update agents to the recommended version.

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
    api_instance = cyperf.AgentsApi(api_client)

    try:
        api_response = api_instance.start_update()
        print("The response of AgentsApi->start_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->start_update: %s\n" % e)
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

