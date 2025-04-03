# HealthIssue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Details regarding the health issue | [optional] 
**type** | **str** | The type of the health issue | [optional] 

## Example

```python
from cyperf.models.health_issue import HealthIssue

# TODO update the JSON string below
json = "{}"
# create an instance of HealthIssue from a JSON string
health_issue_instance = HealthIssue.from_json(json)
# print the JSON string representation of the object
print(HealthIssue.to_json())

# convert the object into a dict
health_issue_dict = health_issue_instance.to_dict()
# create an instance of HealthIssue from a dict
health_issue_from_dict = HealthIssue.from_dict(health_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


