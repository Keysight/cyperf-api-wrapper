# GridPosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **int** | The height of the panel. A unit is equal to 30 pixels | [optional] 
**width** | **int** | The width of the panel. A unit is equal to 1/24 of the screen width | [optional] 
**x_pos** | **int** | The x coordinate of the panel. A unit is equal to 1/24 of the screen width | [optional] 
**y_pos** | **int** | The y coordinate of the panel. A unit is equal to 30 pixels | [optional] 

## Example

```python
from cyperf.models.grid_position import GridPosition

# TODO update the JSON string below
json = "{}"
# create an instance of GridPosition from a JSON string
grid_position_instance = GridPosition.from_json(json)
# print the JSON string representation of the object
print(GridPosition.to_json())

# convert the object into a dict
grid_position_dict = grid_position_instance.to_dict()
# create an instance of GridPosition from a dict
grid_position_from_dict = GridPosition.from_dict(grid_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


