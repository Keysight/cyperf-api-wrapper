# AppsecAppMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions_metadata** | [**List[ActionMetadata]**](ActionMetadata.md) |  | [optional] 
**app_parameters** | [**List[Parameter]**](Parameter.md) |  | [optional] 

## Example

```python
from cyperf.models.appsec_app_metadata import AppsecAppMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AppsecAppMetadata from a JSON string
appsec_app_metadata_instance = AppsecAppMetadata.from_json(json)
# print the JSON string representation of the object
print(AppsecAppMetadata.to_json())

# convert the object into a dict
appsec_app_metadata_dict = appsec_app_metadata_instance.to_dict()
# create an instance of AppsecAppMetadata from a dict
appsec_app_metadata_from_dict = AppsecAppMetadata.from_dict(appsec_app_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


