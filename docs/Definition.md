# Definition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**xml** | **bytearray** | The XML definition of the application | [optional] 

## Example

```python
from cyperf.models.definition import Definition

# TODO update the JSON string below
json = "{}"
# create an instance of Definition from a JSON string
definition_instance = Definition.from_json(json)
# print the JSON string representation of the object
print(Definition.to_json())

# convert the object into a dict
definition_dict = definition_instance.to_dict()
# create an instance of Definition from a dict
definition_from_dict = Definition.from_dict(definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


