# GetBrokers200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Broker]**](Broker.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from cyperf.models.get_brokers200_response_one_of import GetBrokers200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetBrokers200ResponseOneOf from a JSON string
get_brokers200_response_one_of_instance = GetBrokers200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(GetBrokers200ResponseOneOf.to_json())

# convert the object into a dict
get_brokers200_response_one_of_dict = get_brokers200_response_one_of_instance.to_dict()
# create an instance of GetBrokers200ResponseOneOf from a dict
get_brokers200_response_one_of_from_dict = GetBrokers200ResponseOneOf.from_dict(get_brokers200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


