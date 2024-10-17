# ActivationCodeInfo

The KSM activation code information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_code** | **str** |  | 
**available_quantity** | **int** |  | 
**description** | **str** |  | 
**product** | **str** |  | 
**total_quantity** | **int** |  | 

## Example

```python
from cyperf.models.activation_code_info import ActivationCodeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ActivationCodeInfo from a JSON string
activation_code_info_instance = ActivationCodeInfo.from_json(json)
# print the JSON string representation of the object
print(ActivationCodeInfo.to_json())

# convert the object into a dict
activation_code_info_dict = activation_code_info_instance.to_dict()
# create an instance of ActivationCodeInfo from a dict
activation_code_info_from_dict = ActivationCodeInfo.from_dict(activation_code_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


