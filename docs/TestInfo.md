# TestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboards** | [**List[Dashboard]**](Dashboard.md) | All the dashboards generated for the current test | [optional] 
**default_dashboard_index** | **int** | The index of the dashboard that should be opened when user first accesses the UI | [optional] 
**default_polling_interval** | **int** | The default polling interval that should be used by the dashboards to refresh their data from the underlying stats source | [optional] 
**status** | **str** | The status of the test | [optional] 
**test_details** | **str** | An optional message that gives more details about the test run | [optional] 
**test_duration** | **int** | The run duration (in seconds) of the test | [optional] 
**test_elapsed** | **int** | The elapsed time (in seconds) since the test started | [optional] [readonly] 
**test_id** | **str** | The identifier of the test run | [optional] 
**test_initialized** | **int** | A Unix timestamp that indicates when the last test was initialized | [optional] 
**test_started** | **int** | A Unix timestamp that indicates when the test was started | [optional] 
**test_stopped** | **int** | A Unix timestamp that indicates when the test was stopped. May be null if the test is still running. | [optional] 

## Example

```python
from cyperf.models.test_info import TestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TestInfo from a JSON string
test_info_instance = TestInfo.from_json(json)
# print the JSON string representation of the object
print(TestInfo.to_json())

# convert the object into a dict
test_info_dict = test_info_instance.to_dict()
# create an instance of TestInfo from a dict
test_info_from_dict = TestInfo.from_dict(test_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


