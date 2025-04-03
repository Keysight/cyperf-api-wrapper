# ChangeLinkStateOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** | The desired link state. | [optional] 
**ports** | **List[str]** | The port ids for which to change the link state. | [optional] 

## Example

```python
from cyperf.models.change_link_state_operation import ChangeLinkStateOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeLinkStateOperation from a JSON string
change_link_state_operation_instance = ChangeLinkStateOperation.from_json(json)
# print the JSON string representation of the object
print(ChangeLinkStateOperation.to_json())

# convert the object into a dict
change_link_state_operation_dict = change_link_state_operation_instance.to_dict()
# create an instance of ChangeLinkStateOperation from a dict
change_link_state_operation_from_dict = ChangeLinkStateOperation.from_dict(change_link_state_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


