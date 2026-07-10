# PortsByPanel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**front_panel_id** | **str** | The id of the front panel that the ports are part of. | [optional] 
**ports** | **List[str]** | The port ids. | [optional] 

## Example

```python
from cyperf.models.ports_by_panel import PortsByPanel

# TODO update the JSON string below
json = "{}"
# create an instance of PortsByPanel from a JSON string
ports_by_panel_instance = PortsByPanel.from_json(json)
# print the JSON string representation of the object
print(PortsByPanel.to_json())

# convert the object into a dict
ports_by_panel_dict = ports_by_panel_instance.to_dict()
# create an instance of PortsByPanel from a dict
ports_by_panel_from_dict = PortsByPanel.from_dict(ports_by_panel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


