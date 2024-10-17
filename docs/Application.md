# Application


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_timeout** | **int** | The action timeout value of the Scenario. | [optional] 
**active** | **bool** | Indicates whether the scenario is enabled or not. | [optional] 
**client_http_profile** | [**HTTPProfile**](HTTPProfile.md) | The client HTTP profile used in the Scenario. | [optional] 
**connections** | [**List[Connection]**](Connection.md) |  | [optional] 
**connections_max_transactions** | **int** | The maximum number of transactions for all scenario connections. | [optional] 
**description** | **str** | The description of the Scenario. | [optional] 
**destination_hostname** | **str** |  | [optional] 
**dnn_id** | **str** |  | [optional] 
**end_point_id** | **int** | The endpoint ID of the Scenario. | [optional] 
**endpoints** | [**List[Endpoint]**](Endpoint.md) |  | [optional] 
**external_resource_url** | **str** | The external resource URL of the Scenario. | [optional] 
**id** | **str** |  | [optional] 
**index** | **int** | The index of the scenario. | [optional] 
**inherit_http_profile** | **bool** |  | [optional] 
**ip_preference** | [**IpPreference**](IpPreference.md) | The Ip Preference. Must be one of: IPV4_ONLY, IPV6_ONLY, BOTH_IPV4_FIRST, BOTH_IPV6_FIRST or IP_PREF_MAX. | [optional] 
**is_deprecated** | **bool** | A value that indicates if the action is deprecated. | [optional] 
**iteration_count** | **int** | The iteration counter of the Scenario. | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**max_active_limit** | **int** | The maximum active limit of the Scenario. | [optional] 
**name** | **str** |  | [optional] 
**network_mapping** | [**NetworkMapping**](NetworkMapping.md) |  | [optional] 
**params** | [**List[Params]**](Params.md) |  | [optional] 
**protocol_id** | **str** | The protocol ID of the Scenario. | [optional] 
**qos_flow_id** | **str** |  | [optional] 
**readonly_max_trans** | **bool** | If true, ConnectionsMaxTransactions will be readonly. | [optional] 
**server_http_profile** | [**HTTPProfile**](HTTPProfile.md) | The server HTTP profile used in the Scenario. | [optional] 
**supports_client_http_profile** | **bool** | Indicates if the scenario supports Client HTTP profile. | [optional] 
**supports_http_profiles** | **bool** | Indicates if the scenario supports HTTP profiles. | [optional] 
**supports_server_http_profile** | **bool** | Indicates if the scenario supports Server HTTP profile. | [optional] 
**client_tls_profile** | [**TLSProfile**](TLSProfile.md) |  | [optional] 
**data_types** | [**List[DataType]**](DataType.md) |  | [optional] 
**inherit_tls** | **bool** |  | [optional] 
**is_stateless_stream** | **bool** |  | [optional] 
**modify_excluded_dut_recursively** | [**List[UpdateNetworkMapping]**](UpdateNetworkMapping.md) |  | [optional] 
**modify_tags_recursively** | [**List[UpdateNetworkMapping]**](UpdateNetworkMapping.md) |  | [optional] 
**objective_weight** | **int** | The objective weight of the application. | 
**server_tls_profile** | [**TLSProfile**](TLSProfile.md) |  | [optional] 
**stateless_stream** | [**StatelessStream**](StatelessStream.md) |  | [optional] 
**static** | **bool** |  | [optional] 
**supported_apps** | **List[str]** |  | [optional] 
**supports_calibration** | **bool** |  | [optional] 
**supports_strikes** | **bool** |  | [optional] 
**supports_tls** | **bool** |  | [optional] 
**tracks** | [**List[Track]**](Track.md) |  | [optional] 

## Example

```python
from cyperf.models.application import Application

# TODO update the JSON string below
json = "{}"
# create an instance of Application from a JSON string
application_instance = Application.from_json(json)
# print the JSON string representation of the object
print(Application.to_json())

# convert the object into a dict
application_dict = application_instance.to_dict()
# create an instance of Application from a dict
application_from_dict = Application.from_dict(application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


