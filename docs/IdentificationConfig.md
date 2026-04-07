# IdentificationConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_initiator_idr** | **bool** |  | 
**initiator_id** | **str** |  | 
**initiator_id_type** | **str** |  | 
**responder_id** | **str** |  | 
**responder_id_type** | **str** |  | 

## Example

```python
from cyperf.models.identification_config import IdentificationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of IdentificationConfig from a JSON string
identification_config_instance = IdentificationConfig.from_json(json)
# print the JSON string representation of the object
print(IdentificationConfig.to_json())

# convert the object into a dict
identification_config_dict = identification_config_instance.to_dict()
# create an instance of IdentificationConfig from a dict
identification_config_from_dict = IdentificationConfig.from_dict(identification_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


