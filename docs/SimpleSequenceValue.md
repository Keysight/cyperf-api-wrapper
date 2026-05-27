# SimpleSequenceValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | [**SingleValue**](SingleValue.md) |  | [optional] 
**step** | [**SingleValue**](SingleValue.md) |  | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.simple_sequence_value import SimpleSequenceValue

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleSequenceValue from a JSON string
simple_sequence_value_instance = SimpleSequenceValue.from_json(json)
# print the JSON string representation of the object
print(SimpleSequenceValue.to_json())

# convert the object into a dict
simple_sequence_value_dict = simple_sequence_value_instance.to_dict()
# create an instance of SimpleSequenceValue from a dict
simple_sequence_value_from_dict = SimpleSequenceValue.from_dict(simple_sequence_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


