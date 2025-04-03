# ImportOfflineLicenseResult

The result of import offline license.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmation_code** | **str** | Non-empty value, if &#x60;isDeactivation&#x60; flag is true. | 
**is_deactivation** | **bool** | True, if the offline license was generated through offline deactivation, otherwise false. | 
**receipt** | [**LicenseReceipt**](LicenseReceipt.md) |  | 

## Example

```python
from cyperf.models.import_offline_license_result import ImportOfflineLicenseResult

# TODO update the JSON string below
json = "{}"
# create an instance of ImportOfflineLicenseResult from a JSON string
import_offline_license_result_instance = ImportOfflineLicenseResult.from_json(json)
# print the JSON string representation of the object
print(ImportOfflineLicenseResult.to_json())

# convert the object into a dict
import_offline_license_result_dict = import_offline_license_result_instance.to_dict()
# create an instance of ImportOfflineLicenseResult from a dict
import_offline_license_result_from_dict = ImportOfflineLicenseResult.from_dict(import_offline_license_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


