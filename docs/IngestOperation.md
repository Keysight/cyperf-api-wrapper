# IngestOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plugin_stats** | [**PluginStats**](PluginStats.md) |  | [optional] 

## Example

```python
from cyperf.models.ingest_operation import IngestOperation

# TODO update the JSON string below
json = "{}"
# create an instance of IngestOperation from a JSON string
ingest_operation_instance = IngestOperation.from_json(json)
# print the JSON string representation of the object
print(IngestOperation.to_json())

# convert the object into a dict
ingest_operation_dict = ingest_operation_instance.to_dict()
# create an instance of IngestOperation from a dict
ingest_operation_from_dict = IngestOperation.from_dict(ingest_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


