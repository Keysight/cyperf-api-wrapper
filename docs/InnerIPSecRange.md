# InnerIPSecRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_auth_settings** | [**AuthenticationSettings**](AuthenticationSettings.md) |  | [optional] 
**ike_phase1_config** | [**P1Config**](P1Config.md) |  | [optional] 
**ike_phase2_config** | [**P2Config**](P2Config.md) |  | [optional] 
**ip_sec_range_name** | **str** |  | 
**local_sub_config** | [**LocalSubnetConfig**](LocalSubnetConfig.md) |  | [optional] 
**multi_p2_over_p1** | **bool** |  | 
**public_peer** | **str** |  | 
**public_peer_increment** | **str** |  | 
**remote_access** | [**RemoteAccess**](RemoteAccess.md) |  | [optional] 
**remote_sub_config** | [**RemoteSubnetConfig**](RemoteSubnetConfig.md) |  | [optional] 
**test_scenario** | **str** |  | 
**timers** | [**Timers**](Timers.md) |  | [optional] 
**tunnel_count_per_outer_ip** | **int** |  | 
**id** | **str** |  | 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.inner_ip_sec_range import InnerIPSecRange

# TODO update the JSON string below
json = "{}"
# create an instance of InnerIPSecRange from a JSON string
inner_ip_sec_range_instance = InnerIPSecRange.from_json(json)
# print the JSON string representation of the object
print(InnerIPSecRange.to_json())

# convert the object into a dict
inner_ip_sec_range_dict = inner_ip_sec_range_instance.to_dict()
# create an instance of InnerIPSecRange from a dict
inner_ip_sec_range_from_dict = InnerIPSecRange.from_dict(inner_ip_sec_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


