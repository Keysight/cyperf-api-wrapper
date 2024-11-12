# NetworkMeshing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dst_ips_per_group** | **int** | The number of destination IPs to use for each meshing group. | [optional] 
**mapping_type** | [**MappingType**](MappingType.md) |  | [optional] 
**src_vlans_per_group** | **int** | The number of source VLANs to use for each meshing group. | [optional] 

## Example

```python
from cyperf.models.network_meshing import NetworkMeshing

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkMeshing from a JSON string
network_meshing_instance = NetworkMeshing.from_json(json)
# print the JSON string representation of the object
print(NetworkMeshing.to_json())

# convert the object into a dict
network_meshing_dict = network_meshing_instance.to_dict()
# create an instance of NetworkMeshing from a dict
network_meshing_from_dict = NetworkMeshing.from_dict(network_meshing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


