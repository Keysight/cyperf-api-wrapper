# HTTPProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_headers** | [**Params**](Params.md) |  | [optional] 
**connection_persistence** | [**ConnectionPersistence**](ConnectionPersistence.md) |  | [optional] 
**connections_max_transactions** | **int** | The maximum number of transactions for all scenario connections. | [optional] 
**description** | **str** | The description of the HTTP profile. | 
**external_resource_url** | **str** | The external resource URL of the HTTP profile. | [optional] 
**headers** | [**Params**](Params.md) |  | [optional] 
**http_version** | [**HTTPVersion**](HTTPVersion.md) |  | [optional] 
**is_modified** | **bool** |  | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**name** | **str** | The name of the HTTP profile. | 
**params** | [**List[Params]**](Params.md) | The list of parameters present in the HTTP profile. | [optional] 
**use_application_server_headers** | **bool** |  | [optional] 

## Example

```python
from cyperf.models.http_profile import HTTPProfile

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPProfile from a JSON string
http_profile_instance = HTTPProfile.from_json(json)
# print the JSON string representation of the object
print(HTTPProfile.to_json())

# convert the object into a dict
http_profile_dict = http_profile_instance.to_dict()
# create an instance of HTTPProfile from a dict
http_profile_from_dict = HTTPProfile.from_dict(http_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


