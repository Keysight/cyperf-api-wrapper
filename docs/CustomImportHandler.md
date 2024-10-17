# CustomImportHandler


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | [**APILink**](APILink.md) |  | [optional] 
**name** | **str** | The name of the custom import config operation | [optional] 

## Example

```python
from cyperf.models.custom_import_handler import CustomImportHandler

# TODO update the JSON string below
json = "{}"
# create an instance of CustomImportHandler from a JSON string
custom_import_handler_instance = CustomImportHandler.from_json(json)
# print the JSON string representation of the object
print(CustomImportHandler.to_json())

# convert the object into a dict
custom_import_handler_dict = custom_import_handler_instance.to_dict()
# create an instance of CustomImportHandler from a dict
custom_import_handler_from_dict = CustomImportHandler.from_dict(custom_import_handler_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


