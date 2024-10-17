# P2Config


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enc_algorithm** | [**EncP2Algorithm**](EncP2Algorithm.md) |  | 
**hash_algorithm** | [**HashP2Algorithm**](HashP2Algorithm.md) |  | 
**lifetime** | **int** |  | 
**nat_enabled** | **bool** |  | 
**pfs_enabled** | **bool** |  | 
**pfs_group** | [**PfsP2Group**](PfsP2Group.md) |  | 

## Example

```python
from cyperf.models.p2_config import P2Config

# TODO update the JSON string below
json = "{}"
# create an instance of P2Config from a JSON string
p2_config_instance = P2Config.from_json(json)
# print the JSON string representation of the object
print(P2Config.to_json())

# convert the object into a dict
p2_config_dict = p2_config_instance.to_dict()
# create an instance of P2Config from a dict
p2_config_from_dict = P2Config.from_dict(p2_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


