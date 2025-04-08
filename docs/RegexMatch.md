# RegexMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patterns** | **List[str]** |  | [optional] 

## Example

```python
from cyperf.models.regex_match import RegexMatch

# TODO update the JSON string below
json = "{}"
# create an instance of RegexMatch from a JSON string
regex_match_instance = RegexMatch.from_json(json)
# print the JSON string representation of the object
print(RegexMatch.to_json())

# convert the object into a dict
regex_match_dict = regex_match_instance.to_dict()
# create an instance of RegexMatch from a dict
regex_match_from_dict = RegexMatch.from_dict(regex_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


