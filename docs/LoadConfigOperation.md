# LoadConfigOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_url** | **str** | The URL of the configuration that should be loaded | [optional] 

## Example

```python
from cyperf.models.load_config_operation import LoadConfigOperation

# TODO update the JSON string below
json = "{}"
# create an instance of LoadConfigOperation from a JSON string
load_config_operation_instance = LoadConfigOperation.from_json(json)
# print the JSON string representation of the object
print(LoadConfigOperation.to_json())

# convert the object into a dict
load_config_operation_dict = load_config_operation_instance.to_dict()
# create an instance of LoadConfigOperation from a dict
load_config_operation_from_dict = LoadConfigOperation.from_dict(load_config_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


