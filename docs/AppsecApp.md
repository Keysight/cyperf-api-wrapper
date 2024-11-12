# AppsecApp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | [**Application**](Application.md) |  | [optional] 
**description** | **str** | The description of the application | [optional] 
**name** | **str** | The user friendly name of the application | [optional] 
**static** | **bool** | If true, the application/strike is generated from Controller | [optional] [readonly] 
**user_defined** | **bool** | If true, the application was created by the user | [optional] [readonly] 
**app_metadata** | [**AppsecAppMetadata**](AppsecAppMetadata.md) |  | [optional] 
**id** | **str** | The unique identifier of the application | [optional] [readonly] 
**last_modified** | **int** |  | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**owner** | **str** | The friendly display name of the application&#39;s owner | [optional] [readonly] 
**owner_id** | **str** | The unique identifier of the application&#39;s owner | [optional] [readonly] 

## Example

```python
from cyperf.models.appsec_app import AppsecApp

# TODO update the JSON string below
json = "{}"
# create an instance of AppsecApp from a JSON string
appsec_app_instance = AppsecApp.from_json(json)
# print the JSON string representation of the object
print(AppsecApp.to_json())

# convert the object into a dict
appsec_app_dict = appsec_app_instance.to_dict()
# create an instance of AppsecApp from a dict
appsec_app_from_dict = AppsecApp.from_dict(appsec_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


