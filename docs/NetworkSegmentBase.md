# NetworkSegmentBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**id** | **str** |  | 
**network_tags** | **List[str]** | A list of tags. | [optional] 

## Example

```python
from cyperf.models.network_segment_base import NetworkSegmentBase

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkSegmentBase from a JSON string
network_segment_base_instance = NetworkSegmentBase.from_json(json)
# print the JSON string representation of the object
print(NetworkSegmentBase.to_json())

# convert the object into a dict
network_segment_base_dict = network_segment_base_instance.to_dict()
# create an instance of NetworkSegmentBase from a dict
network_segment_base_from_dict = NetworkSegmentBase.from_dict(network_segment_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


