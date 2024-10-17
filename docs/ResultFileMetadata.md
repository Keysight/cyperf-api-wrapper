# ResultFileMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | The file ID of the saved file, can be agentID | [optional] [readonly] 
**file_name** | **str** | The name of the file associated with the result | [optional] 
**id** | **str** | The unique ID of the saved result | [optional] [readonly] 
**last_modified** | **int** | The time when the result was last modified | [optional] [readonly] 
**result_id** | **str** | The unique ID of the saved result | [optional] [readonly] 
**type** | **str** | Represents the type of the file | [optional] [readonly] 

## Example

```python
from cyperf.models.result_file_metadata import ResultFileMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ResultFileMetadata from a JSON string
result_file_metadata_instance = ResultFileMetadata.from_json(json)
# print the JSON string representation of the object
print(ResultFileMetadata.to_json())

# convert the object into a dict
result_file_metadata_dict = result_file_metadata_instance.to_dict()
# create an instance of ResultFileMetadata from a dict
result_file_metadata_from_dict = ResultFileMetadata.from_dict(result_file_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


