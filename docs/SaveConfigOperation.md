# SaveConfigOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the configuration template that will be saved | [optional] 

## Example

```python
from cyperf.models.save_config_operation import SaveConfigOperation

# TODO update the JSON string below
json = "{}"
# create an instance of SaveConfigOperation from a JSON string
save_config_operation_instance = SaveConfigOperation.from_json(json)
# print the JSON string representation of the object
print(SaveConfigOperation.to_json())

# convert the object into a dict
save_config_operation_dict = save_config_operation_instance.to_dict()
# create an instance of SaveConfigOperation from a dict
save_config_operation_from_dict = SaveConfigOperation.from_dict(save_config_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


