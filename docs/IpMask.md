# IpMask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** |  | [optional] [readonly] 
**net_mask** | **int** |  | [optional] [readonly] 

## Example

```python
from cyperf.models.ip_mask import IpMask

# TODO update the JSON string below
json = "{}"
# create an instance of IpMask from a JSON string
ip_mask_instance = IpMask.from_json(json)
# print the JSON string representation of the object
print(IpMask.to_json())

# convert the object into a dict
ip_mask_dict = ip_mask_instance.to_dict()
# create an instance of IpMask from a dict
ip_mask_from_dict = IpMask.from_dict(ip_mask_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


