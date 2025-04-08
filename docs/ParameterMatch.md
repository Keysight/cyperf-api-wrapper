# ParameterMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_location** | **List[str]** |  | [optional] 
**match_type** | **str** |  | [optional] 
**regex_match** | [**RegexMatch**](RegexMatch.md) |  | [optional] 

## Example

```python
from cyperf.models.parameter_match import ParameterMatch

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterMatch from a JSON string
parameter_match_instance = ParameterMatch.from_json(json)
# print the JSON string representation of the object
print(ParameterMatch.to_json())

# convert the object into a dict
parameter_match_dict = parameter_match_instance.to_dict()
# create an instance of ParameterMatch from a dict
parameter_match_from_dict = ParameterMatch.from_dict(parameter_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


