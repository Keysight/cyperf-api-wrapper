# SimulatedIdP


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assertion_signature** | **bool** |  | 
**audience_uri** | **str** |  | 
**cert_config** | [**CertConfig**](CertConfig.md) |  | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**name_id_format** | [**NameIdFormat**](NameIdFormat.md) |  | 
**response_signature** | **bool** |  | 
**signature_algorithm** | [**IdPSignatureAlgo**](IdPSignatureAlgo.md) |  | [optional] 
**single_sign_on_url** | **str** |  | 
**xml_metadata** | **List[bytearray]** |  | [optional] 

## Example

```python
from cyperf.models.simulated_id_p import SimulatedIdP

# TODO update the JSON string below
json = "{}"
# create an instance of SimulatedIdP from a JSON string
simulated_id_p_instance = SimulatedIdP.from_json(json)
# print the JSON string representation of the object
print(SimulatedIdP.to_json())

# convert the object into a dict
simulated_id_p_dict = simulated_id_p_instance.to_dict()
# create an instance of SimulatedIdP from a dict
simulated_id_p_from_dict = SimulatedIdP.from_dict(simulated_id_p_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


