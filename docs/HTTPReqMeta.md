# HTTPReqMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | **Dict[str, List[str]]** |  | [optional] 
**hostname** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**uri** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from cyperf.models.http_req_meta import HTTPReqMeta

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPReqMeta from a JSON string
http_req_meta_instance = HTTPReqMeta.from_json(json)
# print the JSON string representation of the object
print(HTTPReqMeta.to_json())

# convert the object into a dict
http_req_meta_dict = http_req_meta_instance.to_dict()
# create an instance of HTTPReqMeta from a dict
http_req_meta_from_dict = HTTPReqMeta.from_dict(http_req_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


