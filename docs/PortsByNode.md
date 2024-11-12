# PortsByNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compute_node_id** | **str** | The id of the compute node that the ports are part of. | [optional] 
**ports** | **List[str]** | The port ids. | [optional] 

## Example

```python
from cyperf.models.ports_by_node import PortsByNode

# TODO update the JSON string below
json = "{}"
# create an instance of PortsByNode from a JSON string
ports_by_node_instance = PortsByNode.from_json(json)
# print the JSON string representation of the object
print(PortsByNode.to_json())

# convert the object into a dict
ports_by_node_dict = ports_by_node_instance.to_dict()
# create an instance of PortsByNode from a dict
ports_by_node_from_dict = PortsByNode.from_dict(ports_by_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


