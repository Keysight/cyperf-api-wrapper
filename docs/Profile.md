# Profile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | The category of the profile template. | [optional] 
**config_id** | **str** | The config ID associated with this profile | [optional] 
**description** | **str** | Description of the profile | [optional] 
**display_name** | **str** | Display name of the profile | [optional] 
**icon** | **str** | Profile icon (base64 encoded) | [optional] 
**id** | **str** |  | [optional] 
**index** | **int** | The index of the profile in the list of profiles. This is used for ordering profiles. | [optional] [readonly] 
**owner** | **str** | The friendly display name of the profile&#39;s owner | [optional] [readonly] 
**owner_id** | **str** | The unique identifier of the profile&#39;s owner | [optional] [readonly] 
**topology_img_dark** | **str** | Topology image (dark theme, base64 encoded) | [optional] 
**topology_img_light** | **str** | Topology image (light theme, base64 encoded) | [optional] 

## Example

```python
from cyperf.models.profile import Profile

# TODO update the JSON string below
json = "{}"
# create an instance of Profile from a JSON string
profile_instance = Profile.from_json(json)
# print the JSON string representation of the object
print(Profile.to_json())

# convert the object into a dict
profile_dict = profile_instance.to_dict()
# create an instance of Profile from a dict
profile_from_dict = Profile.from_dict(profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


