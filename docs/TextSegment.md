# TextSegment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bold** | **bool** | Whether the text is bold. | [optional] 
**color** | **str** | The color of the text. | [optional] 
**css_class** | **str** | A CSS class to apply to the text segment. | [optional] 
**italic** | **bool** | Whether the text is italic. | [optional] 
**text** | **str** | The text content of the segment. | [optional] 

## Example

```python
from cyperf.models.text_segment import TextSegment

# TODO update the JSON string below
json = "{}"
# create an instance of TextSegment from a JSON string
text_segment_instance = TextSegment.from_json(json)
# print the JSON string representation of the object
print(TextSegment.to_json())

# convert the object into a dict
text_segment_dict = text_segment_instance.to_dict()
# create an instance of TextSegment from a dict
text_segment_from_dict = TextSegment.from_dict(text_segment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


