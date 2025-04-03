# ResultMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_session** | **str** | The id of the session where the result is currently loaded | [optional] 
**config_url** | **str** | The URL of the result&#39;s configuration | [optional] [readonly] 
**csv_url** | **str** | The URL of the cached csv archive | [optional] 
**display_name** | **str** | The user-visible name of the result | [optional] 
**download_all** | **object** | Download all available test result types | [optional] 
**download_diagnostic** | **object** | The available test diagnostic result | [optional] 
**end_time** | **int** | A Unix timestamp that indicates when the test ended | [optional] 
**files** | [**List[ResultFileMetadata]**](ResultFileMetadata.md) | The list of result files | [optional] 
**id** | **str** | The unique identifier of the result | [optional] [readonly] 
**last_modified** | **int** | A Unix timestamp that indicates when the result was last modified | [optional] [readonly] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**marked_as_deleted** | [**MarkedAsDeleted**](MarkedAsDeleted.md) |  | [optional] 
**owner** | **str** | The user-visible name of the user who owns the result | [optional] [readonly] 
**owner_id** | **str** | The unique identifier of the user who owns the result | [optional] [readonly] 
**pdf_url** | **str** | The URL of the cached pdf report | [optional] 
**pinned** | **bool** | A flag that indicates if the result&#39;s configuration is pinned | [optional] 
**reporting_links** | [**List[APILink]**](APILink.md) | A list of links to result reporting resources | [optional] 
**result_url** | **str** | The URL of the result | [optional] [readonly] 
**start_time** | **int** | A Unix timestamp that indicates when the test was started | [optional] [readonly] 
**tags** | **Dict[str, str]** | A series of tags that describe the result | [optional] 
**test_name** | **str** | The name of the test associated with the result | [optional] 
**type** | **str** | The application type of the result | [optional] [readonly] 
**user_tags** | **List[str]** | The list of user defined tags | [optional] 

## Example

```python
from cyperf.models.result_metadata import ResultMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ResultMetadata from a JSON string
result_metadata_instance = ResultMetadata.from_json(json)
# print the JSON string representation of the object
print(ResultMetadata.to_json())

# convert the object into a dict
result_metadata_dict = result_metadata_instance.to_dict()
# create an instance of ResultMetadata from a dict
result_metadata_from_dict = ResultMetadata.from_dict(result_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


