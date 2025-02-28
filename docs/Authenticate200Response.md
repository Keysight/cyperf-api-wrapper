# Authenticate200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The access token. Set this in the Authorization HTTP Header to authenticate requests. | [optional] 
**expires_in** | **float** | The access token lifetime. | [optional] 
**refresh_expires_in** | **float** | The refresh token lifetime. | [optional] 
**refresh_token** | **str** | Token that can be used with this request and grant_type: refresh_token to get a new access_token if the current one expires. | [optional] 

## Example

```python
from cyperf.models.authenticate200_response import Authenticate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Authenticate200Response from a JSON string
authenticate200_response_instance = Authenticate200Response.from_json(json)
# print the JSON string representation of the object
print(Authenticate200Response.to_json())

# convert the object into a dict
authenticate200_response_dict = authenticate200_response_instance.to_dict()
# create an instance of Authenticate200Response from a dict
authenticate200_response_from_dict = Authenticate200Response.from_dict(authenticate200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


