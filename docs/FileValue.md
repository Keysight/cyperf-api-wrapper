# FileValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | The name of the file. | [optional] 
**payload** | **List[bytearray]** | The payload value of the file. | [optional] 
**resource_url** | **str** | The resource URL of the file. | [optional] 
**value** | **str** | Selected column name of the file (playlist type). | [optional] 

## Example

```python
from cyperf.models.file_value import FileValue

# TODO update the JSON string below
json = "{}"
# create an instance of FileValue from a JSON string
file_value_instance = FileValue.from_json(json)
# print the JSON string representation of the object
print(FileValue.to_json())

# convert the object into a dict
file_value_dict = file_value_instance.to_dict()
# create an instance of FileValue from a dict
file_value_from_dict = FileValue.from_dict(file_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


