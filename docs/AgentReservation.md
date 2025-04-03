# AgentReservation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** |  | [optional] 
**agent_payload_names** | **List[str]** |  | [optional] 
**general_purpose_cpu_percent** | **int** |  | [optional] 
**interfaces** | **List[str]** |  | [optional] 
**ip_address_version_used** | **str** |  | [optional] 
**optimization_mode** | **str** |  | [optional] 

## Example

```python
from cyperf.models.agent_reservation import AgentReservation

# TODO update the JSON string below
json = "{}"
# create an instance of AgentReservation from a JSON string
agent_reservation_instance = AgentReservation.from_json(json)
# print the JSON string representation of the object
print(AgentReservation.to_json())

# convert the object into a dict
agent_reservation_dict = agent_reservation_instance.to_dict()
# create an instance of AgentReservation from a dict
agent_reservation_from_dict = AgentReservation.from_dict(agent_reservation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


