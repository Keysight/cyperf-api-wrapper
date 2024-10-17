# Choice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**hidden** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from cyperf.models.choice import Choice

# TODO update the JSON string below
json = "{}"
# create an instance of Choice from a JSON string
choice_instance = Choice.from_json(json)
# print the JSON string representation of the object
print(Choice.to_json())

# convert the object into a dict
choice_dict = choice_instance.to_dict()
# create an instance of Choice from a dict
choice_from_dict = Choice.from_dict(choice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


