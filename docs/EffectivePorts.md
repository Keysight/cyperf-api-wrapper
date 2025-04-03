# EffectivePorts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_destination_port** | **str** |  | 
**effective_forward_proxy_port** | **str** |  | [optional] 
**effective_server_port** | **str** |  | 

## Example

```python
from cyperf.models.effective_ports import EffectivePorts

# TODO update the JSON string below
json = "{}"
# create an instance of EffectivePorts from a JSON string
effective_ports_instance = EffectivePorts.from_json(json)
# print the JSON string representation of the object
print(EffectivePorts.to_json())

# convert the object into a dict
effective_ports_dict = effective_ports_instance.to_dict()
# create an instance of EffectivePorts from a dict
effective_ports_from_dict = EffectivePorts.from_dict(effective_ports_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


