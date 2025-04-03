# ActivationCodeListRequest

Activation code list request object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_code** | **List[str]** | The activation codes | [optional] 

## Example

```python
from cyperf.models.activation_code_list_request import ActivationCodeListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActivationCodeListRequest from a JSON string
activation_code_list_request_instance = ActivationCodeListRequest.from_json(json)
# print the JSON string representation of the object
print(ActivationCodeListRequest.to_json())

# convert the object into a dict
activation_code_list_request_dict = activation_code_list_request_instance.to_dict()
# create an instance of ActivationCodeListRequest from a dict
activation_code_list_request_from_dict = ActivationCodeListRequest.from_dict(activation_code_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


