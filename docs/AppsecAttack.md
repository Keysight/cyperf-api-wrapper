# AppsecAttack


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attack** | [**Attack**](Attack.md) |  | [optional] 
**description** | **str** | The description of the attack | [optional] 
**metadata** | [**AttackMetadata**](AttackMetadata.md) |  | [optional] 
**name** | **str** | The user friendly name of the attack | [optional] 
**id** | **str** | The unique identifier of the attack | [optional] [readonly] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**owner** | **str** | The friendly display name of the attack&#39;s owner | [optional] [readonly] 
**owner_id** | **str** | The unique identifier of the attack&#39;s owner | [optional] [readonly] 

## Example

```python
from cyperf.models.appsec_attack import AppsecAttack

# TODO update the JSON string below
json = "{}"
# create an instance of AppsecAttack from a JSON string
appsec_attack_instance = AppsecAttack.from_json(json)
# print the JSON string representation of the object
print(AppsecAttack.to_json())

# convert the object into a dict
appsec_attack_dict = appsec_attack_instance.to_dict()
# create an instance of AppsecAttack from a dict
appsec_attack_from_dict = AppsecAttack.from_dict(appsec_attack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


