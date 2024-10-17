# GetAsyncOperationResult200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_codes** | [**List[ActivationCodeInfo]**](ActivationCodeInfo.md) | The list of activation codes that the entitlement code was generated with. | 
**entitlement_code** | **str** | The entitlement code | 
**activation_code** | **str** |  | 
**available_quantity** | **int** |  | 
**description** | **str** |  | 
**product** | **str** |  | 
**total_quantity** | **int** |  | 
**available_count** | **int** | Available count. | 
**consumers** | [**List[CountedFeatureConsumer]**](CountedFeatureConsumer.md) | Consumed by. | 
**feature_name** | **str** | The feature name. | 
**installed_count** | **int** | Total installed count. | 

## Example

```python
from cyperf.models.get_async_operation_result200_response import GetAsyncOperationResult200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAsyncOperationResult200Response from a JSON string
get_async_operation_result200_response_instance = GetAsyncOperationResult200Response.from_json(json)
# print the JSON string representation of the object
print(GetAsyncOperationResult200Response.to_json())

# convert the object into a dict
get_async_operation_result200_response_dict = get_async_operation_result200_response_instance.to_dict()
# create an instance of GetAsyncOperationResult200Response from a dict
get_async_operation_result200_response_from_dict = GetAsyncOperationResult200Response.from_dict(get_async_operation_result200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


