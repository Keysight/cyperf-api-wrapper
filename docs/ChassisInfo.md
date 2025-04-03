# ChassisInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkout_id** | **int** | The id of the compute node used for checkout licenses | [optional] [readonly] 
**compute_node_id** | **str** | The id of the compute node where the agent is running | [optional] [readonly] 
**port_id** | **str** | The id of the corresponding port | [optional] [readonly] 

## Example

```python
from cyperf.models.chassis_info import ChassisInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ChassisInfo from a JSON string
chassis_info_instance = ChassisInfo.from_json(json)
# print the JSON string representation of the object
print(ChassisInfo.to_json())

# convert the object into a dict
chassis_info_dict = chassis_info_instance.to_dict()
# create an instance of ChassisInfo from a dict
chassis_info_from_dict = ChassisInfo.from_dict(chassis_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


