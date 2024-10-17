# CustomDashboards


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Indicates whether the custom dashboards are enabled or not. | 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**links** | [**List[APILink]**](APILink.md) | A list of links to user defined stats dashboards. | [optional] 

## Example

```python
from cyperf.models.custom_dashboards import CustomDashboards

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDashboards from a JSON string
custom_dashboards_instance = CustomDashboards.from_json(json)
# print the JSON string representation of the object
print(CustomDashboards.to_json())

# convert the object into a dict
custom_dashboards_dict = custom_dashboards_instance.to_dict()
# create an instance of CustomDashboards from a dict
custom_dashboards_from_dict = CustomDashboards.from_dict(custom_dashboards_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


