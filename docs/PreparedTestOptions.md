# PreparedTestOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_activity_meta** | **bool** |  | [optional] 
**datasource_for_ui_views** | **str** |  | [optional] 
**extra_tags** | **Dict[str, List[str]]** |  | [optional] 
**filter_by_properties** | **Dict[str, str]** |  | [optional] 
**format_protocol_name** | **bool** |  | [optional] 
**override_properties** | **Dict[str, str]** |  | [optional] 

## Example

```python
from cyperf.models.prepared_test_options import PreparedTestOptions

# TODO update the JSON string below
json = "{}"
# create an instance of PreparedTestOptions from a JSON string
prepared_test_options_instance = PreparedTestOptions.from_json(json)
# print the JSON string representation of the object
print(PreparedTestOptions.to_json())

# convert the object into a dict
prepared_test_options_dict = prepared_test_options_instance.to_dict()
# create an instance of PreparedTestOptions from a dict
prepared_test_options_from_dict = PreparedTestOptions.from_dict(prepared_test_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


