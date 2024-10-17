# ChangeAggregationModeOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregated** | **bool** | The desired aggregation mode. | [optional] 
**compute_nodes** | **List[str]** | The compute-node ids for which to change the aggregation mode. | [optional] 
**controller** | **str** | The id of the controller that is linked with the compute-nodes. | [optional] 

## Example

```python
from cyperf.models.change_aggregation_mode_operation import ChangeAggregationModeOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeAggregationModeOperation from a JSON string
change_aggregation_mode_operation_instance = ChangeAggregationModeOperation.from_json(json)
# print the JSON string representation of the object
print(ChangeAggregationModeOperation.to_json())

# convert the object into a dict
change_aggregation_mode_operation_dict = change_aggregation_mode_operation_instance.to_dict()
# create an instance of ChangeAggregationModeOperation from a dict
change_aggregation_mode_operation_from_dict = ChangeAggregationModeOperation.from_dict(change_aggregation_mode_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


