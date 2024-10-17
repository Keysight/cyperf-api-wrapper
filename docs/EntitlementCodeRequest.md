# EntitlementCodeRequest

Entitlement code request object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entitlement_code** | **str** | The entitlement code | 

## Example

```python
from cyperf.models.entitlement_code_request import EntitlementCodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementCodeRequest from a JSON string
entitlement_code_request_instance = EntitlementCodeRequest.from_json(json)
# print the JSON string representation of the object
print(EntitlementCodeRequest.to_json())

# convert the object into a dict
entitlement_code_request_dict = entitlement_code_request_instance.to_dict()
# create an instance of EntitlementCodeRequest from a dict
entitlement_code_request_from_dict = EntitlementCodeRequest.from_dict(entitlement_code_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


