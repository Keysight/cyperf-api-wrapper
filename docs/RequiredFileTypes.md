# RequiredFileTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csvs** | **bool** | Include CSV files. | [optional] 
**packet_capture** | **bool** | Include packet capture. | [optional] 
**syslog** | **bool** | Include syslog. | [optional] 
**traffic_agent_log** | **bool** | Include traffic agent log. | [optional] 

## Example

```python
from cyperf.models.required_file_types import RequiredFileTypes

# TODO update the JSON string below
json = "{}"
# create an instance of RequiredFileTypes from a JSON string
required_file_types_instance = RequiredFileTypes.from_json(json)
# print the JSON string representation of the object
print(RequiredFileTypes.to_json())

# convert the object into a dict
required_file_types_dict = required_file_types_instance.to_dict()
# create an instance of RequiredFileTypes from a dict
required_file_types_from_dict = RequiredFileTypes.from_dict(required_file_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


