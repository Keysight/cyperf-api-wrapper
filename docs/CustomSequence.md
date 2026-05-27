# CustomSequence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | [**SingleValue**](SingleValue.md) |  | [optional] 
**step** | [**SingleValue**](SingleValue.md) |  | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**sub_steps** | [**List[SubStep]**](SubStep.md) |  | [optional] 

## Example

```python
from cyperf.models.custom_sequence import CustomSequence

# TODO update the JSON string below
json = "{}"
# create an instance of CustomSequence from a JSON string
custom_sequence_instance = CustomSequence.from_json(json)
# print the JSON string representation of the object
print(CustomSequence.to_json())

# convert the object into a dict
custom_sequence_dict = custom_sequence_instance.to_dict()
# create an instance of CustomSequence from a dict
custom_sequence_from_dict = CustomSequence.from_dict(custom_sequence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


