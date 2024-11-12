# Exchange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_endpoint** | **str** | The client&#39;s endpoint for exchange. | [optional] 
**name** | **str** | The name of the exchange. | [optional] 
**server_endpoint** | **str** | The server&#39;s endpoint for exchange. | [optional] 
**id** | **str** |  | 

## Example

```python
from cyperf.models.exchange import Exchange

# TODO update the JSON string below
json = "{}"
# create an instance of Exchange from a JSON string
exchange_instance = Exchange.from_json(json)
# print the JSON string representation of the object
print(Exchange.to_json())

# convert the object into a dict
exchange_dict = exchange_instance.to_dict()
# create an instance of Exchange from a dict
exchange_from_dict = Exchange.from_dict(exchange_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


