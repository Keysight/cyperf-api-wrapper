# IPNetwork

The IP network configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**id** | **str** |  | 
**network_tags** | **List[str]** | A list of tags. | [optional] 
**dns_resolver** | [**DNSResolver**](DNSResolver.md) |  | [optional] 
**dns_server** | [**DNSServer**](DNSServer.md) | The DNS Server configuration for Network Segment | [optional] 
**dut_connections** | **List[str]** | The connected DUT network segments. | [optional] 
**emulated_router** | [**EmulatedRouter**](EmulatedRouter.md) |  | [optional] 
**eth_range** | [**EthRange**](EthRange.md) |  | [optional] 
**ip_ranges** | [**List[IPRange]**](IPRange.md) |  | [optional] 
**ip_sec_stacks** | [**List[IPSecStack]**](IPSecStack.md) |  | [optional] 
**mac_dtls_stacks** | [**List[MacDtlsStack]**](MacDtlsStack.md) |  | [optional] 
**tunnel_stacks** | [**List[TunnelStack]**](TunnelStack.md) |  | [optional] 
**vx_lan_stacks** | [**List[VxLANStack]**](VxLANStack.md) |  | [optional] 
**active** | **bool** | A flag indicating if the network segment is active.(default: true) | [optional] 
**agent_assignments** | [**AgentAssignments**](AgentAssignments.md) |  | [optional] 
**inherit_streaming_cpu_allocation** | **bool** | A flag indicating if the CPU percentage used by agents assigned to this network segment for streaming purposes will be inherited from the objective settings (default: true). | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**min_agents** | **int** | The minimum number of agents that should be assigned to this network segment in a valid test (default: 1). | [optional] 
**streaming_cpu_allocation** | **int** | The CPU percentage used by agents assigned to this network segment for streaming purposes (default: 25). | [optional] 

## Example

```python
from cyperf.models.ip_network import IPNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of IPNetwork from a JSON string
ip_network_instance = IPNetwork.from_json(json)
# print the JSON string representation of the object
print(IPNetwork.to_json())

# convert the object into a dict
ip_network_dict = ip_network_instance.to_dict()
# create an instance of IPNetwork from a dict
ip_network_from_dict = IPNetwork.from_dict(ip_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


