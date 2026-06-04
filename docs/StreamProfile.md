# StreamProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**packet_rate** | **int** |  | 
**payload_size** | **int** |  | 
**payload_type** | [**StreamPayloadType**](StreamPayloadType.md) |  | 
**total_estimated_throughput** | **str** |  | [optional] 
**total_estimated_throughput_per_simulated_user** | **str** |  | [optional] 
**unique_pool_size** | **int** |  | [optional] 

## Example

```python
from cyperf.models.stream_profile import StreamProfile

# TODO update the JSON string below
json = "{}"
# create an instance of StreamProfile from a JSON string
stream_profile_instance = StreamProfile.from_json(json)
# print the JSON string representation of the object
print(StreamProfile.to_json())

# convert the object into a dict
stream_profile_dict = stream_profile_instance.to_dict()
# create an instance of StreamProfile from a dict
stream_profile_from_dict = StreamProfile.from_dict(stream_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


