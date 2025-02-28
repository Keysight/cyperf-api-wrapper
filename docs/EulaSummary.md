# EulaSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**accepted** | **bool** |  | [default to False]

## Example

```python
from cyperf.models.eula_summary import EulaSummary

# TODO update the JSON string below
json = "{}"
# create an instance of EulaSummary from a JSON string
eula_summary_instance = EulaSummary.from_json(json)
# print the JSON string representation of the object
print(EulaSummary.to_json())

# convert the object into a dict
eula_summary_dict = eula_summary_instance.to_dict()
# create an instance of EulaSummary from a dict
eula_summary_from_dict = EulaSummary.from_dict(eula_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


