# PayloadMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_extension** | **str** | The extension of the file | [optional] 
**file_name** | **str** | The path of the file | [optional] 
**file_type** | **str** | The type of the file | [optional] 
**file_url** | **str** | The relative URL of the file | [optional] 

## Example

```python
from cyperf.models.payload_metadata import PayloadMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of PayloadMetadata from a JSON string
payload_metadata_instance = PayloadMetadata.from_json(json)
# print the JSON string representation of the object
print(PayloadMetadata.to_json())

# convert the object into a dict
payload_metadata_dict = payload_metadata_instance.to_dict()
# create an instance of PayloadMetadata from a dict
payload_metadata_from_dict = PayloadMetadata.from_dict(payload_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


