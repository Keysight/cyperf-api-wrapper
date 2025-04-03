# ImportAllOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configs** | [**List[ConfigMetadata]**](ConfigMetadata.md) | The list of configurations to be imported | [optional] 

## Example

```python
from cyperf.models.import_all_operation import ImportAllOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ImportAllOperation from a JSON string
import_all_operation_instance = ImportAllOperation.from_json(json)
# print the JSON string representation of the object
print(ImportAllOperation.to_json())

# convert the object into a dict
import_all_operation_dict = import_all_operation_instance.to_dict()
# create an instance of ImportAllOperation from a dict
import_all_operation_from_dict = ImportAllOperation.from_dict(import_all_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


