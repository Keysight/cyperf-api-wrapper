# ReserveOperationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agents_data** | [**List[AgentReservation]**](AgentReservation.md) |  | [optional] 
**force** | **bool** |  | [optional] 
**owner** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**payloads** | [**Dict[str, PayloadMeta]**](PayloadMeta.md) |  | [optional] 
**session_id** | **str** |  | [optional] 
**session_name** | **str** |  | [optional] 

## Example

```python
from cyperf.models.reserve_operation_input import ReserveOperationInput

# TODO update the JSON string below
json = "{}"
# create an instance of ReserveOperationInput from a JSON string
reserve_operation_input_instance = ReserveOperationInput.from_json(json)
# print the JSON string representation of the object
print(ReserveOperationInput.to_json())

# convert the object into a dict
reserve_operation_input_dict = reserve_operation_input_instance.to_dict()
# create an instance of ReserveOperationInput from a dict
reserve_operation_input_from_dict = ReserveOperationInput.from_dict(reserve_operation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


