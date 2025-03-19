# swagger_client.ScanApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scans_create**](ScanApi.md#scans_create) | **POST** /api/v1/scans | Trigger a manual scan
[**scans_list**](ScanApi.md#scans_list) | **GET** /api/v1/scans | List all scans
[**scans_partial_update**](ScanApi.md#scans_partial_update) | **PATCH** /api/v1/scans/{id} | Partially update a scan
[**scans_report_retrieve**](ScanApi.md#scans_report_retrieve) | **GET** /api/v1/scans/{id}/report | Download ZIP report
[**scans_retrieve**](ScanApi.md#scans_retrieve) | **GET** /api/v1/scans/{id} | Retrieve data from a specific scan

# **scans_create**
> OpenApiResponseResponse scans_create(body)

Trigger a manual scan

Trigger a manual scan by providing the required scan details. If `scanner_args` are not provided, the system will automatically use the default settings from the associated provider. If you do provide `scanner_args`, these settings will be merged with the provider's defaults. This means that your provided settings will override the defaults only where they conflict, while the rest of the default settings will remain intact.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ScanApi(swagger_client.ApiClient(configuration))
body = swagger_client.ScanCreateRequest() # ScanCreateRequest | 

try:
    # Trigger a manual scan
    api_response = api_instance.scans_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanApi->scans_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScanCreateRequest**](ScanCreateRequest.md)|  | 

### Return type

[**OpenApiResponseResponse**](OpenApiResponseResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scans_list**
> PaginatedScanList scans_list(fields_scans=fields_scans, filter_completed_at=filter_completed_at, filter_inserted_at=filter_inserted_at, filter_name=filter_name, filter_name__icontains=filter_name__icontains, filter_next_scan_at=filter_next_scan_at, filter_next_scan_at__gte=filter_next_scan_at__gte, filter_next_scan_at__lte=filter_next_scan_at__lte, filter_provider=filter_provider, filter_provider__in=filter_provider__in, filter_provider_alias=filter_provider_alias, filter_provider_alias__icontains=filter_provider_alias__icontains, filter_provider_alias__in=filter_provider_alias__in, filter_provider_type=filter_provider_type, filter_provider_type__in=filter_provider_type__in, filter_provider_uid=filter_provider_uid, filter_provider_uid__icontains=filter_provider_uid__icontains, filter_provider_uid__in=filter_provider_uid__in, filter_search=filter_search, filter_started_at=filter_started_at, filter_started_at__gte=filter_started_at__gte, filter_started_at__lte=filter_started_at__lte, filter_state=filter_state, filter_state__in=filter_state__in, filter_trigger=filter_trigger, page_number=page_number, page_size=page_size, sort=sort)

List all scans

Retrieve a list of all scans with options for filtering by various criteria.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ScanApi(swagger_client.ApiClient(configuration))
fields_scans = ['fields_scans_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)
filter_completed_at = '2013-10-20' # date |  (optional)
filter_inserted_at = '2013-10-20' # date |  (optional)
filter_name = 'filter_name_example' # str |  (optional)
filter_name__icontains = 'filter_name__icontains_example' # str |  (optional)
filter_next_scan_at = '2013-10-20' # date |  (optional)
filter_next_scan_at__gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_next_scan_at__lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_provider = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
filter_provider__in = ['filter_provider__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_provider_alias = 'filter_provider_alias_example' # str |  (optional)
filter_provider_alias__icontains = 'filter_provider_alias__icontains_example' # str |  (optional)
filter_provider_alias__in = ['filter_provider_alias__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_provider_type = 'filter_provider_type_example' # str | * `aws` - AWS * `azure` - Azure * `gcp` - GCP * `kubernetes` - Kubernetes (optional)
filter_provider_type__in = ['filter_provider_type__in_example'] # list[str] | Multiple values may be separated by commas.  * `aws` - AWS * `azure` - Azure * `gcp` - GCP * `kubernetes` - Kubernetes (optional)
filter_provider_uid = 'filter_provider_uid_example' # str |  (optional)
filter_provider_uid__icontains = 'filter_provider_uid__icontains_example' # str |  (optional)
filter_provider_uid__in = ['filter_provider_uid__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_search = 'filter_search_example' # str | A search term. (optional)
filter_started_at = '2013-10-20' # date |  (optional)
filter_started_at__gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_started_at__lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_state = 'filter_state_example' # str | * `available` - Available * `scheduled` - Scheduled * `executing` - Executing * `completed` - Completed * `failed` - Failed * `cancelled` - Cancelled (optional)
filter_state__in = ['filter_state__in_example'] # list[str] | Multiple values may be separated by commas.  * `available` - Available * `scheduled` - Scheduled * `executing` - Executing * `completed` - Completed * `failed` - Failed * `cancelled` - Cancelled (optional)
filter_trigger = 'filter_trigger_example' # str | * `scheduled` - Scheduled * `manual` - Manual (optional)
page_number = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
sort = ['sort_example'] # list[str] | [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) (optional)

try:
    # List all scans
    api_response = api_instance.scans_list(fields_scans=fields_scans, filter_completed_at=filter_completed_at, filter_inserted_at=filter_inserted_at, filter_name=filter_name, filter_name__icontains=filter_name__icontains, filter_next_scan_at=filter_next_scan_at, filter_next_scan_at__gte=filter_next_scan_at__gte, filter_next_scan_at__lte=filter_next_scan_at__lte, filter_provider=filter_provider, filter_provider__in=filter_provider__in, filter_provider_alias=filter_provider_alias, filter_provider_alias__icontains=filter_provider_alias__icontains, filter_provider_alias__in=filter_provider_alias__in, filter_provider_type=filter_provider_type, filter_provider_type__in=filter_provider_type__in, filter_provider_uid=filter_provider_uid, filter_provider_uid__icontains=filter_provider_uid__icontains, filter_provider_uid__in=filter_provider_uid__in, filter_search=filter_search, filter_started_at=filter_started_at, filter_started_at__gte=filter_started_at__gte, filter_started_at__lte=filter_started_at__lte, filter_state=filter_state, filter_state__in=filter_state__in, filter_trigger=filter_trigger, page_number=page_number, page_size=page_size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanApi->scans_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields_scans** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 
 **filter_completed_at** | **date**|  | [optional] 
 **filter_inserted_at** | **date**|  | [optional] 
 **filter_name** | **str**|  | [optional] 
 **filter_name__icontains** | **str**|  | [optional] 
 **filter_next_scan_at** | **date**|  | [optional] 
 **filter_next_scan_at__gte** | **datetime**|  | [optional] 
 **filter_next_scan_at__lte** | **datetime**|  | [optional] 
 **filter_provider** | [**str**](.md)|  | [optional] 
 **filter_provider__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_provider_alias** | **str**|  | [optional] 
 **filter_provider_alias__icontains** | **str**|  | [optional] 
 **filter_provider_alias__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_provider_type** | **str**| * &#x60;aws&#x60; - AWS * &#x60;azure&#x60; - Azure * &#x60;gcp&#x60; - GCP * &#x60;kubernetes&#x60; - Kubernetes | [optional] 
 **filter_provider_type__in** | [**list[str]**](str.md)| Multiple values may be separated by commas.  * &#x60;aws&#x60; - AWS * &#x60;azure&#x60; - Azure * &#x60;gcp&#x60; - GCP * &#x60;kubernetes&#x60; - Kubernetes | [optional] 
 **filter_provider_uid** | **str**|  | [optional] 
 **filter_provider_uid__icontains** | **str**|  | [optional] 
 **filter_provider_uid__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_search** | **str**| A search term. | [optional] 
 **filter_started_at** | **date**|  | [optional] 
 **filter_started_at__gte** | **datetime**|  | [optional] 
 **filter_started_at__lte** | **datetime**|  | [optional] 
 **filter_state** | **str**| * &#x60;available&#x60; - Available * &#x60;scheduled&#x60; - Scheduled * &#x60;executing&#x60; - Executing * &#x60;completed&#x60; - Completed * &#x60;failed&#x60; - Failed * &#x60;cancelled&#x60; - Cancelled | [optional] 
 **filter_state__in** | [**list[str]**](str.md)| Multiple values may be separated by commas.  * &#x60;available&#x60; - Available * &#x60;scheduled&#x60; - Scheduled * &#x60;executing&#x60; - Executing * &#x60;completed&#x60; - Completed * &#x60;failed&#x60; - Failed * &#x60;cancelled&#x60; - Cancelled | [optional] 
 **filter_trigger** | **str**| * &#x60;scheduled&#x60; - Scheduled * &#x60;manual&#x60; - Manual | [optional] 
 **page_number** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **sort** | [**list[str]**](str.md)| [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) | [optional] 

### Return type

[**PaginatedScanList**](PaginatedScanList.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scans_partial_update**
> ScanUpdateResponse scans_partial_update(body, id)

Partially update a scan

Update certain fields of an existing scan without affecting other fields.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ScanApi(swagger_client.ApiClient(configuration))
body = swagger_client.PatchedScanUpdateRequest() # PatchedScanUpdateRequest | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this scan.

try:
    # Partially update a scan
    api_response = api_instance.scans_partial_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanApi->scans_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchedScanUpdateRequest**](PatchedScanUpdateRequest.md)|  | 
 **id** | [**str**](.md)| A UUID string identifying this scan. | 

### Return type

[**ScanUpdateResponse**](ScanUpdateResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scans_report_retrieve**
> scans_report_retrieve(id, fields_scan_reports=fields_scan_reports)

Download ZIP report

Returns a ZIP file containing the requested report

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ScanApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this scan.
fields_scan_reports = ['fields_scan_reports_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)

try:
    # Download ZIP report
    api_instance.scans_report_retrieve(id, fields_scan_reports=fields_scan_reports)
except ApiException as e:
    print("Exception when calling ScanApi->scans_report_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this scan. | 
 **fields_scan_reports** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 

### Return type

void (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scans_retrieve**
> ScanResponse scans_retrieve(id, fields_scans=fields_scans)

Retrieve data from a specific scan

Fetch detailed information about a specific scan by its ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ScanApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this scan.
fields_scans = ['fields_scans_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)

try:
    # Retrieve data from a specific scan
    api_response = api_instance.scans_retrieve(id, fields_scans=fields_scans)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanApi->scans_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this scan. | 
 **fields_scans** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 

### Return type

[**ScanResponse**](ScanResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

