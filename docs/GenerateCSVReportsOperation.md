# GenerateCSVReportsOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force_generate** | **bool** | Generate a new CSV report replacing the cached one | [optional] 
**var_from** | **str** | (optional) UNIX time in milliseconds or milliseconds from the test start (based on useRelativeTime flag) as the query interval start. Defaults to &#39;now-5m&#39; (in milliseconds) for false useRelativeTime, and 0 otherwise. | [optional] 
**interval** | **str** | (optional) The interval used to aggregate the statistics snapshots | [optional] 
**stats** | [**List[FilteredStat]**](FilteredStat.md) | The stat views for which a CSV report will be generated | [optional] 
**to** | **str** | (optional) UNIX time in milliseconds or milliseconds from the test start (based on useRelativeTime flag) as the query interval end. Defaults to &#39;now-7s&#39; (in milliseconds). | [optional] 
**use_relative_time** | **bool** | (optional) Specifies if the from/to params use milliseconds from test start or UNIX time in milliseconds. | [optional] 

## Example

```python
from cyperf.models.generate_csv_reports_operation import GenerateCSVReportsOperation

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateCSVReportsOperation from a JSON string
generate_csv_reports_operation_instance = GenerateCSVReportsOperation.from_json(json)
# print the JSON string representation of the object
print(GenerateCSVReportsOperation.to_json())

# convert the object into a dict
generate_csv_reports_operation_dict = generate_csv_reports_operation_instance.to_dict()
# create an instance of GenerateCSVReportsOperation from a dict
generate_csv_reports_operation_from_dict = GenerateCSVReportsOperation.from_dict(generate_csv_reports_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


