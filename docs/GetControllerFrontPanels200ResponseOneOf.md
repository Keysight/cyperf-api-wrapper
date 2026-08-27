# GetControllerFrontPanels200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[FrontPanel]**](FrontPanel.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from cyperf.models.get_controller_front_panels200_response_one_of import GetControllerFrontPanels200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetControllerFrontPanels200ResponseOneOf from a JSON string
get_controller_front_panels200_response_one_of_instance = GetControllerFrontPanels200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(GetControllerFrontPanels200ResponseOneOf.to_json())

# convert the object into a dict
get_controller_front_panels200_response_one_of_dict = get_controller_front_panels200_response_one_of_instance.to_dict()
# create an instance of GetControllerFrontPanels200ResponseOneOf from a dict
get_controller_front_panels200_response_one_of_from_dict = GetControllerFrontPanels200ResponseOneOf.from_dict(get_controller_front_panels200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


