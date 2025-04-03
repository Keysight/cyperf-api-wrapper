# GetApps200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AppsecApp]**](AppsecApp.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from cyperf.models.get_apps200_response_one_of import GetApps200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetApps200ResponseOneOf from a JSON string
get_apps200_response_one_of_instance = GetApps200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(GetApps200ResponseOneOf.to_json())

# convert the object into a dict
get_apps200_response_one_of_dict = get_apps200_response_one_of_instance.to_dict()
# create an instance of GetApps200ResponseOneOf from a dict
get_apps200_response_one_of_from_dict = GetApps200ResponseOneOf.from_dict(get_apps200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


