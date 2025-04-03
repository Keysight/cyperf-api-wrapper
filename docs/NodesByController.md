# NodesByController


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compute_nodes** | **List[str]** | The compute node ids. | [optional] 
**controller_id** | **str** | The id of the controller that the compute nodes are part of. | [optional] 

## Example

```python
from cyperf.models.nodes_by_controller import NodesByController

# TODO update the JSON string below
json = "{}"
# create an instance of NodesByController from a JSON string
nodes_by_controller_instance = NodesByController.from_json(json)
# print the JSON string representation of the object
print(NodesByController.to_json())

# convert the object into a dict
nodes_by_controller_dict = nodes_by_controller_instance.to_dict()
# create an instance of NodesByController from a dict
nodes_by_controller_from_dict = NodesByController.from_dict(nodes_by_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


