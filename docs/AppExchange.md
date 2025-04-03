# AppExchange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**c2s_payload** | [**GenericFile**](GenericFile.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**payload** | [**ExchangePayload**](ExchangePayload.md) |  | [optional] 
**s2c_payload** | [**GenericFile**](GenericFile.md) |  | [optional] 

## Example

```python
from cyperf.models.app_exchange import AppExchange

# TODO update the JSON string below
json = "{}"
# create an instance of AppExchange from a JSON string
app_exchange_instance = AppExchange.from_json(json)
# print the JSON string representation of the object
print(AppExchange.to_json())

# convert the object into a dict
app_exchange_dict = app_exchange_instance.to_dict()
# create an instance of AppExchange from a dict
app_exchange_from_dict = AppExchange.from_dict(app_exchange_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


