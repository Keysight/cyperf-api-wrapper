# ParamMetadataTypeInfoArrayV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elements** | [**List[ParamMetadataTypeInfoArrayV2ElementsInner]**](ParamMetadataTypeInfoArrayV2ElementsInner.md) |  | [optional] 

## Example

```python
from cyperf.models.param_metadata_type_info_array_v2 import ParamMetadataTypeInfoArrayV2

# TODO update the JSON string below
json = "{}"
# create an instance of ParamMetadataTypeInfoArrayV2 from a JSON string
param_metadata_type_info_array_v2_instance = ParamMetadataTypeInfoArrayV2.from_json(json)
# print the JSON string representation of the object
print(ParamMetadataTypeInfoArrayV2.to_json())

# convert the object into a dict
param_metadata_type_info_array_v2_dict = param_metadata_type_info_array_v2_instance.to_dict()
# create an instance of ParamMetadataTypeInfoArrayV2 from a dict
param_metadata_type_info_array_v2_from_dict = ParamMetadataTypeInfoArrayV2.from_dict(param_metadata_type_info_array_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


