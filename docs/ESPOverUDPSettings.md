# ESPOverUDPSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**udp_profile** | [**UdpProfile**](UdpProfile.md) |  | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.esp_over_udp_settings import ESPOverUDPSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ESPOverUDPSettings from a JSON string
esp_over_udp_settings_instance = ESPOverUDPSettings.from_json(json)
# print the JSON string representation of the object
print(ESPOverUDPSettings.to_json())

# convert the object into a dict
esp_over_udp_settings_dict = esp_over_udp_settings_instance.to_dict()
# create an instance of ESPOverUDPSettings from a dict
esp_over_udp_settings_from_dict = ESPOverUDPSettings.from_dict(esp_over_udp_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


