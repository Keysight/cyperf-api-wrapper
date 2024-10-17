# GetAttacks200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AppsecAttack]**](AppsecAttack.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from cyperf.models.get_attacks200_response import GetAttacks200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAttacks200Response from a JSON string
get_attacks200_response_instance = GetAttacks200Response.from_json(json)
# print the JSON string representation of the object
print(GetAttacks200Response.to_json())

# convert the object into a dict
get_attacks200_response_dict = get_attacks200_response_instance.to_dict()
# create an instance of GetAttacks200Response from a dict
get_attacks200_response_from_dict = GetAttacks200Response.from_dict(get_attacks200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


