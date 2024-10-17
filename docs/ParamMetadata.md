# ParamMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_info** | [**ParamMetadataTypeInfo**](ParamMetadataTypeInfo.md) |  | [optional] 

## Example

```python
from cyperf.models.param_metadata import ParamMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ParamMetadata from a JSON string
param_metadata_instance = ParamMetadata.from_json(json)
# print the JSON string representation of the object
print(ParamMetadata.to_json())

# convert the object into a dict
param_metadata_dict = param_metadata_instance.to_dict()
# create an instance of ParamMetadata from a dict
param_metadata_from_dict = ParamMetadata.from_dict(param_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


