# ConfigValidation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_validated** | **bool** |  | 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**validation_messages** | [**List[ValidationMessage]**](ValidationMessage.md) |  | [optional] 

## Example

```python
from cyperf.models.config_validation import ConfigValidation

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigValidation from a JSON string
config_validation_instance = ConfigValidation.from_json(json)
# print the JSON string representation of the object
print(ConfigValidation.to_json())

# convert the object into a dict
config_validation_dict = config_validation_instance.to_dict()
# create an instance of ConfigValidation from a dict
config_validation_from_dict = ConfigValidation.from_dict(config_validation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


