# ExternalResourceInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_resource_url** | **str** | The id of the attack resource | [optional] 

## Example

```python
from cyperf.models.external_resource_info import ExternalResourceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalResourceInfo from a JSON string
external_resource_info_instance = ExternalResourceInfo.from_json(json)
# print the JSON string representation of the object
print(ExternalResourceInfo.to_json())

# convert the object into a dict
external_resource_info_dict = external_resource_info_instance.to_dict()
# create an instance of ExternalResourceInfo from a dict
external_resource_info_from_dict = ExternalResourceInfo.from_dict(external_resource_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


