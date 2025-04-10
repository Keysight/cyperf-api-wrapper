# HTTPResMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | **Dict[str, List[str]]** |  | [optional] 
**size** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**status_code** | **int** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from cyperf.models.http_res_meta import HTTPResMeta

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPResMeta from a JSON string
http_res_meta_instance = HTTPResMeta.from_json(json)
# print the JSON string representation of the object
print(HTTPResMeta.to_json())

# convert the object into a dict
http_res_meta_dict = http_res_meta_instance.to_dict()
# create an instance of HTTPResMeta from a dict
http_res_meta_from_dict = HTTPResMeta.from_dict(http_res_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


