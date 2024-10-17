# ParamsEnum


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**choices** | [**List[Choice]**](Choice.md) |  | [optional] 

## Example

```python
from cyperf.models.params_enum import ParamsEnum

# TODO update the JSON string below
json = "{}"
# create an instance of ParamsEnum from a JSON string
params_enum_instance = ParamsEnum.from_json(json)
# print the JSON string representation of the object
print(ParamsEnum.to_json())

# convert the object into a dict
params_enum_dict = params_enum_instance.to_dict()
# create an instance of ParamsEnum from a dict
params_enum_from_dict = ParamsEnum.from_dict(params_enum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


