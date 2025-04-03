# FeatureReservation

The reservation info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_count** | **int** | Count available for reservation. | 
**is_allowed** | **bool** | Boolean flag denoting if reservation is allowed for the feature. | 
**reserved_count** | **int** | The total reserved count. | 
**reserved_remaining_duration** | **int** | Remaining duration, in seconds, of the reservation. | 

## Example

```python
from cyperf.models.feature_reservation import FeatureReservation

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureReservation from a JSON string
feature_reservation_instance = FeatureReservation.from_json(json)
# print the JSON string representation of the object
print(FeatureReservation.to_json())

# convert the object into a dict
feature_reservation_dict = feature_reservation_instance.to_dict()
# create an instance of FeatureReservation from a dict
feature_reservation_from_dict = FeatureReservation.from_dict(feature_reservation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


