# Command


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_id** | **str** | The internal ID of the command | [optional] [readonly] 
**description** | **str** | The description of the command | [optional] 
**exchanges** | [**List[Exchange]**](Exchange.md) | The exchanges of the command | [optional] 
**is_strike** | **bool** | Indicates if the command is a strike | [optional] [readonly] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**name** | **str** | The name of the command | [optional] [readonly] 
**parameters** | [**List[Parameter]**](Parameter.md) | The parameters of the command | [optional] 

## Example

```python
from cyperf.models.command import Command

# TODO update the JSON string below
json = "{}"
# create an instance of Command from a JSON string
command_instance = Command.from_json(json)
# print the JSON string representation of the object
print(Command.to_json())

# convert the object into a dict
command_dict = command_instance.to_dict()
# create an instance of Command from a dict
command_from_dict = Command.from_dict(command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


