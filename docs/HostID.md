# HostID

The host ID of license server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostid** | **str** |  | [optional] 

## Example

```python
from cyperf.models.host_id import HostID

# TODO update the JSON string below
json = "{}"
# create an instance of HostID from a JSON string
host_id_instance = HostID.from_json(json)
# print the JSON string representation of the object
print(HostID.to_json())

# convert the object into a dict
host_id_dict = host_id_instance.to_dict()
# create an instance of HostID from a dict
host_id_from_dict = HostID.from_dict(host_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


