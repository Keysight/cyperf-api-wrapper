# RemoteAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode_cfg_increment** | **str** | The increment value for the ModeCfg address pool (default: 0.0.0.1). | 
**mode_cfg_start** | **str** | The base address to be used for the ModeCfg address pool | [optional] 
**mode_cfg_suffix** | **int** | The IP address suffix for the ModeCfg address pool(default: 0.0.0.1). | 

## Example

```python
from cyperf.models.remote_access import RemoteAccess

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteAccess from a JSON string
remote_access_instance = RemoteAccess.from_json(json)
# print the JSON string representation of the object
print(RemoteAccess.to_json())

# convert the object into a dict
remote_access_dict = remote_access_instance.to_dict()
# create an instance of RemoteAccess from a dict
remote_access_from_dict = RemoteAccess.from_dict(remote_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


