# ValidationMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**severity** | **str** |  | 

## Example

```python
from cyperf.models.validation_message import ValidationMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationMessage from a JSON string
validation_message_instance = ValidationMessage.from_json(json)
# print the JSON string representation of the object
print(ValidationMessage.to_json())

# convert the object into a dict
validation_message_dict = validation_message_instance.to_dict()
# create an instance of ValidationMessage from a dict
validation_message_from_dict = ValidationMessage.from_dict(validation_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


