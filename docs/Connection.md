# Connection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_endpoint** | **str** | The client endpoint of the connection. | 
**client_port** | **int** | The client port of the connection (default: 80). | 
**closing_end** | **str** |  | [optional] 
**disable_encryption** | **bool** | If true, the connection will be unencrypted regardless of other TLS settings. | [optional] 
**hostname** | **str** | The hostname associated with the connection. (default: generic.keysight.io). | [optional] 
**hostname_param** | [**Params**](Params.md) | The hostname associated with the connection. (default: generic.keysight.io). | [optional] 
**http_forward_proxy_mode** | **str** | Deprecated. This is ignored and the proxy mode will be deduced from the connection type. | [optional] 
**id** | **str** |  | 
**is_deprecated** | **bool** |  | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**max_transactions** | **int** | The maximum number of transactions for this connection. | 
**name** | **str** | The name of the Connection. | [optional] 
**port_settings** | [**PortSettings**](PortSettings.md) |  | [optional] 
**readonly** | **bool** | If true, the connection can&#39;t be modified by the user. | [optional] 
**readonly_hostname** | **bool** | If true, the connection hostname will be readonly. | [optional] 
**readonly_max_trans** | **bool** | If true, MaxTransactions will be readonly | [optional] 
**readonly_type** | **bool** | If true or missing, the type of the connection cannot be changed | [optional] 
**server_endpoint** | **str** | The server endpoint of the connection. | [optional] 
**server_port** | **int** | The server port of the connection (default: 80). | 
**type** | **str** |  | [optional] 

## Example

```python
from cyperf.models.connection import Connection

# TODO update the JSON string below
json = "{}"
# create an instance of Connection from a JSON string
connection_instance = Connection.from_json(json)
# print the JSON string representation of the object
print(Connection.to_json())

# convert the object into a dict
connection_dict = connection_instance.to_dict()
# create an instance of Connection from a dict
connection_from_dict = Connection.from_dict(connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


