# FeatureReservationReserve

Feature reservation reserve request object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count_to_reserve** | **int** | The count to reserve. | 
**duration** | **int** | The duration of the reservation, in hours. | 
**feature_name** | **str** | The feature name. | 

## Example

```python
from cyperf.models.feature_reservation_reserve import FeatureReservationReserve

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureReservationReserve from a JSON string
feature_reservation_reserve_instance = FeatureReservationReserve.from_json(json)
# print the JSON string representation of the object
print(FeatureReservationReserve.to_json())

# convert the object into a dict
feature_reservation_reserve_dict = feature_reservation_reserve_instance.to_dict()
# create an instance of FeatureReservationReserve from a dict
feature_reservation_reserve_from_dict = FeatureReservationReserve.from_dict(feature_reservation_reserve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


