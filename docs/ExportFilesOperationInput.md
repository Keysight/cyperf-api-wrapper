# ExportFilesOperationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**export_files_requests_by_agent** | **Dict[str, List[ExportFilesRequest]]** |  | [optional] 
**timeout** | **int** | Maximum waiting time in seconds to complete the agent file export operation | [optional] 

## Example

```python
from cyperf.models.export_files_operation_input import ExportFilesOperationInput

# TODO update the JSON string below
json = "{}"
# create an instance of ExportFilesOperationInput from a JSON string
export_files_operation_input_instance = ExportFilesOperationInput.from_json(json)
# print the JSON string representation of the object
print(ExportFilesOperationInput.to_json())

# convert the object into a dict
export_files_operation_input_dict = export_files_operation_input_instance.to_dict()
# create an instance of ExportFilesOperationInput from a dict
export_files_operation_input_from_dict = ExportFilesOperationInput.from_dict(export_files_operation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


