# FilteredStat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[Filter]**](Filter.md) | The filters that will be applied to the corresponding stat view | [optional] 
**name** | **str** | The name of the stat view | [optional] 

## Example

```python
from cyperf.models.filtered_stat import FilteredStat

# TODO update the JSON string below
json = "{}"
# create an instance of FilteredStat from a JSON string
filtered_stat_instance = FilteredStat.from_json(json)
# print the JSON string representation of the object
print(FilteredStat.to_json())

# convert the object into a dict
filtered_stat_dict = filtered_stat_instance.to_dict()
# create an instance of FilteredStat from a dict
filtered_stat_from_dict = FilteredStat.from_dict(filtered_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


