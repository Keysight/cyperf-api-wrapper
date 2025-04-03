# CiscoEncapsulation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dtls_enabled** | **bool** |  | 
**dtls_settings** | [**DTLSSettings**](DTLSSettings.md) |  | [optional] 
**encapsulation_mode** | **str** | The encapsulation mode for inner traffic. | 
**udp_port** | **int** |  | 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.cisco_encapsulation import CiscoEncapsulation

# TODO update the JSON string below
json = "{}"
# create an instance of CiscoEncapsulation from a JSON string
cisco_encapsulation_instance = CiscoEncapsulation.from_json(json)
# print the JSON string representation of the object
print(CiscoEncapsulation.to_json())

# convert the object into a dict
cisco_encapsulation_dict = cisco_encapsulation_instance.to_dict()
# create an instance of CiscoEncapsulation from a dict
cisco_encapsulation_from_dict = CiscoEncapsulation.from_dict(cisco_encapsulation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


