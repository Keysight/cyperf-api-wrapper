# ReorderExchangesInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_name** | **str** |  | [optional] 
**exchanges_order** | [**List[ExchangeOrder]**](ExchangeOrder.md) |  | [optional] 
**flow_idx** | **int** |  | [optional] 

## Example

```python
from cyperf.models.reorder_exchanges_input import ReorderExchangesInput

# TODO update the JSON string below
json = "{}"
# create an instance of ReorderExchangesInput from a JSON string
reorder_exchanges_input_instance = ReorderExchangesInput.from_json(json)
# print the JSON string representation of the object
print(ReorderExchangesInput.to_json())

# convert the object into a dict
reorder_exchanges_input_dict = reorder_exchanges_input_instance.to_dict()
# create an instance of ReorderExchangesInput from a dict
reorder_exchanges_input_from_dict = ReorderExchangesInput.from_dict(reorder_exchanges_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


