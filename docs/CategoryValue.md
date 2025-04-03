# CategoryValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items_count** | **int** | The number of items associated with the category value | [optional] 
**value** | **str** | One value of the category | [optional] 

## Example

```python
from cyperf.models.category_value import CategoryValue

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryValue from a JSON string
category_value_instance = CategoryValue.from_json(json)
# print the JSON string representation of the object
print(CategoryValue.to_json())

# convert the object into a dict
category_value_dict = category_value_instance.to_dict()
# create an instance of CategoryValue from a dict
category_value_from_dict = CategoryValue.from_dict(category_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


