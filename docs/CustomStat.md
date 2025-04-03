# CustomStat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function** | **str** | The function of the custom statistic | [optional] 
**path** | **str** | The path of the custom statistic | [optional] 

## Example

```python
from cyperf.models.custom_stat import CustomStat

# TODO update the JSON string below
json = "{}"
# create an instance of CustomStat from a JSON string
custom_stat_instance = CustomStat.from_json(json)
# print the JSON string representation of the object
print(CustomStat.to_json())

# convert the object into a dict
custom_stat_dict = custom_stat_instance.to_dict()
# create an instance of CustomStat from a dict
custom_stat_from_dict = CustomStat.from_dict(custom_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


