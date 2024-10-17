# UpdateNetworkMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_network_tags** | **List[str]** |  | [optional] 
**excluded_dut_list** | **List[str]** |  | [optional] 
**select_tags** | **bool** |  | [optional] 
**server_network_tags** | **List[str]** |  | [optional] 

## Example

```python
from cyperf.models.update_network_mapping import UpdateNetworkMapping

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateNetworkMapping from a JSON string
update_network_mapping_instance = UpdateNetworkMapping.from_json(json)
# print the JSON string representation of the object
print(UpdateNetworkMapping.to_json())

# convert the object into a dict
update_network_mapping_dict = update_network_mapping_instance.to_dict()
# create an instance of UpdateNetworkMapping from a dict
update_network_mapping_from_dict = UpdateNetworkMapping.from_dict(update_network_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


