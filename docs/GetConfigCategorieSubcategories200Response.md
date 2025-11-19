# GetConfigCategorieSubcategories200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ConfigSubCategory]**](ConfigSubCategory.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from cyperf.models.get_config_categorie_subcategories200_response import GetConfigCategorieSubcategories200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetConfigCategorieSubcategories200Response from a JSON string
get_config_categorie_subcategories200_response_instance = GetConfigCategorieSubcategories200Response.from_json(json)
# print the JSON string representation of the object
print(GetConfigCategorieSubcategories200Response.to_json())

# convert the object into a dict
get_config_categorie_subcategories200_response_dict = get_config_categorie_subcategories200_response_instance.to_dict()
# create an instance of GetConfigCategorieSubcategories200Response from a dict
get_config_categorie_subcategories200_response_from_dict = GetConfigCategorieSubcategories200Response.from_dict(get_config_categorie_subcategories200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


