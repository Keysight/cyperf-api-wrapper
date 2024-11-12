# Endpoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**network_mapping** | [**NetworkMapping**](NetworkMapping.md) | The per-endpoint network mapping. Depending on Endpoint type, only ClientNetworkTags or ServerNetworkTags will be used. | [optional] 
**type** | **str** |  | 
**id** | **str** |  | 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.endpoint import Endpoint

# TODO update the JSON string below
json = "{}"
# create an instance of Endpoint from a JSON string
endpoint_instance = Endpoint.from_json(json)
# print the JSON string representation of the object
print(Endpoint.to_json())

# convert the object into a dict
endpoint_dict = endpoint_instance.to_dict()
# create an instance of Endpoint from a dict
endpoint_from_dict = Endpoint.from_dict(endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


