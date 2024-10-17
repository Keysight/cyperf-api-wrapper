# LogConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **str** | The current global log level | [optional] 

## Example

```python
from cyperf.models.log_config import LogConfig

# TODO update the JSON string below
json = "{}"
# create an instance of LogConfig from a JSON string
log_config_instance = LogConfig.from_json(json)
# print the JSON string representation of the object
print(LogConfig.to_json())

# convert the object into a dict
log_config_dict = log_config_instance.to_dict()
# create an instance of LogConfig from a dict
log_config_from_dict = LogConfig.from_dict(log_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


