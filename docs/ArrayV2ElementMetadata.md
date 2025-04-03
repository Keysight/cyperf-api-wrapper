# ArrayV2ElementMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the element | [optional] 
**type** | **str** | The type of the element | [optional] 

## Example

```python
from cyperf.models.array_v2_element_metadata import ArrayV2ElementMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayV2ElementMetadata from a JSON string
array_v2_element_metadata_instance = ArrayV2ElementMetadata.from_json(json)
# print the JSON string representation of the object
print(ArrayV2ElementMetadata.to_json())

# convert the object into a dict
array_v2_element_metadata_dict = array_v2_element_metadata_instance.to_dict()
# create an instance of ArrayV2ElementMetadata from a dict
array_v2_element_metadata_from_dict = ArrayV2ElementMetadata.from_dict(array_v2_element_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


