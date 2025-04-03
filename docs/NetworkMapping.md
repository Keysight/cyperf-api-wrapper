# NetworkMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_network_tags** | **List[str]** | A list of tags of Network Segments which serve as clients. (default: Client) | 
**excluded_dut_list** | **List[str]** | A list of DUTs that are excluded from client-server network connections. | [optional] 
**server_network_tags** | **List[str]** | A list of tags of Network Segments which serve as servers. (default: Server) | 

## Example

```python
from cyperf.models.network_mapping import NetworkMapping

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkMapping from a JSON string
network_mapping_instance = NetworkMapping.from_json(json)
# print the JSON string representation of the object
print(NetworkMapping.to_json())

# convert the object into a dict
network_mapping_dict = network_mapping_instance.to_dict()
# create an instance of NetworkMapping from a dict
network_mapping_from_dict = NetworkMapping.from_dict(network_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


