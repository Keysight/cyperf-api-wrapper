# DiagnosticComponent

Object that holds the diagnostic component metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component_name** | **str** | The name of the diagnostic component. | [optional] 
**options** | [**List[DiagnosticOptions]**](DiagnosticOptions.md) | The list of diagnostic options. | [optional] 
**sub_components** | [**List[DiagnosticComponent]**](DiagnosticComponent.md) | The list of subordinated diagnostic components. | [optional] 

## Example

```python
from cyperf.models.diagnostic_component import DiagnosticComponent

# TODO update the JSON string below
json = "{}"
# create an instance of DiagnosticComponent from a JSON string
diagnostic_component_instance = DiagnosticComponent.from_json(json)
# print the JSON string representation of the object
print(DiagnosticComponent.to_json())

# convert the object into a dict
diagnostic_component_dict = diagnostic_component_instance.to_dict()
# create an instance of DiagnosticComponent from a dict
diagnostic_component_from_dict = DiagnosticComponent.from_dict(diagnostic_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


