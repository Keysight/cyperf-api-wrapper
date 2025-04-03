# ConfigMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | **str** |  | [optional] 
**config_data** | [**Dict[str, ConfigMetadataConfigDataValue]**](ConfigMetadataConfigDataValue.md) | The actual configuration object | [optional] 
**config_url** | **str** | The backend URL of the saved config data | [optional] 
**created_on** | **int** | A Unix timestamp that indicates when config was created | [optional] [readonly] 
**display_name** | **str** | The user-visible name of the configuration | [optional] 
**encoded_files** | **bool** |  | [optional] 
**id** | **str** | The unique identifier of the configuration | [optional] [readonly] 
**last_accessed** | **int** | A Unix timestamp that indicates when config was last opened or modified | [optional] 
**last_modified** | **int** | A Unix timestamp that indicates when config was last modified | [optional] [readonly] 
**linked_resources** | [**List[APILink]**](APILink.md) |  | [optional] 
**owner** | **str** | A user-friendly display name of the config&#39;s owner | [optional] [readonly] 
**owner_id** | **str** | The unique identifier of the config&#39;s owner | [optional] [readonly] 
**readonly** | **bool** | Indicates if the configuration can be modified. | [optional] [readonly] 
**tags** | **Dict[str, str]** | Tags used for categorizing configs | [optional] 
**type** | **str** | The type of config | [optional] [readonly] 
**version** | [**Version**](Version.md) |  | [optional] 

## Example

```python
from cyperf.models.config_metadata import ConfigMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigMetadata from a JSON string
config_metadata_instance = ConfigMetadata.from_json(json)
# print the JSON string representation of the object
print(ConfigMetadata.to_json())

# convert the object into a dict
config_metadata_dict = config_metadata_instance.to_dict()
# create an instance of ConfigMetadata from a dict
config_metadata_from_dict = ConfigMetadata.from_dict(config_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


