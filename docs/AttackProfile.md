# AttackProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Indicates whether the profile is enabled or not. | [optional] 
**traffic_settings** | [**TrafficSettings**](TrafficSettings.md) |  | [optional] 
**id** | **str** |  | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**attacks** | [**List[Attack]**](Attack.md) |  | [optional] 
**default_network_mapping** | [**NetworkMapping**](NetworkMapping.md) |  | [optional] 
**name** | **str** |  | 
**objectives_and_timeline** | [**AttackObjectivesAndTimeline**](AttackObjectivesAndTimeline.md) |  | [optional] 
**add_attacks** | [**List[ExternalResourceInfo]**](ExternalResourceInfo.md) |  | [optional] 
**modify_excluded_dut_recursively** | [**List[UpdateNetworkMapping]**](UpdateNetworkMapping.md) |  | [optional] 
**modify_tags_recursively** | [**List[UpdateNetworkMapping]**](UpdateNetworkMapping.md) |  | [optional] 
**reset_tags_to_default** | **List[bytearray]** |  | [optional] 

## Example

```python
from cyperf.models.attack_profile import AttackProfile

# TODO update the JSON string below
json = "{}"
# create an instance of AttackProfile from a JSON string
attack_profile_instance = AttackProfile.from_json(json)
# print the JSON string representation of the object
print(AttackProfile.to_json())

# convert the object into a dict
attack_profile_dict = attack_profile_instance.to_dict()
# create an instance of AttackProfile from a dict
attack_profile_from_dict = AttackProfile.from_dict(attack_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


