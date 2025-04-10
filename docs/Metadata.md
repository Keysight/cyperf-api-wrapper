# Metadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** | The direction of the strike | [optional] 
**is_banner** | **bool** | Indicates that this is a command that is required, can only be add once and also must be the first | [optional] 
**keywords** | [**List[ConfigMetadataConfigDataValue]**](ConfigMetadataConfigDataValue.md) | The keywords of the strike | [optional] 
**legacy_names** | **List[str]** | The names of the equivalent application/strike | [optional] 
**protocol** | **str** | The protocol of the strike | [optional] 
**rtp_profile_meta** | [**RTPProfileMeta**](RTPProfileMeta.md) |  | [optional] 
**references** | [**List[Reference]**](Reference.md) | The references of the strike | [optional] 
**requires_uniqueness** | **bool** | If true, for applications with the same protocol id, application/attack must have been uniquely identified in previous commands | [optional] 
**severity** | **str** | The severity of the strike | [optional] 
**skip_attack_generation** | **bool** | If true, don&#39;t generate an attack for this strike | [optional] 
**sort_severity** | **str** | The field by which the severity is sorted | [optional] 
**static** | **bool** | If true, the application/strike is managed directly by the controller | [optional] 
**supported_apps** | **List[str]** | The apps that this strike can be used with | [optional] 
**year** | **str** | The year of the strike | [optional] 

## Example

```python
from cyperf.models.metadata import Metadata

# TODO update the JSON string below
json = "{}"
# create an instance of Metadata from a JSON string
metadata_instance = Metadata.from_json(json)
# print the JSON string representation of the object
print(Metadata.to_json())

# convert the object into a dict
metadata_dict = metadata_instance.to_dict()
# create an instance of Metadata from a dict
metadata_from_dict = Metadata.from_dict(metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


