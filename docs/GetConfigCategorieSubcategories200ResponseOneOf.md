# GetConfigCategorieSubcategories200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ConfigSubCategory]**](ConfigSubCategory.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from cyperf.models.get_config_categorie_subcategories200_response_one_of import GetConfigCategorieSubcategories200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetConfigCategorieSubcategories200ResponseOneOf from a JSON string
get_config_categorie_subcategories200_response_one_of_instance = GetConfigCategorieSubcategories200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(GetConfigCategorieSubcategories200ResponseOneOf.to_json())

# convert the object into a dict
get_config_categorie_subcategories200_response_one_of_dict = get_config_categorie_subcategories200_response_one_of_instance.to_dict()
# create an instance of GetConfigCategorieSubcategories200ResponseOneOf from a dict
get_config_categorie_subcategories200_response_one_of_from_dict = GetConfigCategorieSubcategories200ResponseOneOf.from_dict(get_config_categorie_subcategories200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


