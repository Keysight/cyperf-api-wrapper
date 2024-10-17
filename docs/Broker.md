# Broker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_status** | **str** | The broker&#39;s connection status | [optional] 
**fingerprint** | **str** | The broker&#39;s fingerprint | [optional] 
**host** | **str** | The IP or hostname of the registered broker | [optional] [readonly] 
**host_name** | **str** | The IP or hostname of the registered broker | [optional] [readonly] 
**id** | **str** | The unique identifier of the broker | [optional] [readonly] 
**interactive_fingerprint_verification** | **bool** | Validate the broker&#39;s fingerprint interactively | [optional] 
**password** | **str** | The broker&#39;s authentication password | [optional] 
**pretty_conn_status** | **str** | The broker&#39;s connection status in human readable format | [optional] 
**trust_new** | **bool** | The flag used to skip broker&#39;s identity verifications | [optional] 
**user** | **str** | The broker&#39;s authentication user | [optional] 

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


