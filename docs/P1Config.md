# P1Config


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dh_group** | [**DhP1Group**](DhP1Group.md) |  | 
**enc_algorithm** | [**EncP1Algorithm**](EncP1Algorithm.md) |  | 
**hash_algorithm** | [**HashP1Algorithm**](HashP1Algorithm.md) |  | 
**initial_contact** | **bool** |  | 
**lifetime** | **int** |  | 
**prf_algorithm** | [**PrfP1Algorithm**](PrfP1Algorithm.md) |  | 

## Example

```python
from cyperf.models.p1_config import P1Config

# TODO update the JSON string below
json = "{}"
# create an instance of P1Config from a JSON string
p1_config_instance = P1Config.from_json(json)
# print the JSON string representation of the object
print(P1Config.to_json())

# convert the object into a dict
p1_config_dict = p1_config_instance.to_dict()
# create an instance of P1Config from a dict
p1_config_from_dict = P1Config.from_dict(p1_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


