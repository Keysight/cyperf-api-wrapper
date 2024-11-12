# AppsecConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**Config**](Config.md) |  | [optional] 
**session_id** | **str** | The unique identifier of the session this configuration belongs to | [optional] [readonly] 
**template_id** | **str** | The unique identifier of the CyPerf configuration template from which this configuration was created | [optional] [readonly] 
**config_type_name** | **str** | Used for API clients to decide what type of config they have loaded | 
**data_model_version** | **str** | The version of the data model used for this configuration | [optional] [readonly] 
**id** | **str** | The unique identifier of the CyPerf configuration | [optional] [readonly] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**name** | **str** | The name of the configuration | [optional] 

## Example

```python
from cyperf.models.appsec_config import AppsecConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppsecConfig from a JSON string
appsec_config_instance = AppsecConfig.from_json(json)
# print the JSON string representation of the object
print(AppsecConfig.to_json())

# convert the object into a dict
appsec_config_dict = appsec_config_instance.to_dict()
# create an instance of AppsecConfig from a dict
appsec_config_from_dict = AppsecConfig.from_dict(appsec_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


