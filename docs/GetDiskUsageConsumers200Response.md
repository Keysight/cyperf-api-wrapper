# GetDiskUsageConsumers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Consumer]**](Consumer.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from cyperf.models.get_disk_usage_consumers200_response import GetDiskUsageConsumers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDiskUsageConsumers200Response from a JSON string
get_disk_usage_consumers200_response_instance = GetDiskUsageConsumers200Response.from_json(json)
# print the JSON string representation of the object
print(GetDiskUsageConsumers200Response.to_json())

# convert the object into a dict
get_disk_usage_consumers200_response_dict = get_disk_usage_consumers200_response_instance.to_dict()
# create an instance of GetDiskUsageConsumers200Response from a dict
get_disk_usage_consumers200_response_from_dict = GetDiskUsageConsumers200Response.from_dict(get_disk_usage_consumers200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


