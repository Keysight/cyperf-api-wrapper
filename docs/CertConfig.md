# CertConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_file** | [**Params**](Params.md) | The certificate file of the TLS profile. | [optional] 
**dh_file** | [**Params**](Params.md) |  | [optional] 
**get_sni_conflicts** | **List[bytearray]** |  | [optional] 
**id** | **str** |  | 
**is_playlist** | **bool** |  | [optional] 
**key_file** | [**Params**](Params.md) | The key file of the TLS profile. | [optional] 
**key_file_password** | **str** | The key file password of the TLS profile. | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**playlist_column_name** | **str** |  | [optional] 
**playlist_filename** | **str** |  | [optional] 
**resolve_sni_conflicts** | [**List[Conflict]**](Conflict.md) |  | [optional] 
**sni_hostname** | **str** | The SNI hostname associated with the certificate. (default: generic.keysight.io). | 

## Example

```python
from cyperf.models.cert_config import CertConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CertConfig from a JSON string
cert_config_instance = CertConfig.from_json(json)
# print the JSON string representation of the object
print(CertConfig.to_json())

# convert the object into a dict
cert_config_dict = cert_config_instance.to_dict()
# create an instance of CertConfig from a dict
cert_config_from_dict = CertConfig.from_dict(cert_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


