# PANGPEncapsulation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**esp_over_udp_enabled** | **bool** |  | 
**esp_over_udp_settings** | [**ESPOverUDPSettings**](ESPOverUDPSettings.md) |  | [optional] 
**encapsulation_mode** | **str** | The encapsulation mode for inner traffic. | 
**udp_port** | **int** |  | 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.pangp_encapsulation import PANGPEncapsulation

# TODO update the JSON string below
json = "{}"
# create an instance of PANGPEncapsulation from a JSON string
pangp_encapsulation_instance = PANGPEncapsulation.from_json(json)
# print the JSON string representation of the object
print(PANGPEncapsulation.to_json())

# convert the object into a dict
pangp_encapsulation_dict = pangp_encapsulation_instance.to_dict()
# create an instance of PANGPEncapsulation from a dict
pangp_encapsulation_from_dict = PANGPEncapsulation.from_dict(pangp_encapsulation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


