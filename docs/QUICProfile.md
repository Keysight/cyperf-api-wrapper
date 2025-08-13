# QUICProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_tls_profile** | [**TLSProfile**](TLSProfile.md) |  | [optional] 
**min_rto** | **int** |  | [optional] 
**name** | **str** | The name of the QUIC profile. | [optional] 
**quic_version** | [**QUICVersion**](QUICVersion.md) |  | [optional] 
**rx_buffer** | **int** |  | [optional] 
**server_tls_profile** | [**TLSProfile**](TLSProfile.md) |  | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.quic_profile import QUICProfile

# TODO update the JSON string below
json = "{}"
# create an instance of QUICProfile from a JSON string
quic_profile_instance = QUICProfile.from_json(json)
# print the JSON string representation of the object
print(QUICProfile.to_json())

# convert the object into a dict
quic_profile_dict = quic_profile_instance.to_dict()
# create an instance of QUICProfile from a dict
quic_profile_from_dict = QUICProfile.from_dict(quic_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


