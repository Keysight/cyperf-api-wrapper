# GetApplicationTypes200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApplicationType]**](ApplicationType.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from cyperf.models.get_application_types200_response_one_of import GetApplicationTypes200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetApplicationTypes200ResponseOneOf from a JSON string
get_application_types200_response_one_of_instance = GetApplicationTypes200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(GetApplicationTypes200ResponseOneOf.to_json())

# convert the object into a dict
get_application_types200_response_one_of_dict = get_application_types200_response_one_of_instance.to_dict()
# create an instance of GetApplicationTypes200ResponseOneOf from a dict
get_application_types200_response_one_of_from_dict = GetApplicationTypes200ResponseOneOf.from_dict(get_application_types200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


