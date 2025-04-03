# HealthCheckConfig

The HealthCheck configuration for DUT

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | A flag indicating if the servers should listen for HealthCheck requests (default: true). | [optional] 
**params** | [**List[Params]**](Params.md) | A list of additional parameters for the HealthCheck. | [optional] 
**port** | **int** | The port that the DUT will send HealthCheck requests to the simulated servers. (default: 80) | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.health_check_config import HealthCheckConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HealthCheckConfig from a JSON string
health_check_config_instance = HealthCheckConfig.from_json(json)
# print the JSON string representation of the object
print(HealthCheckConfig.to_json())

# convert the object into a dict
health_check_config_dict = health_check_config_instance.to_dict()
# create an instance of HealthCheckConfig from a dict
health_check_config_from_dict = HealthCheckConfig.from_dict(health_check_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


