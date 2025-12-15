# GroupTLS13

A TLSv1.3 group with deprecation status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_deprecated** | **bool** |  | 
**name** | [**SupportedGroupTLS13**](SupportedGroupTLS13.md) |  | 

## Example

```python
from cyperf.models.group_tls13 import GroupTLS13

# TODO update the JSON string below
json = "{}"
# create an instance of GroupTLS13 from a JSON string
group_tls13_instance = GroupTLS13.from_json(json)
# print the JSON string representation of the object
print(GroupTLS13.to_json())

# convert the object into a dict
group_tls13_dict = group_tls13_instance.to_dict()
# create an instance of GroupTLS13 from a dict
group_tls13_from_dict = GroupTLS13.from_dict(group_tls13_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


