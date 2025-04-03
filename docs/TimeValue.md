# TimeValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**now** | **int** | A Unix timestamp that indicates the current cluster time | [optional] 

## Example

```python
from cyperf.models.time_value import TimeValue

# TODO update the JSON string below
json = "{}"
# create an instance of TimeValue from a JSON string
time_value_instance = TimeValue.from_json(json)
# print the JSON string representation of the object
print(TimeValue.to_json())

# convert the object into a dict
time_value_dict = time_value_instance.to_dict()
# create an instance of TimeValue from a dict
time_value_from_dict = TimeValue.from_dict(time_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


