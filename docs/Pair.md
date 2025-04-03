# Pair


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the session meta pair | [optional] 
**key** | **str** | The key of the meta pair | [optional] 
**value** | **str** | The value of the meta pair | [optional] 

## Example

```python
from cyperf.models.pair import Pair

# TODO update the JSON string below
json = "{}"
# create an instance of Pair from a JSON string
pair_instance = Pair.from_json(json)
# print the JSON string representation of the object
print(Pair.to_json())

# convert the object into a dict
pair_dict = pair_instance.to_dict()
# create an instance of Pair from a dict
pair_from_dict = Pair.from_dict(pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


