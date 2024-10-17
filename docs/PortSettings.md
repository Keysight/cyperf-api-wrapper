# PortSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automatic** | **bool** |  | 
**automatic_destination_port** | **bool** |  | 
**automatic_forward_proxy_port** | **bool** |  | 
**destination_port** | **int** |  | 
**effective_ports** | [**EffectivePorts**](EffectivePorts.md) |  | [optional] 
**forward_proxy_port** | **int** |  | 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**readonly** | **bool** | If true, the port can&#39;t be selected by the user | [optional] 
**server_listen_port** | **int** |  | 

## Example

```python
from cyperf.models.port_settings import PortSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PortSettings from a JSON string
port_settings_instance = PortSettings.from_json(json)
# print the JSON string representation of the object
print(PortSettings.to_json())

# convert the object into a dict
port_settings_dict = port_settings_instance.to_dict()
# create an instance of PortSettings from a dict
port_settings_from_dict = PortSettings.from_dict(port_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


