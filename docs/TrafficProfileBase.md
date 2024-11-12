# TrafficProfileBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Indicates whether the profile is enabled or not. | [optional] 
**traffic_settings** | [**TrafficSettings**](TrafficSettings.md) |  | [optional] 
**id** | **str** |  | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.traffic_profile_base import TrafficProfileBase

# TODO update the JSON string below
json = "{}"
# create an instance of TrafficProfileBase from a JSON string
traffic_profile_base_instance = TrafficProfileBase.from_json(json)
# print the JSON string representation of the object
print(TrafficProfileBase.to_json())

# convert the object into a dict
traffic_profile_base_dict = traffic_profile_base_instance.to_dict()
# create an instance of TrafficProfileBase from a dict
traffic_profile_base_from_dict = TrafficProfileBase.from_dict(traffic_profile_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


