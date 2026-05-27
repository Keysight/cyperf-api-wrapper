# SequenceValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom** | [**CustomSequence**](CustomSequence.md) |  | [optional] 
**data_type** | [**SequenceDataTypes**](SequenceDataTypes.md) |  | [optional] 
**increment** | [**SimpleSequenceValue**](SimpleSequenceValue.md) |  | [optional] 
**preview** | **List[str]** |  | [optional] 
**sequence_type** | [**SequenceValueTypes**](SequenceValueTypes.md) |  | [optional] 
**id** | **str** |  | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.sequence_value import SequenceValue

# TODO update the JSON string below
json = "{}"
# create an instance of SequenceValue from a JSON string
sequence_value_instance = SequenceValue.from_json(json)
# print the JSON string representation of the object
print(SequenceValue.to_json())

# convert the object into a dict
sequence_value_dict = sequence_value_instance.to_dict()
# create an instance of SequenceValue from a dict
sequence_value_from_dict = SequenceValue.from_dict(sequence_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


