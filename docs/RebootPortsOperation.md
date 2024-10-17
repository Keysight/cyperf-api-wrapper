# RebootPortsOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ports** | **List[str]** | The ids of the ports to reboot. | [optional] 

## Example

```python
from cyperf.models.reboot_ports_operation import RebootPortsOperation

# TODO update the JSON string below
json = "{}"
# create an instance of RebootPortsOperation from a JSON string
reboot_ports_operation_instance = RebootPortsOperation.from_json(json)
# print the JSON string representation of the object
print(RebootPortsOperation.to_json())

# convert the object into a dict
reboot_ports_operation_dict = reboot_ports_operation_instance.to_dict()
# create an instance of RebootPortsOperation from a dict
reboot_ports_operation_from_dict = RebootPortsOperation.from_dict(reboot_ports_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


