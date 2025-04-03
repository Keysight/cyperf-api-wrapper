# GeneratePDFReportOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force_generate** | **bool** | Generate a new PDF report replacing the cached one | [optional] 
**timezone_offset** | **int** |  | [optional] 

## Example

```python
from cyperf.models.generate_pdf_report_operation import GeneratePDFReportOperation

# TODO update the JSON string below
json = "{}"
# create an instance of GeneratePDFReportOperation from a JSON string
generate_pdf_report_operation_instance = GeneratePDFReportOperation.from_json(json)
# print the JSON string representation of the object
print(GeneratePDFReportOperation.to_json())

# convert the object into a dict
generate_pdf_report_operation_dict = generate_pdf_report_operation_instance.to_dict()
# create an instance of GeneratePDFReportOperation from a dict
generate_pdf_report_operation_from_dict = GeneratePDFReportOperation.from_dict(generate_pdf_report_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


