# PayloadMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**byte_size** | **int** |  | [optional] 
**content_file_url** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**md5sum** | **str** |  | [optional] 
**resource_url** | **str** |  | [optional] 

## Example

```python
from cyperf.models.payload_meta import PayloadMeta

# TODO update the JSON string below
json = "{}"
# create an instance of PayloadMeta from a JSON string
payload_meta_instance = PayloadMeta.from_json(json)
# print the JSON string representation of the object
print(PayloadMeta.to_json())

# convert the object into a dict
payload_meta_dict = payload_meta_instance.to_dict()
# create an instance of PayloadMeta from a dict
payload_meta_from_dict = PayloadMeta.from_dict(payload_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


