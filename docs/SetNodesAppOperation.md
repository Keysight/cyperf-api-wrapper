# SetNodesAppOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | The id of the app to activate on the compute nodes. | [optional] 
**controllers** | [**List[NodesByController]**](NodesByController.md) | The controllers that the compute nodes are part of. | [optional] 
**force** | **bool** | Whether the ownership information will be cleared or not. | [optional] 

## Example

```python
from cyperf.models.set_nodes_app_operation import SetNodesAppOperation

# TODO update the JSON string below
json = "{}"
# create an instance of SetNodesAppOperation from a JSON string
set_nodes_app_operation_instance = SetNodesAppOperation.from_json(json)
# print the JSON string representation of the object
print(SetNodesAppOperation.to_json())

# convert the object into a dict
set_nodes_app_operation_dict = set_nodes_app_operation_instance.to_dict()
# create an instance of SetNodesAppOperation from a dict
set_nodes_app_operation_from_dict = SetNodesAppOperation.from_dict(set_nodes_app_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


