# cyperf.ReportsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_pdf**](ReportsApi.md#download_pdf) | **GET** /api/v2/results/{resultId}/download-pdf/{pdfId} | 
[**get_download_csv_by_id**](ReportsApi.md#get_download_csv_by_id) | **GET** /api/v2/results/{resultId}/download-csv/{downloadCsvId} | 
[**poll_results_generate_csv**](ReportsApi.md#poll_results_generate_csv) | **GET** /api/v2/results/{resultId}/operations/generate-csv/{id} | 
[**poll_results_generate_pdf**](ReportsApi.md#poll_results_generate_pdf) | **GET** /api/v2/results/{resultId}/operations/generate-pdf/{id} | 
[**start_results_generate_csv**](ReportsApi.md#start_results_generate_csv) | **POST** /api/v2/results/{resultId}/operations/generate-csv | 
[**start_results_generate_pdf**](ReportsApi.md#start_results_generate_pdf) | **POST** /api/v2/results/{resultId}/operations/generate-pdf | 


# **download_pdf**
> bytearray download_pdf(result_id, pdf_id)



Download the generated PDF report for the current result.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cyperf.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.ReportsApi(api_client)
    result_id = 'result_id_example' # str | The ID of the result.
    pdf_id = 56 # int | The ID of the download PDF operation.

    try:
        api_response = api_instance.download_pdf(result_id, pdf_id)
        print("The response of ReportsApi->download_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->download_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_id** | **str**| The ID of the result. | 
 **pdf_id** | **int**| The ID of the download PDF operation. | 

### Return type

**bytearray**

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The content of the PDF report. |  -  |
**404** | The requested PDF report was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_download_csv_by_id**
> get_download_csv_by_id(result_id, download_csv_id)



Download the generated CSV reports for the current result as a zip file.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cyperf.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.ReportsApi(api_client)
    result_id = 'result_id_example' # str | The ID of the result.
    download_csv_id = 'download_csv_id_example' # str | The ID of the download csv.

    try:
        api_instance.get_download_csv_by_id(result_id, download_csv_id)
    except Exception as e:
        print("Exception when calling ReportsApi->get_download_csv_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_id** | **str**| The ID of the result. | 
 **download_csv_id** | **str**| The ID of the download csv. | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The content of the zip file |  -  |
**404** | The requested CSV reports were not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poll_results_generate_csv**
> AsyncContext poll_results_generate_csv(result_id, id)



Get the state of an ongoing operation.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cyperf.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.ReportsApi(api_client)
    result_id = 'result_id_example' # str | The ID of the result.
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_results_generate_csv(result_id, id)
        print("The response of ReportsApi->poll_results_generate_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->poll_results_generate_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_id** | **str**| The ID of the result. | 
 **id** | **int**| The ID of the async operation. | 

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details about the ongoing operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poll_results_generate_pdf**
> AsyncContext poll_results_generate_pdf(result_id, id)



Get the state of an ongoing operation.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cyperf.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.ReportsApi(api_client)
    result_id = 'result_id_example' # str | The ID of the result.
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_results_generate_pdf(result_id, id)
        print("The response of ReportsApi->poll_results_generate_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->poll_results_generate_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_id** | **str**| The ID of the result. | 
 **id** | **int**| The ID of the async operation. | 

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details about the ongoing operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_results_generate_csv**
> AsyncContext start_results_generate_csv(result_id, generate_csv_reports_operation=generate_csv_reports_operation)



Generate CSV reports for the current result.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.generate_csv_reports_operation import GenerateCSVReportsOperation
from cyperf.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cyperf.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.ReportsApi(api_client)
    result_id = 'result_id_example' # str | The ID of the result.
    generate_csv_reports_operation = cyperf.GenerateCSVReportsOperation() # GenerateCSVReportsOperation |  (optional)

    try:
        api_response = api_instance.start_results_generate_csv(result_id, generate_csv_reports_operation=generate_csv_reports_operation)
        print("The response of ReportsApi->start_results_generate_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->start_results_generate_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_id** | **str**| The ID of the result. | 
 **generate_csv_reports_operation** | [**GenerateCSVReportsOperation**](GenerateCSVReportsOperation.md)|  | [optional] 

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Details about the operation that just started |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_results_generate_pdf**
> AsyncContext start_results_generate_pdf(result_id, generate_pdf_report_operation=generate_pdf_report_operation)



Generate a PDF report for the current result.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.generate_pdf_report_operation import GeneratePDFReportOperation
from cyperf.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cyperf.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.ReportsApi(api_client)
    result_id = 'result_id_example' # str | The ID of the result.
    generate_pdf_report_operation = cyperf.GeneratePDFReportOperation() # GeneratePDFReportOperation |  (optional)

    try:
        api_response = api_instance.start_results_generate_pdf(result_id, generate_pdf_report_operation=generate_pdf_report_operation)
        print("The response of ReportsApi->start_results_generate_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->start_results_generate_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_id** | **str**| The ID of the result. | 
 **generate_pdf_report_operation** | [**GeneratePDFReportOperation**](GeneratePDFReportOperation.md)|  | [optional] 

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Details about the operation that just started |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

