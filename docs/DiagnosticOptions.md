# DiagnosticOptions

Object that holds a diagnostic component option.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the diagnostic component option. | [optional] 
**value** | **str** | The value of the diagnostic component option. | [optional] 

## Example

```python
from cyperf.models.diagnostic_options import DiagnosticOptions

# TODO update the JSON string below
json = "{}"
# create an instance of DiagnosticOptions from a JSON string
diagnostic_options_instance = DiagnosticOptions.from_json(json)
# print the JSON string representation of the object
print(DiagnosticOptions.to_json())

# convert the object into a dict
diagnostic_options_dict = diagnostic_options_instance.to_dict()
# create an instance of DiagnosticOptions from a dict
diagnostic_options_from_dict = DiagnosticOptions.from_dict(diagnostic_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


