# ErrorDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 

## Example

```python
from cyperf.models.error_description import ErrorDescription

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorDescription from a JSON string
error_description_instance = ErrorDescription.from_json(json)
# print the JSON string representation of the object
print(ErrorDescription.to_json())

# convert the object into a dict
error_description_dict = error_description_instance.to_dict()
# create an instance of ErrorDescription from a dict
error_description_from_dict = ErrorDescription.from_dict(error_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


