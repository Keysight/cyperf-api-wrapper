# DiagnosticComponentContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component_list** | [**List[DiagnosticComponent]**](DiagnosticComponent.md) | A list of components and subcomponents. | 
**context** | [**List[DiagnosticOptions]**](DiagnosticOptions.md) | Additional information about the caller or about the case where the operation was called. | [optional] 

## Example

```python
from cyperf.models.diagnostic_component_context import DiagnosticComponentContext

# TODO update the JSON string below
json = "{}"
# create an instance of DiagnosticComponentContext from a JSON string
diagnostic_component_context_instance = DiagnosticComponentContext.from_json(json)
# print the JSON string representation of the object
print(DiagnosticComponentContext.to_json())

# convert the object into a dict
diagnostic_component_context_dict = diagnostic_component_context_instance.to_dict()
# create an instance of DiagnosticComponentContext from a dict
diagnostic_component_context_from_dict = DiagnosticComponentContext.from_dict(diagnostic_component_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


