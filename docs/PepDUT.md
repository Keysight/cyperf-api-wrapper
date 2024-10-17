# PepDUT

The Policy Enforcement Point (PEP) device under test (also known as Zero Trust device)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_method** | [**Params**](Params.md) |  | [optional] 
**auth_profile_params** | [**List[Params]**](Params.md) |  | [optional] 
**auth_profile_type** | **str** |  | [optional] 
**hostname_suffix** | **str** | A suffix to be added to the Host header of all Apps/Attacks running through the DUT (default: empty string). | [optional] 
**idp_type** | [**Params**](Params.md) |  | [optional] 
**is_explicit_proxy** | **bool** | A flag indicating if PEP for the selected authentication profile is an explicit proxy | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**pep_host** | **str** | The hostname where the traffic goes if PEP device is active. | [optional] 
**pep_port** | **int** | The listen port for PEP DUT (default: 443). | [optional] 
**simulated_id_p** | [**SimulatedIdP**](SimulatedIdP.md) |  | [optional] 

## Example

```python
from cyperf.models.pep_dut import PepDUT

# TODO update the JSON string below
json = "{}"
# create an instance of PepDUT from a JSON string
pep_dut_instance = PepDUT.from_json(json)
# print the JSON string representation of the object
print(PepDUT.to_json())

# convert the object into a dict
pep_dut_dict = pep_dut_instance.to_dict()
# create an instance of PepDUT from a dict
pep_dut_from_dict = PepDUT.from_dict(pep_dut_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


