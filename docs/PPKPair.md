# PPKPair


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ppkid** | **str** |  | 
**ppk_key** | **str** |  | 

## Example

```python
from cyperf.models.ppk_pair import PPKPair

# TODO update the JSON string below
json = "{}"
# create an instance of PPKPair from a JSON string
ppk_pair_instance = PPKPair.from_json(json)
# print the JSON string representation of the object
print(PPKPair.to_json())

# convert the object into a dict
ppk_pair_dict = ppk_pair_instance.to_dict()
# create an instance of PPKPair from a dict
ppk_pair_from_dict = PPKPair.from_dict(ppk_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


