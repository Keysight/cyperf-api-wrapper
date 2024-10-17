# Conflict


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**path_to_target** | **str** |  | 
**path_vars** | **Dict[str, str]** |  | 

## Example

```python
from cyperf.models.conflict import Conflict

# TODO update the JSON string below
json = "{}"
# create an instance of Conflict from a JSON string
conflict_instance = Conflict.from_json(json)
# print the JSON string representation of the object
print(Conflict.to_json())

# convert the object into a dict
conflict_dict = conflict_instance.to_dict()
# create an instance of Conflict from a dict
conflict_from_dict = Conflict.from_dict(conflict_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


