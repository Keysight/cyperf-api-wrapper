# ParamMetadataTypeInfoString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charset** | **str** |  | [optional] 
**max_length** | **int** |  | [optional] 
**min_length** | **int** |  | [optional] 

## Example

```python
from cyperf.models.param_metadata_type_info_string import ParamMetadataTypeInfoString

# TODO update the JSON string below
json = "{}"
# create an instance of ParamMetadataTypeInfoString from a JSON string
param_metadata_type_info_string_instance = ParamMetadataTypeInfoString.from_json(json)
# print the JSON string representation of the object
print(ParamMetadataTypeInfoString.to_json())

# convert the object into a dict
param_metadata_type_info_string_dict = param_metadata_type_info_string_instance.to_dict()
# create an instance of ParamMetadataTypeInfoString from a dict
param_metadata_type_info_string_from_dict = ParamMetadataTypeInfoString.from_dict(param_metadata_type_info_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


