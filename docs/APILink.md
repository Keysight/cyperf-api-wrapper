# APILink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**references_count** | **int** |  | [optional] 
**rel** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from cyperf.models.api_link import APILink

# TODO update the JSON string below
json = "{}"
# create an instance of APILink from a JSON string
api_link_instance = APILink.from_json(json)
# print the JSON string representation of the object
print(APILink.to_json())

# convert the object into a dict
api_link_dict = api_link_instance.to_dict()
# create an instance of APILink from a dict
api_link_from_dict = APILink.from_dict(api_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


