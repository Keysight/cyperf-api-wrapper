# SubStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**step** | [**SingleValue**](SingleValue.md) |  | [optional] 
**sub_steps** | [**List[SubStep]**](SubStep.md) |  | 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.sub_step import SubStep

# TODO update the JSON string below
json = "{}"
# create an instance of SubStep from a JSON string
sub_step_instance = SubStep.from_json(json)
# print the JSON string representation of the object
print(SubStep.to_json())

# convert the object into a dict
sub_step_dict = sub_step_instance.to_dict()
# create an instance of SubStep from a dict
sub_step_from_dict = SubStep.from_dict(sub_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


