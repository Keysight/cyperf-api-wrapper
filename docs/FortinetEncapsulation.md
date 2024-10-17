# FortinetEncapsulation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encapsulation_mode** | **str** | The encapsulation mode for inner traffic. | 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**ppp_over_dtls_enabled** | **bool** |  | 
**ppp_over_dtls_settings** | [**DTLSSettings**](DTLSSettings.md) |  | [optional] 
**udp_port** | **int** |  | 

## Example

```python
from cyperf.models.fortinet_encapsulation import FortinetEncapsulation

# TODO update the JSON string below
json = "{}"
# create an instance of FortinetEncapsulation from a JSON string
fortinet_encapsulation_instance = FortinetEncapsulation.from_json(json)
# print the JSON string representation of the object
print(FortinetEncapsulation.to_json())

# convert the object into a dict
fortinet_encapsulation_dict = fortinet_encapsulation_instance.to_dict()
# create an instance of FortinetEncapsulation from a dict
fortinet_encapsulation_from_dict = FortinetEncapsulation.from_dict(fortinet_encapsulation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


