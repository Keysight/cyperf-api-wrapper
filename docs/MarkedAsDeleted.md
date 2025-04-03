# MarkedAsDeleted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_progress** | **int** | The progress of the result deletion | [optional] [readonly] 
**value** | **bool** | The flag that indicates if the result was marked as deleted | [optional] [readonly] 

## Example

```python
from cyperf.models.marked_as_deleted import MarkedAsDeleted

# TODO update the JSON string below
json = "{}"
# create an instance of MarkedAsDeleted from a JSON string
marked_as_deleted_instance = MarkedAsDeleted.from_json(json)
# print the JSON string representation of the object
print(MarkedAsDeleted.to_json())

# convert the object into a dict
marked_as_deleted_dict = marked_as_deleted_instance.to_dict()
# create an instance of MarkedAsDeleted from a dict
marked_as_deleted_from_dict = MarkedAsDeleted.from_dict(marked_as_deleted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


