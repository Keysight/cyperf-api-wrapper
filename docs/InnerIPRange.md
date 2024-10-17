# InnerIPRange

The Inner IP Range assigned to the current test configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_tags** | **List[str]** | A list of tags. | [optional] 

## Example

```python
from cyperf.models.inner_ip_range import InnerIPRange

# TODO update the JSON string below
json = "{}"
# create an instance of InnerIPRange from a JSON string
inner_ip_range_instance = InnerIPRange.from_json(json)
# print the JSON string representation of the object
print(InnerIPRange.to_json())

# convert the object into a dict
inner_ip_range_dict = inner_ip_range_instance.to_dict()
# create an instance of InnerIPRange from a dict
inner_ip_range_from_dict = InnerIPRange.from_dict(inner_ip_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


