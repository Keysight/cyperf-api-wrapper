# ActivationCodeRequest

Activation code request object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_code** | **str** | The activation code | 

## Example

```python
from cyperf.models.activation_code_request import ActivationCodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActivationCodeRequest from a JSON string
activation_code_request_instance = ActivationCodeRequest.from_json(json)
# print the JSON string representation of the object
print(ActivationCodeRequest.to_json())

# convert the object into a dict
activation_code_request_dict = activation_code_request_instance.to_dict()
# create an instance of ActivationCodeRequest from a dict
activation_code_request_from_dict = ActivationCodeRequest.from_dict(activation_code_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


