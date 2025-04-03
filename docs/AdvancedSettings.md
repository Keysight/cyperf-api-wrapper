# AdvancedSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_optimization_mode** | [**AgentOptimizationMode**](AgentOptimizationMode.md) |  | [optional] 
**agent_streaming_purpose_cpu_percent** | **int** | The CPU percentage reserved for streaming purpose use (default: 0). | [optional] 
**automatic_cpu_percent** | **bool** | Deprecated. Use the calibration operation to find the best value for AgentStreamingPurposeCPUPercent for the current assigned agents. | [optional] 
**connection_graceful_stop_timeout** | **int** | The time the test will wait all connections to be graceful stopped (default: 15 seconds). | [optional] 
**warm_up_period** | **int** | The time that servers may need to warm up, when clients should wait (default: 0 seconds). | 

## Example

```python
from cyperf.models.advanced_settings import AdvancedSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AdvancedSettings from a JSON string
advanced_settings_instance = AdvancedSettings.from_json(json)
# print the JSON string representation of the object
print(AdvancedSettings.to_json())

# convert the object into a dict
advanced_settings_dict = advanced_settings_instance.to_dict()
# create an instance of AdvancedSettings from a dict
advanced_settings_from_dict = AdvancedSettings.from_dict(advanced_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


