# DNSServer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | A flag indicating if the servers should listen for DNS requests (default: false). | 
**port** | **int** | The port that the DNS server should listen on. (default: 53) | 

## Example

```python
from cyperf.models.dns_server import DNSServer

# TODO update the JSON string below
json = "{}"
# create an instance of DNSServer from a JSON string
dns_server_instance = DNSServer.from_json(json)
# print the JSON string representation of the object
print(DNSServer.to_json())

# convert the object into a dict
dns_server_dict = dns_server_instance.to_dict()
# create an instance of DNSServer from a dict
dns_server_from_dict = DNSServer.from_dict(dns_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


