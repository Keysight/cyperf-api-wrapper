# GetResultsTags200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResultsGroup]**](ResultsGroup.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from cyperf.models.get_results_tags200_response_one_of import GetResultsTags200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetResultsTags200ResponseOneOf from a JSON string
get_results_tags200_response_one_of_instance = GetResultsTags200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(GetResultsTags200ResponseOneOf.to_json())

# convert the object into a dict
get_results_tags200_response_one_of_dict = get_results_tags200_response_one_of_instance.to_dict()
# create an instance of GetResultsTags200ResponseOneOf from a dict
get_results_tags200_response_one_of_from_dict = GetResultsTags200ResponseOneOf.from_dict(get_results_tags200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


