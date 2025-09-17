# ParameterMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matches** | [**List[ParameterMatch]**](ParameterMatch.md) |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from cyperf.models.parameter_meta import ParameterMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterMeta from a JSON string
parameter_meta_instance = ParameterMeta.from_json(json)
# print the JSON string representation of the object
print(ParameterMeta.to_json())

# convert the object into a dict
parameter_meta_dict = parameter_meta_instance.to_dict()
# create an instance of ParameterMeta from a dict
parameter_meta_from_dict = ParameterMeta.from_dict(parameter_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


