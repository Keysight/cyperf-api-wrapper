# NodesPowerCycleOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controllers** | [**List[NodesByController]**](NodesByController.md) | The controllers that the compute nodes are part of. | [optional] 

## Example

```python
from cyperf.models.nodes_power_cycle_operation import NodesPowerCycleOperation

# TODO update the JSON string below
json = "{}"
# create an instance of NodesPowerCycleOperation from a JSON string
nodes_power_cycle_operation_instance = NodesPowerCycleOperation.from_json(json)
# print the JSON string representation of the object
print(NodesPowerCycleOperation.to_json())

# convert the object into a dict
nodes_power_cycle_operation_dict = nodes_power_cycle_operation_instance.to_dict()
# create an instance of NodesPowerCycleOperation from a dict
nodes_power_cycle_operation_from_dict = NodesPowerCycleOperation.from_dict(nodes_power_cycle_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


