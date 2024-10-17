# ObjectiveValueEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the objective. | 
**unit** | **str** | The unit of the Objective. | [optional] 
**value** | **float** | The value of the Objective. | 

## Example

```python
from cyperf.models.objective_value_entry import ObjectiveValueEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectiveValueEntry from a JSON string
objective_value_entry_instance = ObjectiveValueEntry.from_json(json)
# print the JSON string representation of the object
print(ObjectiveValueEntry.to_json())

# convert the object into a dict
objective_value_entry_dict = objective_value_entry_instance.to_dict()
# create an instance of ObjectiveValueEntry from a dict
objective_value_entry_from_dict = ObjectiveValueEntry.from_dict(objective_value_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


