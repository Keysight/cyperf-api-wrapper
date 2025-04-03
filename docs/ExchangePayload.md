# ExchangePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**c2s** | **bytearray** |  | [optional] 
**s2c** | **bytearray** |  | [optional] 

## Example

```python
from cyperf.models.exchange_payload import ExchangePayload

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangePayload from a JSON string
exchange_payload_instance = ExchangePayload.from_json(json)
# print the JSON string representation of the object
print(ExchangePayload.to_json())

# convert the object into a dict
exchange_payload_dict = exchange_payload_instance.to_dict()
# create an instance of ExchangePayload from a dict
exchange_payload_from_dict = ExchangePayload.from_dict(exchange_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


