# ExportAllOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_ids** | [**List[ConfigId]**](ConfigId.md) | An optional list of configs to be include. All are included if the list is empty. | [optional] 

## Example

```python
from cyperf.models.export_all_operation import ExportAllOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ExportAllOperation from a JSON string
export_all_operation_instance = ExportAllOperation.from_json(json)
# print the JSON string representation of the object
print(ExportAllOperation.to_json())

# convert the object into a dict
export_all_operation_dict = export_all_operation_instance.to_dict()
# create an instance of ExportAllOperation from a dict
export_all_operation_from_dict = ExportAllOperation.from_dict(export_all_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


