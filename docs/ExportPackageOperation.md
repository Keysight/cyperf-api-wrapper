# ExportPackageOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configs** | **bool** |  | [optional] 
**external_nats_brokers** | **bool** |  | [optional] 
**keycloak** | **bool** |  | [optional] 
**license_servers** | **bool** |  | [optional] 
**results** | **bool** |  | [optional] 

## Example

```python
from cyperf.models.export_package_operation import ExportPackageOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ExportPackageOperation from a JSON string
export_package_operation_instance = ExportPackageOperation.from_json(json)
# print the JSON string representation of the object
print(ExportPackageOperation.to_json())

# convert the object into a dict
export_package_operation_dict = export_package_operation_instance.to_dict()
# create an instance of ExportPackageOperation from a dict
export_package_operation_from_dict = ExportPackageOperation.from_dict(export_package_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


