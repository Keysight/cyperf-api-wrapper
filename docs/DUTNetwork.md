# DUTNetwork


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**id** | **str** |  | 
**network_tags** | **List[str]** | A list of tags. | [optional] 
**client_dut_active** | **bool** |  | [optional] 
**client_dut_host** | **str** |  | [optional] 
**client_dut_port** | **int** | The listen port for client-side DUT (default: 80). | [optional] 
**config_settings** | **str** |  | [optional] 
**forward_proxy_pep_dut** | [**PepDUT**](PepDUT.md) |  | [optional] 
**forward_proxy_pep_dut_active** | **bool** | A flag indicating if the PEP device is an active device. If active, the simulated clients will send traffic to the PEP device host. (default: false) | [optional] 
**http_health_check** | [**HealthCheckConfig**](HealthCheckConfig.md) | The HTTP HealthCheck configuration for DUT | [optional] 
**https_health_check** | [**HealthCheckConfig**](HealthCheckConfig.md) | The HTTPS HealthCheck configuration for DUT | [optional] 
**hostname_suffix** | **str** | A suffix to be added to the Host header of all Apps/Attacks running through the forward proxy DUT (default: empty string). | [optional] 
**http_forward_proxy_mode** | **str** | Deprecated. This is ignored and the proxy mode will be deduced from the connection type. | [optional] 
**non_proxied_hosts** | [**Params**](Params.md) |  | [optional] 
**pep_dut** | [**PepDUT**](PepDUT.md) |  | [optional] 
**pep_dut_active** | **bool** | A flag indicating if the PEP device is an active device. If active, the simulated clients will send traffic to the PEP device host. (default: false) | [optional] 
**reverse_proxy_pep_dut** | [**PepDUT**](PepDUT.md) |  | [optional] 
**reverse_proxy_pep_dut_active** | **bool** | A flag indicating if the PEP device is an active device. If active, the simulated clients will send traffic to the PEP device host. (default: false) | [optional] 
**server_dut_active** | **bool** | A flag indicating if the server DUT is an active device. If it is, the simulated clients or client DUT(if active) will send traffic to the server DUT &#39;host&#39;; and the simulated servers will use the healtcheck configurations. (default: false) | [optional] 
**server_dut_host** | **str** | The hostname where the traffic goes if server DUT is active. | [optional] 
**server_dut_port** | **int** | The listen port for server-side DUT | [optional] 
**tcp_health_check** | [**HealthCheckConfig**](HealthCheckConfig.md) | The TCP HealthCheck configuration for DUT | [optional] 
**use_real_host** | **bool** | A flag indicating if tunneled hostname should use real domain names. | [optional] 
**active** | **bool** | A flag indicating if the server DUT is an active device. If it is, the simulated clients or client DUT(if active) will send traffic to the DUT &#39;host&#39;; and the simulated servers will use the healtcheck configurations. (default: false) | [optional] 
**host** | **str** | The hostname where the traffic goes if server DUT is active. | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.dut_network import DUTNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of DUTNetwork from a JSON string
dut_network_instance = DUTNetwork.from_json(json)
# print the JSON string representation of the object
print(DUTNetwork.to_json())

# convert the object into a dict
dut_network_dict = dut_network_instance.to_dict()
# create an instance of DUTNetwork from a dict
dut_network_from_dict = DUTNetwork.from_dict(dut_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


