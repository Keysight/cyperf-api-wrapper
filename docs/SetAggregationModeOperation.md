# SetAggregationModeOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregated** | **bool** | The desired aggregation mode. | [optional] 
**controllers** | [**List[NodesByController]**](NodesByController.md) | The controllers that the compute nodes are part of. | [optional] 

## Example

```python
from cyperf.models.set_aggregation_mode_operation import SetAggregationModeOperation

# TODO update the JSON string below
json = "{}"
# create an instance of SetAggregationModeOperation from a JSON string
set_aggregation_mode_operation_instance = SetAggregationModeOperation.from_json(json)
# print the JSON string representation of the object
print(SetAggregationModeOperation.to_json())

# convert the object into a dict
set_aggregation_mode_operation_dict = set_aggregation_mode_operation_instance.to_dict()
# create an instance of SetAggregationModeOperation from a dict
set_aggregation_mode_operation_from_dict = SetAggregationModeOperation.from_dict(set_aggregation_mode_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


