# GenericFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **bytearray** | The content of the file | [optional] 
**id** | **str** | The unique identifier for the file | [optional] [readonly] 
**md5** | **str** | The md5 value of the file | [optional] 
**metadata** | [**FileMetadata**](FileMetadata.md) |  | [optional] 
**name** | **str** | The name of the file | [optional] 
**options** | [**Dict[str, ConfigMetadataConfigDataValue]**](ConfigMetadataConfigDataValue.md) | The characteristics of the file | [optional] 
**owner** | **str** | The user-visible name of the file&#39;s owner | [optional] [readonly] 
**owner_id** | **str** | The unique identifier of the file&#39;s owner | [optional] [readonly] 
**reference_links** | **Dict[str, int]** |  | [optional] 
**size** | **int** | The size of the file | [optional] 
**type** | **str** | The type of file | [optional] [readonly] 

## Example

```python
from cyperf.models.generic_file import GenericFile

# TODO update the JSON string below
json = "{}"
# create an instance of GenericFile from a JSON string
generic_file_instance = GenericFile.from_json(json)
# print the JSON string representation of the object
print(GenericFile.to_json())

# convert the object into a dict
generic_file_dict = generic_file_instance.to_dict()
# create an instance of GenericFile from a dict
generic_file_from_dict = GenericFile.from_dict(generic_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


