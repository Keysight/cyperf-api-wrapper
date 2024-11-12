# PortsByController


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compute_nodes** | [**List[PortsByNode]**](PortsByNode.md) | The compute nodes that the ports are part of. | [optional] 
**controller_id** | **str** | The id of the controller that the ports are part of. | [optional] 

## Example

```python
from cyperf.models.ports_by_controller import PortsByController

# TODO update the JSON string below
json = "{}"
# create an instance of PortsByController from a JSON string
ports_by_controller_instance = PortsByController.from_json(json)
# print the JSON string representation of the object
print(PortsByController.to_json())

# convert the object into a dict
ports_by_controller_dict = ports_by_controller_instance.to_dict()
# create an instance of PortsByController from a dict
ports_by_controller_from_dict = PortsByController.from_dict(ports_by_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


