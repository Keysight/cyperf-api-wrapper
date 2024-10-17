# ArchiveInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | The name of the archive. | 
**id** | **int** | The subresource id of the status. | 
**message** | **str** | A message from the operation (optional). | 
**result_url** | **str** | The URL where the archive is available. | 
**size** | **int** | The size in bytes of the archive. | [optional] 
**state** | **str** | The state of the archive/collection. | 
**timestamp** | **str** | The timestamp of archive creation. | 
**url** | **str** | The URL to get the status of the archive. | 

## Example

```python
from cyperf.models.archive_info import ArchiveInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArchiveInfo from a JSON string
archive_info_instance = ArchiveInfo.from_json(json)
# print the JSON string representation of the object
print(ArchiveInfo.to_json())

# convert the object into a dict
archive_info_dict = archive_info_instance.to_dict()
# create an instance of ArchiveInfo from a dict
archive_info_from_dict = ArchiveInfo.from_dict(archive_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


