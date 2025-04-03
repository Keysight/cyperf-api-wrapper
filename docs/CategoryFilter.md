# CategoryFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from cyperf.models.category_filter import CategoryFilter

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryFilter from a JSON string
category_filter_instance = CategoryFilter.from_json(json)
# print the JSON string representation of the object
print(CategoryFilter.to_json())

# convert the object into a dict
category_filter_dict = category_filter_instance.to_dict()
# create an instance of CategoryFilter from a dict
category_filter_from_dict = CategoryFilter.from_dict(category_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


