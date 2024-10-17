# Params


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_elements** | **List[Dict[str, str]]** |  | [optional] 
**array_element_type** | **str** | The type of the array elements. | [optional] 
**category** | **str** | The category associated with the parameter | [optional] 
**category_index** | **int** | The position of the category in the category list | [optional] 
**deprecated_previous_source** | **str** | A value indicating that this parameter had a source that was deprecated | [optional] 
**description** | **str** | The description of the parameter | [optional] 
**dictionary_value** | **Dict[str, str]** | The dictionary value of the parameter. | [optional] 
**enum** | [**ParamsEnum**](ParamsEnum.md) |  | [optional] 
**file_upload** | **List[bytearray]** |  | [optional] 
**file_value** | [**FileValue**](FileValue.md) |  | [optional] 
**flow_identifier** | **bool** | If true, the value of this parameter is used to uniquely identify an application/attack | [optional] 
**id** | **str** |  | 
**is_deprecated** | **bool** |  | [optional] 
**is_modified** | **bool** |  | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**media_files** | [**List[MediaFile]**](MediaFile.md) |  | [optional] 
**metadata** | [**ParamMetadata**](ParamMetadata.md) |  | [optional] 
**name** | **str** | The name of the parameter. | [optional] 
**param_id** | **str** | The id of the parameter. | [optional] 
**readonly** | **bool** |  | [optional] 
**source** | **str** | The source of the parameter. | [optional] 
**supported_sources** | **List[str]** | A list that indicates possible sources for the parameter | [optional] 
**supports_dynamic_payload** | **bool** | A value that indicates if the parameter can have dynamic payload. | [optional] 
**type** | **str** | The type of the parameter. | [optional] 
**upload_url** | **str** | The URL where the file parameter content could be uploaded. | [optional] 
**value** | **str** | The value of the parameter. | [optional] 

## Example

```python
from cyperf.models.params import Params

# TODO update the JSON string below
json = "{}"
# create an instance of Params from a JSON string
params_instance = Params.from_json(json)
# print the JSON string representation of the object
print(Params.to_json())

# convert the object into a dict
params_dict = params_instance.to_dict()
# create an instance of Params from a dict
params_from_dict = Params.from_dict(params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


