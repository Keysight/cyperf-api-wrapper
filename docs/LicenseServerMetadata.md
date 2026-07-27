# LicenseServerMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_status** | **str** |  | [optional] 
**failure_reason** | **str** |  | [optional] 
**fingerprint** | **str** |  | [optional] 
**host_name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**interactive_fingerprint_verification** | **bool** |  | [optional] 
**password** | **str** |  | [optional] 
**pretty_conn_status** | **str** |  | [optional] 
**trust_new** | **bool** |  | [optional] 
**tunnel_host_name** | **str** |  | [optional] 
**user** | **str** |  | [optional] 

## Example

```python
from cyperf.models.license_server_metadata import LicenseServerMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseServerMetadata from a JSON string
license_server_metadata_instance = LicenseServerMetadata.from_json(json)
# print the JSON string representation of the object
print(LicenseServerMetadata.to_json())

# convert the object into a dict
license_server_metadata_dict = license_server_metadata_instance.to_dict()
# create an instance of LicenseServerMetadata from a dict
license_server_metadata_from_dict = LicenseServerMetadata.from_dict(license_server_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


