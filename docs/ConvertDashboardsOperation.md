# ConvertDashboardsOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard_ids** | **List[str]** | The dashboard ids to be converted | [optional] 
**test_id** | **str** | The test that contains the dashboards | [optional] 
**types** | **List[str]** | The types of queries the dashboards will be converted in | [optional] 

## Example

```python
from cyperf.models.convert_dashboards_operation import ConvertDashboardsOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertDashboardsOperation from a JSON string
convert_dashboards_operation_instance = ConvertDashboardsOperation.from_json(json)
# print the JSON string representation of the object
print(ConvertDashboardsOperation.to_json())

# convert the object into a dict
convert_dashboards_operation_dict = convert_dashboards_operation_instance.to_dict()
# create an instance of ConvertDashboardsOperation from a dict
convert_dashboards_operation_from_dict = ConvertDashboardsOperation.from_dict(convert_dashboards_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


