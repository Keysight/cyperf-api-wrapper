# LayoutConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | **int** | The number of columns in the layout grid. | [optional] 

## Example

```python
from cyperf.models.layout_config import LayoutConfig

# TODO update the JSON string below
json = "{}"
# create an instance of LayoutConfig from a JSON string
layout_config_instance = LayoutConfig.from_json(json)
# print the JSON string representation of the object
print(LayoutConfig.to_json())

# convert the object into a dict
layout_config_dict = layout_config_instance.to_dict()
# create an instance of LayoutConfig from a dict
layout_config_from_dict = LayoutConfig.from_dict(layout_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


