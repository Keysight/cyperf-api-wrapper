# TLSProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_file** | [**Params**](Params.md) | The certificate file of the TLS profile. | [optional] 
**cipher** | [**CipherTLS12**](CipherTLS12.md) |  | [optional] 
**cipher12** | [**CipherTLS12**](CipherTLS12.md) |  | [optional] 
**cipher13** | [**CipherTLS13**](CipherTLS13.md) |  | [optional] 
**ciphers12** | [**List[CipherTLS12]**](CipherTLS12.md) |  | [optional] 
**ciphers13** | [**List[CipherTLS13]**](CipherTLS13.md) |  | [optional] 
**dh_file** | [**Params**](Params.md) |  | [optional] 
**get_tls_conflicts** | **List[bytearray]** |  | [optional] 
**immediate_close** | **bool** | The immediate FIN after close notify | [optional] 
**key_file** | [**Params**](Params.md) | The key file of the TLS profile. | [optional] 
**key_file_password** | **str** | The key file password of the TLS profile. | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**middle_box_enabled** | **bool** | If true, the middle box compatibility will be enabled | [optional] 
**profile_id** | **str** | The ID of the TLS profile (default: TLSProfile). | 
**resolve_tls_conflicts** | [**List[Conflict]**](Conflict.md) |  | [optional] 
**send_close_notify** | **bool** | If true, a TLS close-notify alert will be sent while closing the TLS session | [optional] 
**session_reuse_count** | **int** |  | [optional] 
**session_reuse_method** | [**SessionReuseMethodTLS12**](SessionReuseMethodTLS12.md) |  | [optional] 
**session_reuse_method12** | [**SessionReuseMethodTLS12**](SessionReuseMethodTLS12.md) |  | [optional] 
**session_reuse_method13** | [**SessionReuseMethodTLS13**](SessionReuseMethodTLS13.md) |  | [optional] 
**sni_cert_configs** | [**List[CertConfig]**](CertConfig.md) | The certificate configs per SNI of the TLS profile. | [optional] 
**sni_enabled** | **bool** | The enable status of the SNI configuration (default: false). | 
**supported_groups13** | [**List[SupportedGroupTLS13]**](SupportedGroupTLS13.md) |  | [optional] 
**tls12_enabled** | **bool** |  | 
**tls13_enabled** | **bool** |  | [optional] 
**use_tls_profile** | **bool** | When disabled, the connection is not TLS secured (default: true). | [optional] 
**version** | **str** | The version of the TLS profile (default: NONE). Must be one of: NONE or TLSv1.2 or TLSv1.3. | 

## Example

```python
from cyperf.models.tls_profile import TLSProfile

# TODO update the JSON string below
json = "{}"
# create an instance of TLSProfile from a JSON string
tls_profile_instance = TLSProfile.from_json(json)
# print the JSON string representation of the object
print(TLSProfile.to_json())

# convert the object into a dict
tls_profile_dict = tls_profile_instance.to_dict()
# create an instance of TLSProfile from a dict
tls_profile_from_dict = TLSProfile.from_dict(tls_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


