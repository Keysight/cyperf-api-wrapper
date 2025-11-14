# Md2Tlv


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**md2_class** | **int** |  | 
**md2_type** | **int** |  | 
**md2_value** | **int** |  | 
**id** | **str** |  | 

## Example

```python
from cyperf.models.md2_tlv import Md2Tlv

# TODO update the JSON string below
json = "{}"
# create an instance of Md2Tlv from a JSON string
md2_tlv_instance = Md2Tlv.from_json(json)
# print the JSON string representation of the object
print(Md2Tlv.to_json())

# convert the object into a dict
md2_tlv_dict = md2_tlv_instance.to_dict()
# create an instance of Md2Tlv from a dict
md2_tlv_from_dict = Md2Tlv.from_dict(md2_tlv_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


