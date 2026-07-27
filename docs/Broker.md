# Broker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_status** | **str** |  | [optional] 
**failure_reason** | **str** |  | [optional] 
**fingerprint** | **str** |  | [optional] 
**host_name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**interactive_fingerprint_verification** | **bool** |  | [optional] 
**password** | **str** |  | [optional] 
**pretty_conn_status** | **str** |  | [optional] 
**trust_new** | **bool** |  | [optional] 
**tunnel_host_name** | **str** |  | [optional] 
**user** | **str** |  | [optional] 

## Example

```python
from cyperf.models.broker import Broker

# TODO update the JSON string below
json = "{}"
# create an instance of Broker from a JSON string
broker_instance = Broker.from_json(json)
# print the JSON string representation of the object
print(Broker.to_json())

# convert the object into a dict
broker_dict = broker_instance.to_dict()
# create an instance of Broker from a dict
broker_from_dict = Broker.from_dict(broker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


