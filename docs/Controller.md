# Controller


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compute_nodes** | [**List[ComputeNode]**](ComputeNode.md) | The compute-nodes of the controller | [optional] 
**health_details** | [**List[HealthIssue]**](HealthIssue.md) | Details regarding any health issue of the controller | [optional] 
**healthy** | **bool** | Whether the controller has any health issue or not | [optional] 
**id** | **str** | The unique identifier of the controller | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**name** | **str** | A user-friendly display name for the controller | [optional] 
**serial** | **str** | The serial of the controller | [optional] 
**type** | **str** | The type of the controller | [optional] 

## Example

```python
from cyperf.models.controller import Controller

# TODO update the JSON string below
json = "{}"
# create an instance of Controller from a JSON string
controller_instance = Controller.from_json(json)
# print the JSON string representation of the object
print(Controller.to_json())

# convert the object into a dict
controller_dict = controller_instance.to_dict()
# create an instance of Controller from a dict
controller_from_dict = Controller.from_dict(controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


