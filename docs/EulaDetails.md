# EulaDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**accepted** | **bool** |  | [default to False]
**text** | **str** |  | [optional] 
**html** | **str** |  | [optional] 

## Example

```python
from cyperf.models.eula_details import EulaDetails

# TODO update the JSON string below
json = "{}"
# create an instance of EulaDetails from a JSON string
eula_details_instance = EulaDetails.from_json(json)
# print the JSON string representation of the object
print(EulaDetails.to_json())

# convert the object into a dict
eula_details_dict = eula_details_instance.to_dict()
# create an instance of EulaDetails from a dict
eula_details_from_dict = EulaDetails.from_dict(eula_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


