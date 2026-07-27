# Keyword


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | The keyword category | [optional] 
**value** | **str** | The keyword value | [optional] 
**index** | **int** | The index of the category | [optional] 

## Example

```python
from cyperf.models.keyword import Keyword

# TODO update the JSON string below
json = "{}"
# create an instance of Keyword from a JSON string
keyword_instance = Keyword.from_json(json)
# print the JSON string representation of the object
print(Keyword.to_json())

# convert the object into a dict
keyword_dict = keyword_instance.to_dict()
# create an instance of Keyword from a dict
keyword_from_dict = Keyword.from_dict(keyword_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


