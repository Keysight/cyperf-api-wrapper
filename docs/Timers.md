# Timers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dpd_enabled** | **bool** |  | 
**dpd_idle_period** | **int** |  | 
**dpd_timeout** | **int** |  | 

## Example

```python
from cyperf.models.timers import Timers

# TODO update the JSON string below
json = "{}"
# create an instance of Timers from a JSON string
timers_instance = Timers.from_json(json)
# print the JSON string representation of the object
print(Timers.to_json())

# convert the object into a dict
timers_dict = timers_instance.to_dict()
# create an instance of Timers from a dict
timers_from_dict = Timers.from_dict(timers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


