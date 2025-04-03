# ExportFilesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** | The ID of the agent | [optional] 
**required_file_types** | [**RequiredFileTypes**](RequiredFileTypes.md) |  | [optional] 
**upload_location** | **str** | The URL to which the agent will send its exported files via a POST request | [optional] 

## Example

```python
from cyperf.models.export_files_request import ExportFilesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExportFilesRequest from a JSON string
export_files_request_instance = ExportFilesRequest.from_json(json)
# print the JSON string representation of the object
print(ExportFilesRequest.to_json())

# convert the object into a dict
export_files_request_dict = export_files_request_instance.to_dict()
# create an instance of ExportFilesRequest from a dict
export_files_request_from_dict = ExportFilesRequest.from_dict(export_files_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


