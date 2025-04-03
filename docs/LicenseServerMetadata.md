# LicenseServerMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_status** | **str** | The license server&#39;s connection status | [optional] [readonly] 
**fingerprint** | **str** | The license server&#39;s fingerprint | [optional] 
**host_name** | **str** | The hostname/IP of the server | [optional] 
**id** | **int** | The unique identifier of the license server | [optional] [readonly] 
**interactive_fingerprint_verification** | **bool** | Validate the license&#39;s server fingerprint interactively | [optional] 
**password** | **str** | The license server&#39;s authentication password | [optional] 
**pretty_conn_status** | **str** | The license server&#39;s connection status in a human-readable format | [optional] [readonly] 
**trust_new** | **bool** | The flag used to skip license server&#39;s identity verifications | [optional] 
**tunnel_host_name** | **str** | The hostname/IP of the license server tunnel | [optional] [readonly] 
**user** | **str** | The license server&#39;s authentication user | [optional] 

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


