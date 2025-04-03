# DNSResolver


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache_timeout** | **int** | The cached timeout for the DNS Resolver | [optional] 
**enable_perconnect** | **bool** | The enable perconnection value. | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**name_servers** | [**List[NameServer]**](NameServer.md) | A list of name servers. | [optional] 

## Example

```python
from cyperf.models.dns_resolver import DNSResolver

# TODO update the JSON string below
json = "{}"
# create an instance of DNSResolver from a JSON string
dns_resolver_instance = DNSResolver.from_json(json)
# print the JSON string representation of the object
print(DNSResolver.to_json())

# convert the object into a dict
dns_resolver_dict = dns_resolver_instance.to_dict()
# create an instance of DNSResolver from a dict
dns_resolver_from_dict = DNSResolver.from_dict(dns_resolver_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


