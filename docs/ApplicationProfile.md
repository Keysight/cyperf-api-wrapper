# ApplicationProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Indicates whether the profile is enabled or not. | [optional] 
**id** | **str** |  | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**traffic_settings** | [**TrafficSettings**](TrafficSettings.md) |  | [optional] 
**add_applications** | [**List[ExternalResourceInfo]**](ExternalResourceInfo.md) |  | [optional] 
**applications** | [**List[Application]**](Application.md) |  | [optional] 
**default_network_mapping** | [**NetworkMapping**](NetworkMapping.md) |  | [optional] 
**modify_excluded_dut_recursively** | [**List[UpdateNetworkMapping]**](UpdateNetworkMapping.md) |  | [optional] 
**modify_tags_recursively** | [**List[UpdateNetworkMapping]**](UpdateNetworkMapping.md) |  | [optional] 
**name** | **str** |  | 
**objectives_and_timeline** | [**ObjectivesAndTimeline**](ObjectivesAndTimeline.md) |  | [optional] 
**reset_tags_to_default** | **List[bytearray]** |  | [optional] 

## Example

```python
from cyperf.models.application_profile import ApplicationProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationProfile from a JSON string
application_profile_instance = ApplicationProfile.from_json(json)
# print the JSON string representation of the object
print(ApplicationProfile.to_json())

# convert the object into a dict
application_profile_dict = application_profile_instance.to_dict()
# create an instance of ApplicationProfile from a dict
application_profile_from_dict = ApplicationProfile.from_dict(application_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


