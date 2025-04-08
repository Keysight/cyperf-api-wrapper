# FindParamMatchesOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[ActionInputFindParam]**](ActionInputFindParam.md) |  | [optional] 
**app_id** | **str** |  | [optional] 
**match_location** | **List[str]** |  | [optional] 
**pattern** | **str** |  | [optional] 

## Example

```python
from cyperf.models.find_param_matches_operation import FindParamMatchesOperation

# TODO update the JSON string below
json = "{}"
# create an instance of FindParamMatchesOperation from a JSON string
find_param_matches_operation_instance = FindParamMatchesOperation.from_json(json)
# print the JSON string representation of the object
print(FindParamMatchesOperation.to_json())

# convert the object into a dict
find_param_matches_operation_dict = find_param_matches_operation_instance.to_dict()
# create an instance of FindParamMatchesOperation from a dict
find_param_matches_operation_from_dict = FindParamMatchesOperation.from_dict(find_param_matches_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


