# LicenseReceipt

The license receipt after of an online or offline license operation, as follows:   - deactivation: the licenses deactivated with their respective quantities;   - activation: the licenses activated with their respective quantities;   - synchronize: the licenses renewed;

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changed_licenses** | [**List[License]**](License.md) | The list of licenses changed (added/removed/renewed) by a license operation. | 
**is_online** | **bool** | Flag denoting if the license operation was performed in online or offline mode. | 
**operation_type** | **str** | The license operation type performed. | 

## Example

```python
from cyperf.models.license_receipt import LicenseReceipt

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseReceipt from a JSON string
license_receipt_instance = LicenseReceipt.from_json(json)
# print the JSON string representation of the object
print(LicenseReceipt.to_json())

# convert the object into a dict
license_receipt_dict = license_receipt_instance.to_dict()
# create an instance of LicenseReceipt from a dict
license_receipt_from_dict = LicenseReceipt.from_dict(license_receipt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


