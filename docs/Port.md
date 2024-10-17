# Port


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** | Whether the port is disabled or not | [optional] 
**id** | **str** | The port&#39;s unique identifier | [optional] 
**link** | **str** | The link state of the port: up or down | [optional] 
**name** | **str** | A user-friendly display name for the port | [optional] 
**owner** | **str** | A user-friendly display name for the port&#39;s owner | [optional] 
**owner_id** | **str** | The unique identifier of the port&#39;s owner | [optional] 
**speed** | **str** | The port&#39;s speed | [optional] 
**status** | **str** | The current status of the port: ready or not ready | [optional] 
**traffic_status** | **str** | The traffic status of the port | [optional] 

## Example

```python
from cyperf.models.port import Port

# TODO update the JSON string below
json = "{}"
# create an instance of Port from a JSON string
port_instance = Port.from_json(json)
# print the JSON string representation of the object
print(Port.to_json())

# convert the object into a dict
port_dict = port_instance.to_dict()
# create an instance of Port from a dict
port_from_dict = Port.from_dict(port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


