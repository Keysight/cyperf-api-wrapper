# F5Encapsulation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encapsulation_mode** | **str** | The encapsulation mode for inner traffic. | 
**ppp_over_dtls_enabled** | **bool** |  | 
**ppp_over_dtls_settings** | [**DTLSSettings**](DTLSSettings.md) |  | [optional] 
**udp_port** | **int** |  | 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.f5_encapsulation import F5Encapsulation

# TODO update the JSON string below
json = "{}"
# create an instance of F5Encapsulation from a JSON string
f5_encapsulation_instance = F5Encapsulation.from_json(json)
# print the JSON string representation of the object
print(F5Encapsulation.to_json())

# convert the object into a dict
f5_encapsulation_dict = f5_encapsulation_instance.to_dict()
# create an instance of F5Encapsulation from a dict
f5_encapsulation_from_dict = F5Encapsulation.from_dict(f5_encapsulation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


