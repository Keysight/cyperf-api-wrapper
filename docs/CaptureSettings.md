# CaptureSettings

The capture settings for an agent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capture_enabled** | **bool** | The enable status of the capture configuration (default: false). | 
**capture_latest_packets** | **bool** | Capture first or latest packets (true to enable latest packets capture). | [optional] 
**log_level** | [**LogLevel**](LogLevel.md) | Log level options: NONE, ERROR, WARN, INFO, DEBUG, TRACE (default: INFO) | 
**max_capture_size** | **int** | The maximum capture size in bytes (default: 104857600). | [optional] 

## Example

```python
from cyperf.models.capture_settings import CaptureSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CaptureSettings from a JSON string
capture_settings_instance = CaptureSettings.from_json(json)
# print the JSON string representation of the object
print(CaptureSettings.to_json())

# convert the object into a dict
capture_settings_dict = capture_settings_instance.to_dict()
# create an instance of CaptureSettings from a dict
capture_settings_from_dict = CaptureSettings.from_dict(capture_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


