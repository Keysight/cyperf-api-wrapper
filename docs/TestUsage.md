# TestUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**used_agents** | **List[str]** | The agents used by the current test | [optional] 
**used_licenses** | **Dict[str, int]** | Feature types used by the current test and their respective counts | [optional] 

## Example

```python
from cyperf.models.test_usage import TestUsage

# TODO update the JSON string below
json = "{}"
# create an instance of TestUsage from a JSON string
test_usage_instance = TestUsage.from_json(json)
# print the JSON string representation of the object
print(TestUsage.to_json())

# convert the object into a dict
test_usage_dict = test_usage_instance.to_dict()
# create an instance of TestUsage from a dict
test_usage_from_dict = TestUsage.from_dict(test_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


