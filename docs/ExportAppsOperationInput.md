# ExportAppsOperationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_ids** | [**List[AppId]**](AppId.md) | An optional list of applications to be included. All are included if the list is empty. | [optional] 

## Example

```python
from cyperf.models.export_apps_operation_input import ExportAppsOperationInput

# TODO update the JSON string below
json = "{}"
# create an instance of ExportAppsOperationInput from a JSON string
export_apps_operation_input_instance = ExportAppsOperationInput.from_json(json)
# print the JSON string representation of the object
print(ExportAppsOperationInput.to_json())

# convert the object into a dict
export_apps_operation_input_dict = export_apps_operation_input_instance.to_dict()
# create an instance of ExportAppsOperationInput from a dict
export_apps_operation_input_from_dict = ExportAppsOperationInput.from_dict(export_apps_operation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


