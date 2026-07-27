# FormattedDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**layout** | [**LayoutConfig**](LayoutConfig.md) |  | [optional] 
**sections** | [**List[Section]**](Section.md) | The list of sections that make up the page. | [optional] 
**summary** | [**Section**](Section.md) |  | [optional] 

## Example

```python
from cyperf.models.formatted_description import FormattedDescription

# TODO update the JSON string below
json = "{}"
# create an instance of FormattedDescription from a JSON string
formatted_description_instance = FormattedDescription.from_json(json)
# print the JSON string representation of the object
print(FormattedDescription.to_json())

# convert the object into a dict
formatted_description_dict = formatted_description_instance.to_dict()
# create an instance of FormattedDescription from a dict
formatted_description_from_dict = FormattedDescription.from_dict(formatted_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


