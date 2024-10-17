# StatelessStream


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_stream_profile** | [**StreamProfile**](StreamProfile.md) |  | [optional] 
**direction** | [**StreamDirection**](StreamDirection.md) |  | [optional] 
**is_flood_stream** | **bool** |  | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**server_stream_profile** | [**StreamProfile**](StreamProfile.md) |  | [optional] 

## Example

```python
from cyperf.models.stateless_stream import StatelessStream

# TODO update the JSON string below
json = "{}"
# create an instance of StatelessStream from a JSON string
stateless_stream_instance = StatelessStream.from_json(json)
# print the JSON string representation of the object
print(StatelessStream.to_json())

# convert the object into a dict
stateless_stream_dict = stateless_stream_instance.to_dict()
# create an instance of StatelessStream from a dict
stateless_stream_from_dict = StatelessStream.from_dict(stateless_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


