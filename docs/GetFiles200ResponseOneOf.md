# GetFiles200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResultFileMetadata]**](ResultFileMetadata.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from cyperf.models.get_files200_response_one_of import GetFiles200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetFiles200ResponseOneOf from a JSON string
get_files200_response_one_of_instance = GetFiles200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(GetFiles200ResponseOneOf.to_json())

# convert the object into a dict
get_files200_response_one_of_dict = get_files200_response_one_of_instance.to_dict()
# create an instance of GetFiles200ResponseOneOf from a dict
get_files200_response_one_of_from_dict = GetFiles200ResponseOneOf.from_dict(get_files200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


