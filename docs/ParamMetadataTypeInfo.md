# ParamMetadataTypeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_v2** | [**ParamMetadataTypeInfoArrayV2**](ParamMetadataTypeInfoArrayV2.md) |  | [optional] 
**int** | [**ParamMetadataTypeInfoInt**](ParamMetadataTypeInfoInt.md) |  | [optional] 
**media** | [**ParamMetadataTypeInfoMedia**](ParamMetadataTypeInfoMedia.md) |  | [optional] 
**string** | [**ParamMetadataTypeInfoString**](ParamMetadataTypeInfoString.md) |  | [optional] 

## Example

```python
from cyperf.models.param_metadata_type_info import ParamMetadataTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ParamMetadataTypeInfo from a JSON string
param_metadata_type_info_instance = ParamMetadataTypeInfo.from_json(json)
# print the JSON string representation of the object
print(ParamMetadataTypeInfo.to_json())

# convert the object into a dict
param_metadata_type_info_dict = param_metadata_type_info_instance.to_dict()
# create an instance of ParamMetadataTypeInfo from a dict
param_metadata_type_info_from_dict = ParamMetadataTypeInfo.from_dict(param_metadata_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


