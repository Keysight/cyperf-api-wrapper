# ExchangeOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exchange_id** | **str** |  | [optional] 
**exchange_idx** | **int** |  | [optional] 

## Example

```python
from cyperf.models.exchange_order import ExchangeOrder

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeOrder from a JSON string
exchange_order_instance = ExchangeOrder.from_json(json)
# print the JSON string representation of the object
print(ExchangeOrder.to_json())

# convert the object into a dict
exchange_order_dict = exchange_order_instance.to_dict()
# create an instance of ExchangeOrder from a dict
exchange_order_from_dict = ExchangeOrder.from_dict(exchange_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


