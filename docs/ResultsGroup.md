# ResultsGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the result group | [optional] [readonly] 
**results** | **List[str]** | The IDs of the results that are part of the group | [optional] [readonly] 

## Example

```python
from cyperf.models.results_group import ResultsGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ResultsGroup from a JSON string
results_group_instance = ResultsGroup.from_json(json)
# print the JSON string representation of the object
print(ResultsGroup.to_json())

# convert the object into a dict
results_group_dict = results_group_instance.to_dict()
# create an instance of ResultsGroup from a dict
results_group_from_dict = ResultsGroup.from_dict(results_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


