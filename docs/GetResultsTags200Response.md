# GetResultsTags200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResultsGroup]**](ResultsGroup.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from cyperf.models.get_results_tags200_response import GetResultsTags200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetResultsTags200Response from a JSON string
get_results_tags200_response_instance = GetResultsTags200Response.from_json(json)
# print the JSON string representation of the object
print(GetResultsTags200Response.to_json())

# convert the object into a dict
get_results_tags200_response_dict = get_results_tags200_response_instance.to_dict()
# create an instance of GetResultsTags200Response from a dict
get_results_tags200_response_from_dict = GetResultsTags200Response.from_dict(get_results_tags200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


