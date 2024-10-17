# EmulatedRouter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emulated_router_ranges** | [**List[EmulatedRouterRange]**](EmulatedRouterRange.md) |  | [optional] 
**enabled** | **bool** |  | 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.emulated_router import EmulatedRouter

# TODO update the JSON string below
json = "{}"
# create an instance of EmulatedRouter from a JSON string
emulated_router_instance = EmulatedRouter.from_json(json)
# print the JSON string representation of the object
print(EmulatedRouter.to_json())

# convert the object into a dict
emulated_router_dict = emulated_router_instance.to_dict()
# create an instance of EmulatedRouter from a dict
emulated_router_from_dict = EmulatedRouter.from_dict(emulated_router_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


