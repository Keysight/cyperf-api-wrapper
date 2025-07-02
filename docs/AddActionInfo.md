# AddActionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_id** | **str** |  | 
**insert_at_index** | **int** |  | 
**is_strike** | **bool** |  | 
**protocol_id** | **str** |  | 

## Example

```python
from cyperf.models.add_action_info import AddActionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AddActionInfo from a JSON string
add_action_info_instance = AddActionInfo.from_json(json)
# print the JSON string representation of the object
print(AddActionInfo.to_json())

# convert the object into a dict
add_action_info_dict = add_action_info_instance.to_dict()
# create an instance of AddActionInfo from a dict
add_action_info_from_dict = AddActionInfo.from_dict(add_action_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


