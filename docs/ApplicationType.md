# ApplicationType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commands** | [**List[Command]**](Command.md) | The commands included in the flow | [optional] 
**connections** | [**List[Connection]**](Connection.md) | The connections included in the flow | [optional] [readonly] 
**custom_stats** | [**List[CustomStat]**](CustomStat.md) | The custom statistics of the application | [optional] 
**data_types** | [**List[DataType]**](DataType.md) | The data types definition of the parameters | [optional] 
**definition** | [**Definition**](Definition.md) |  | [optional] 
**description** | **str** | The description of the application | [optional] 
**endpoints** | [**List[Endpoint]**](Endpoint.md) | The list of endpoints used by the application | [optional] [readonly] 
**file_name** | **str** | The name of the XML file that contains the application definition | [optional] 
**has_banner_command** | **bool** | Indicates if there is a command that is required, can only be add once and also must be the first | [optional] 
**md5_content** | **str** | The MD5 value of the XML file that contains the application definition. | [optional] 
**md5_metadata** | **str** | The MD5 value of the XML file that contains the metadata definition. | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**name** | **str** | The display name of the application | [optional] 
**parameters** | [**List[Parameter]**](Parameter.md) | The parameters of the application | [optional] [readonly] 
**strikes** | [**List[Command]**](Command.md) | The commands and strikes included in the flow | [optional] 
**supports_calibration** | **bool** | Indicates if the best configuration can be computed automatically | [optional] 
**supports_client_http_profile** | **bool** | Indicates if the application uses Client HTTP profiles. | [optional] 
**supports_http_profiles** | **bool** | Indicates if the application uses HTTP profiles. | [optional] 
**supports_server_http_profile** | **bool** | Indicates if the application uses Server HTTP profiles. | [optional] 
**supports_strikes** | **bool** | Indicates if the application supports strikes. | [optional] 
**supports_tls** | **bool** | Indicates if the application supports TLS protocol. | [optional] 
**id** | **str** | The unique identifier of the flow | [optional] [readonly] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from cyperf.models.application_type import ApplicationType

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationType from a JSON string
application_type_instance = ApplicationType.from_json(json)
# print the JSON string representation of the object
print(ApplicationType.to_json())

# convert the object into a dict
application_type_dict = application_type_instance.to_dict()
# create an instance of ApplicationType from a dict
application_type_from_dict = ApplicationType.from_dict(application_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


