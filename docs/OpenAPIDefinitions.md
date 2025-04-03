# OpenAPIDefinitions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**open_api_definitions** | [**Dict[str, ConfigMetadataConfigDataValue]**](ConfigMetadataConfigDataValue.md) | The OpenAPI definitions for CyPerf data model | [optional] 

## Example

```python
from cyperf.models.open_api_definitions import OpenAPIDefinitions

# TODO update the JSON string below
json = "{}"
# create an instance of OpenAPIDefinitions from a JSON string
open_api_definitions_instance = OpenAPIDefinitions.from_json(json)
# print the JSON string representation of the object
print(OpenAPIDefinitions.to_json())

# convert the object into a dict
open_api_definitions_dict = open_api_definitions_instance.to_dict()
# create an instance of OpenAPIDefinitions from a dict
open_api_definitions_from_dict = OpenAPIDefinitions.from_dict(open_api_definitions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


