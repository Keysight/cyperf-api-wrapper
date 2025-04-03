# FulfillmentRequest

Fulfillment to be sent to KSM.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_code** | **str** | The activation code to fulfill. | 
**quantity** | **int** | The quantity to activate/deactivate. | 

## Example

```python
from cyperf.models.fulfillment_request import FulfillmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FulfillmentRequest from a JSON string
fulfillment_request_instance = FulfillmentRequest.from_json(json)
# print the JSON string representation of the object
print(FulfillmentRequest.to_json())

# convert the object into a dict
fulfillment_request_dict = fulfillment_request_instance.to_dict()
# create an instance of FulfillmentRequest from a dict
fulfillment_request_from_dict = FulfillmentRequest.from_dict(fulfillment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


