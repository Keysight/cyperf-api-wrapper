# Feature

Feature information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The feature count | 
**feature_type** | **str** | The feature type:   * &#x60;nodeLocked&#x60; - Node-locked on the host running the license server   * &#x60;floating&#x60;    - Allows concurrent users  | 
**is_uncounted** | **bool** | Feature is uncounted or not | 
**name** | **str** | The feature name | 
**reservation** | [**FeatureReservation**](FeatureReservation.md) |  | 

## Example

```python
from cyperf.models.feature import Feature

# TODO update the JSON string below
json = "{}"
# create an instance of Feature from a JSON string
feature_instance = Feature.from_json(json)
# print the JSON string representation of the object
print(Feature.to_json())

# convert the object into a dict
feature_dict = feature_instance.to_dict()
# create an instance of Feature from a dict
feature_from_dict = Feature.from_dict(feature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


