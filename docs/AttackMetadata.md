# AttackMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve_count** | **int** | The number of CVE references associated with the attack | [optional] 
**direction** | **str** | The aggregated direction of the strike included in the attack | [optional] 
**keywords** | [**List[AttackMetadataKeywordsInner]**](AttackMetadataKeywordsInner.md) | The aggregated keywords of the attack | [optional] 
**legacy_names** | **List[str]** |  | [optional] 
**references** | [**List[Reference]**](Reference.md) | The aggregated references of the attack | [optional] 
**severity** | **str** | The aggregated severity of the strike included in the attack | [optional] 
**strikes_count** | **int** | The number of strikes associated with the attack | [optional] 

## Example

```python
from cyperf.models.attack_metadata import AttackMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AttackMetadata from a JSON string
attack_metadata_instance = AttackMetadata.from_json(json)
# print the JSON string representation of the object
print(AttackMetadata.to_json())

# convert the object into a dict
attack_metadata_dict = attack_metadata_instance.to_dict()
# create an instance of AttackMetadata from a dict
attack_metadata_from_dict = AttackMetadata.from_dict(attack_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


