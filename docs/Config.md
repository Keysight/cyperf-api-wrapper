# Config

The test configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attack_profiles** | [**List[AttackProfile]**](AttackProfile.md) |  | [optional] 
**config_validation** | [**ConfigValidation**](ConfigValidation.md) |  | [optional] 
**custom_dashboards** | [**CustomDashboards**](CustomDashboards.md) |  | [optional] 
**expected_disk_space** | [**List[ExpectedDiskSpace]**](ExpectedDiskSpace.md) |  | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**network_profiles** | [**List[NetworkProfile]**](NetworkProfile.md) |  | [optional] 
**traffic_profiles** | [**List[ApplicationProfile]**](ApplicationProfile.md) |  | [optional] 
**validate** | **List[bytearray]** |  | [optional] 

## Example

```python
from cyperf.models.config import Config

# TODO update the JSON string below
json = "{}"
# create an instance of Config from a JSON string
config_instance = Config.from_json(json)
# print the JSON string representation of the object
print(Config.to_json())

# convert the object into a dict
config_dict = config_instance.to_dict()
# create an instance of Config from a dict
config_from_dict = Config.from_dict(config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


