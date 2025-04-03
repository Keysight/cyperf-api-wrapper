# EntitlementCodeInfo

The KSM entitlement code information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_codes** | [**List[ActivationCodeInfo]**](ActivationCodeInfo.md) | The list of activation codes that the entitlement code was generated with. | 
**entitlement_code** | **str** | The entitlement code | 

## Example

```python
from cyperf.models.entitlement_code_info import EntitlementCodeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementCodeInfo from a JSON string
entitlement_code_info_instance = EntitlementCodeInfo.from_json(json)
# print the JSON string representation of the object
print(EntitlementCodeInfo.to_json())

# convert the object into a dict
entitlement_code_info_dict = entitlement_code_info_instance.to_dict()
# create an instance of EntitlementCodeInfo from a dict
entitlement_code_info_from_dict = EntitlementCodeInfo.from_dict(entitlement_code_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


