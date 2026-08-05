# FrontPanelsByController


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controller_id** | **str** | The id of the controller that the front panels are part of. | [optional] 
**front_panels** | **List[str]** | The front panel ids. | [optional] 

## Example

```python
from cyperf.models.front_panels_by_controller import FrontPanelsByController

# TODO update the JSON string below
json = "{}"
# create an instance of FrontPanelsByController from a JSON string
front_panels_by_controller_instance = FrontPanelsByController.from_json(json)
# print the JSON string representation of the object
print(FrontPanelsByController.to_json())

# convert the object into a dict
front_panels_by_controller_dict = front_panels_by_controller_instance.to_dict()
# create an instance of FrontPanelsByController from a dict
front_panels_by_controller_from_dict = FrontPanelsByController.from_dict(front_panels_by_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


