# TrafficSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_transport_profile** | [**TransportProfile**](TransportProfile.md) |  | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.traffic_settings import TrafficSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TrafficSettings from a JSON string
traffic_settings_instance = TrafficSettings.from_json(json)
# print the JSON string representation of the object
print(TrafficSettings.to_json())

# convert the object into a dict
traffic_settings_dict = traffic_settings_instance.to_dict()
# create an instance of TrafficSettings from a dict
traffic_settings_from_dict = TrafficSettings.from_dict(traffic_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


