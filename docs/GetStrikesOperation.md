# GetStrikesOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**List[CategoryFilter]**](CategoryFilter.md) |  | [optional] 
**compatible_with** | **str** |  | [optional] 
**filter_mode** | **str** |  | [optional] 
**search_col** | **List[str]** |  | [optional] 
**search_val** | **List[str]** |  | [optional] 
**skip** | **str** |  | [optional] 
**sort** | [**List[SortBodyField]**](SortBodyField.md) |  | [optional] 
**take** | **str** |  | [optional] 

## Example

```python
from cyperf.models.get_strikes_operation import GetStrikesOperation

# TODO update the JSON string below
json = "{}"
# create an instance of GetStrikesOperation from a JSON string
get_strikes_operation_instance = GetStrikesOperation.from_json(json)
# print the JSON string representation of the object
print(GetStrikesOperation.to_json())

# convert the object into a dict
get_strikes_operation_dict = get_strikes_operation_instance.to_dict()
# create an instance of GetStrikesOperation from a dict
get_strikes_operation_from_dict = GetStrikesOperation.from_dict(get_strikes_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


