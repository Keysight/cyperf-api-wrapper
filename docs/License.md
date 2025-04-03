# License

The license information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_code** | **str** | The activation code that uniquely identifies the license | 
**days_left_to_expire** | **int** | Days left to expire, value is negative if expired. | 
**expiry_date** | **str** | Expiry date of the license | 
**features** | [**List[Feature]**](Feature.md) | Features of the activation code | 
**is_expired** | **bool** | Expired flag. | 
**links** | [**List[Link]**](Link.md) | Hypermedia links. | 
**maintenance_date** | **str** | Maintenance date of the license | 
**part_number_description** | **str** | Part number description | 
**part_number_id** | **str** | Part number id. | 
**product** | **str** | The product for which the license was generated | 
**quantity** | **int** | Quantity installed of the license | 

## Example

```python
from cyperf.models.license import License

# TODO update the JSON string below
json = "{}"
# create an instance of License from a JSON string
license_instance = License.from_json(json)
# print the JSON string representation of the object
print(License.to_json())

# convert the object into a dict
license_dict = license_instance.to_dict()
# create an instance of License from a dict
license_from_dict = License.from_dict(license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


