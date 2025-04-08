# GetResourcesAttacks200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AppsecAttack]**](AppsecAttack.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from cyperf.models.get_resources_attacks200_response_one_of import GetResourcesAttacks200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetResourcesAttacks200ResponseOneOf from a JSON string
get_resources_attacks200_response_one_of_instance = GetResourcesAttacks200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(GetResourcesAttacks200ResponseOneOf.to_json())

# convert the object into a dict
get_resources_attacks200_response_one_of_dict = get_resources_attacks200_response_one_of_instance.to_dict()
# create an instance of GetResourcesAttacks200ResponseOneOf from a dict
get_resources_attacks200_response_one_of_from_dict = GetResourcesAttacks200ResponseOneOf.from_dict(get_resources_attacks200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


