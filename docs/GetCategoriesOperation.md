# GetCategoriesOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**List[CategoryFilter]**](CategoryFilter.md) |  | [optional] 

## Example

```python
from cyperf.models.get_categories_operation import GetCategoriesOperation

# TODO update the JSON string below
json = "{}"
# create an instance of GetCategoriesOperation from a JSON string
get_categories_operation_instance = GetCategoriesOperation.from_json(json)
# print the JSON string representation of the object
print(GetCategoriesOperation.to_json())

# convert the object into a dict
get_categories_operation_dict = get_categories_operation_instance.to_dict()
# create an instance of GetCategoriesOperation from a dict
get_categories_operation_from_dict = GetCategoriesOperation.from_dict(get_categories_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


