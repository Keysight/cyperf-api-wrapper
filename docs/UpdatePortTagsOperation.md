# UpdatePortTagsOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controllers** | [**List[PortsByController]**](PortsByController.md) | The controllers that the ports are part of. | [optional] 
**tags_to_add** | **List[str]** | The list of tags to add to the port selection | [optional] 
**tags_to_remove** | **List[str]** | The list of tags to remove from the port selection | [optional] 

## Example

```python
from cyperf.models.update_port_tags_operation import UpdatePortTagsOperation

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePortTagsOperation from a JSON string
update_port_tags_operation_instance = UpdatePortTagsOperation.from_json(json)
# print the JSON string representation of the object
print(UpdatePortTagsOperation.to_json())

# convert the object into a dict
update_port_tags_operation_dict = update_port_tags_operation_instance.to_dict()
# create an instance of UpdatePortTagsOperation from a dict
update_port_tags_operation_from_dict = UpdatePortTagsOperation.from_dict(update_port_tags_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


