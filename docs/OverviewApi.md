# swagger_client.OverviewApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**overviews_findings_retrieve**](OverviewApi.md#overviews_findings_retrieve) | **GET** /api/v1/overviews/findings | Get aggregated findings data
[**overviews_findings_severity_retrieve**](OverviewApi.md#overviews_findings_severity_retrieve) | **GET** /api/v1/overviews/findings_severity | Get findings data by severity
[**overviews_providers_retrieve**](OverviewApi.md#overviews_providers_retrieve) | **GET** /api/v1/overviews/providers | Get aggregated provider data
[**overviews_services_retrieve**](OverviewApi.md#overviews_services_retrieve) | **GET** /api/v1/overviews/services | Get findings data by service

# **overviews_findings_retrieve**
> OverviewFindingResponse overviews_findings_retrieve(fields_findings_overview=fields_findings_overview, filter_inserted_at=filter_inserted_at, filter_inserted_at__date=filter_inserted_at__date, filter_inserted_at__gte=filter_inserted_at__gte, filter_inserted_at__lte=filter_inserted_at__lte, filter_muted_findings=filter_muted_findings, filter_provider_id=filter_provider_id, filter_provider_type=filter_provider_type, filter_provider_type__in=filter_provider_type__in, filter_region=filter_region, filter_region__icontains=filter_region__icontains, filter_region__in=filter_region__in, filter_search=filter_search, sort=sort)

Get aggregated findings data

Fetch aggregated findings data across all providers, grouped by various metrics such as passed, failed, muted, and total findings. This endpoint calculates summary statistics based on the latest scans for each provider and applies any provided filters, such as region, provider type, and scan date.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OverviewApi(swagger_client.ApiClient(configuration))
fields_findings_overview = ['fields_findings_overview_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)
filter_inserted_at = '2013-10-20' # date |  (optional)
filter_inserted_at__date = '2013-10-20' # date |  (optional)
filter_inserted_at__gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_inserted_at__lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_muted_findings = true # bool |  (optional)
filter_provider_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
filter_provider_type = 'filter_provider_type_example' # str | * `aws` - AWS * `azure` - Azure * `gcp` - GCP * `kubernetes` - Kubernetes (optional)
filter_provider_type__in = ['filter_provider_type__in_example'] # list[str] | Multiple values may be separated by commas.  * `aws` - AWS * `azure` - Azure * `gcp` - GCP * `kubernetes` - Kubernetes (optional)
filter_region = 'filter_region_example' # str |  (optional)
filter_region__icontains = 'filter_region__icontains_example' # str |  (optional)
filter_region__in = ['filter_region__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_search = 'filter_search_example' # str | A search term. (optional)
sort = ['sort_example'] # list[str] | [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) (optional)

try:
    # Get aggregated findings data
    api_response = api_instance.overviews_findings_retrieve(fields_findings_overview=fields_findings_overview, filter_inserted_at=filter_inserted_at, filter_inserted_at__date=filter_inserted_at__date, filter_inserted_at__gte=filter_inserted_at__gte, filter_inserted_at__lte=filter_inserted_at__lte, filter_muted_findings=filter_muted_findings, filter_provider_id=filter_provider_id, filter_provider_type=filter_provider_type, filter_provider_type__in=filter_provider_type__in, filter_region=filter_region, filter_region__icontains=filter_region__icontains, filter_region__in=filter_region__in, filter_search=filter_search, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverviewApi->overviews_findings_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields_findings_overview** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 
 **filter_inserted_at** | **date**|  | [optional] 
 **filter_inserted_at__date** | **date**|  | [optional] 
 **filter_inserted_at__gte** | **datetime**|  | [optional] 
 **filter_inserted_at__lte** | **datetime**|  | [optional] 
 **filter_muted_findings** | **bool**|  | [optional] 
 **filter_provider_id** | [**str**](.md)|  | [optional] 
 **filter_provider_type** | **str**| * &#x60;aws&#x60; - AWS * &#x60;azure&#x60; - Azure * &#x60;gcp&#x60; - GCP * &#x60;kubernetes&#x60; - Kubernetes | [optional] 
 **filter_provider_type__in** | [**list[str]**](str.md)| Multiple values may be separated by commas.  * &#x60;aws&#x60; - AWS * &#x60;azure&#x60; - Azure * &#x60;gcp&#x60; - GCP * &#x60;kubernetes&#x60; - Kubernetes | [optional] 
 **filter_region** | **str**|  | [optional] 
 **filter_region__icontains** | **str**|  | [optional] 
 **filter_region__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_search** | **str**| A search term. | [optional] 
 **sort** | [**list[str]**](str.md)| [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) | [optional] 

### Return type

[**OverviewFindingResponse**](OverviewFindingResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **overviews_findings_severity_retrieve**
> OverviewSeverityResponse overviews_findings_severity_retrieve(fields_findings_severity_overview=fields_findings_severity_overview, filter_inserted_at=filter_inserted_at, filter_inserted_at__date=filter_inserted_at__date, filter_inserted_at__gte=filter_inserted_at__gte, filter_inserted_at__lte=filter_inserted_at__lte, filter_muted_findings=filter_muted_findings, filter_provider_id=filter_provider_id, filter_provider_type=filter_provider_type, filter_provider_type__in=filter_provider_type__in, filter_region=filter_region, filter_region__icontains=filter_region__icontains, filter_region__in=filter_region__in, filter_search=filter_search, sort=sort)

Get findings data by severity

Retrieve an aggregated summary of findings grouped by severity levels, such as low, medium, high, and critical. The response includes the total count of findings for each severity, considering only the latest scans for each provider. Additional filters can be applied to narrow down results by region, provider type, or other attributes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OverviewApi(swagger_client.ApiClient(configuration))
fields_findings_severity_overview = ['fields_findings_severity_overview_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)
filter_inserted_at = '2013-10-20' # date |  (optional)
filter_inserted_at__date = '2013-10-20' # date |  (optional)
filter_inserted_at__gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_inserted_at__lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_muted_findings = true # bool |  (optional)
filter_provider_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
filter_provider_type = 'filter_provider_type_example' # str | * `aws` - AWS * `azure` - Azure * `gcp` - GCP * `kubernetes` - Kubernetes (optional)
filter_provider_type__in = ['filter_provider_type__in_example'] # list[str] | Multiple values may be separated by commas.  * `aws` - AWS * `azure` - Azure * `gcp` - GCP * `kubernetes` - Kubernetes (optional)
filter_region = 'filter_region_example' # str |  (optional)
filter_region__icontains = 'filter_region__icontains_example' # str |  (optional)
filter_region__in = ['filter_region__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_search = 'filter_search_example' # str | A search term. (optional)
sort = ['sort_example'] # list[str] | [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) (optional)

try:
    # Get findings data by severity
    api_response = api_instance.overviews_findings_severity_retrieve(fields_findings_severity_overview=fields_findings_severity_overview, filter_inserted_at=filter_inserted_at, filter_inserted_at__date=filter_inserted_at__date, filter_inserted_at__gte=filter_inserted_at__gte, filter_inserted_at__lte=filter_inserted_at__lte, filter_muted_findings=filter_muted_findings, filter_provider_id=filter_provider_id, filter_provider_type=filter_provider_type, filter_provider_type__in=filter_provider_type__in, filter_region=filter_region, filter_region__icontains=filter_region__icontains, filter_region__in=filter_region__in, filter_search=filter_search, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverviewApi->overviews_findings_severity_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields_findings_severity_overview** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 
 **filter_inserted_at** | **date**|  | [optional] 
 **filter_inserted_at__date** | **date**|  | [optional] 
 **filter_inserted_at__gte** | **datetime**|  | [optional] 
 **filter_inserted_at__lte** | **datetime**|  | [optional] 
 **filter_muted_findings** | **bool**|  | [optional] 
 **filter_provider_id** | [**str**](.md)|  | [optional] 
 **filter_provider_type** | **str**| * &#x60;aws&#x60; - AWS * &#x60;azure&#x60; - Azure * &#x60;gcp&#x60; - GCP * &#x60;kubernetes&#x60; - Kubernetes | [optional] 
 **filter_provider_type__in** | [**list[str]**](str.md)| Multiple values may be separated by commas.  * &#x60;aws&#x60; - AWS * &#x60;azure&#x60; - Azure * &#x60;gcp&#x60; - GCP * &#x60;kubernetes&#x60; - Kubernetes | [optional] 
 **filter_region** | **str**|  | [optional] 
 **filter_region__icontains** | **str**|  | [optional] 
 **filter_region__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_search** | **str**| A search term. | [optional] 
 **sort** | [**list[str]**](str.md)| [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) | [optional] 

### Return type

[**OverviewSeverityResponse**](OverviewSeverityResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **overviews_providers_retrieve**
> OverviewProviderResponse overviews_providers_retrieve(fields_providers_overview=fields_providers_overview)

Get aggregated provider data

Retrieve an aggregated overview of findings and resources grouped by providers. The response includes the count of passed, failed, and manual findings, along with the total number of resources managed by each provider. Only the latest findings for each provider are considered in the aggregation to ensure accurate and up-to-date insights.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OverviewApi(swagger_client.ApiClient(configuration))
fields_providers_overview = ['fields_providers_overview_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)

try:
    # Get aggregated provider data
    api_response = api_instance.overviews_providers_retrieve(fields_providers_overview=fields_providers_overview)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverviewApi->overviews_providers_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields_providers_overview** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 

### Return type

[**OverviewProviderResponse**](OverviewProviderResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **overviews_services_retrieve**
> OverviewServiceResponse overviews_services_retrieve(fields_services_overview=fields_services_overview, filter_inserted_at=filter_inserted_at, filter_inserted_at__date=filter_inserted_at__date, filter_inserted_at__gte=filter_inserted_at__gte, filter_inserted_at__lte=filter_inserted_at__lte, filter_provider_id=filter_provider_id, filter_provider_type=filter_provider_type, filter_provider_type__in=filter_provider_type__in, filter_region=filter_region, filter_region__icontains=filter_region__icontains, filter_region__in=filter_region__in, filter_search=filter_search, sort=sort)

Get findings data by service

Retrieve an aggregated summary of findings grouped by service. The response includes the total count of findings for each service, as long as there are at least one finding for that service. At least one of the `inserted_at` filters must be provided.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OverviewApi(swagger_client.ApiClient(configuration))
fields_services_overview = ['fields_services_overview_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)
filter_inserted_at = '2013-10-20' # date |  (optional)
filter_inserted_at__date = '2013-10-20' # date |  (optional)
filter_inserted_at__gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_inserted_at__lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_provider_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
filter_provider_type = 'filter_provider_type_example' # str | * `aws` - AWS * `azure` - Azure * `gcp` - GCP * `kubernetes` - Kubernetes (optional)
filter_provider_type__in = ['filter_provider_type__in_example'] # list[str] | Multiple values may be separated by commas.  * `aws` - AWS * `azure` - Azure * `gcp` - GCP * `kubernetes` - Kubernetes (optional)
filter_region = 'filter_region_example' # str |  (optional)
filter_region__icontains = 'filter_region__icontains_example' # str |  (optional)
filter_region__in = ['filter_region__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_search = 'filter_search_example' # str | A search term. (optional)
sort = ['sort_example'] # list[str] | [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) (optional)

try:
    # Get findings data by service
    api_response = api_instance.overviews_services_retrieve(fields_services_overview=fields_services_overview, filter_inserted_at=filter_inserted_at, filter_inserted_at__date=filter_inserted_at__date, filter_inserted_at__gte=filter_inserted_at__gte, filter_inserted_at__lte=filter_inserted_at__lte, filter_provider_id=filter_provider_id, filter_provider_type=filter_provider_type, filter_provider_type__in=filter_provider_type__in, filter_region=filter_region, filter_region__icontains=filter_region__icontains, filter_region__in=filter_region__in, filter_search=filter_search, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverviewApi->overviews_services_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields_services_overview** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 
 **filter_inserted_at** | **date**|  | [optional] 
 **filter_inserted_at__date** | **date**|  | [optional] 
 **filter_inserted_at__gte** | **datetime**|  | [optional] 
 **filter_inserted_at__lte** | **datetime**|  | [optional] 
 **filter_provider_id** | [**str**](.md)|  | [optional] 
 **filter_provider_type** | **str**| * &#x60;aws&#x60; - AWS * &#x60;azure&#x60; - Azure * &#x60;gcp&#x60; - GCP * &#x60;kubernetes&#x60; - Kubernetes | [optional] 
 **filter_provider_type__in** | [**list[str]**](str.md)| Multiple values may be separated by commas.  * &#x60;aws&#x60; - AWS * &#x60;azure&#x60; - Azure * &#x60;gcp&#x60; - GCP * &#x60;kubernetes&#x60; - Kubernetes | [optional] 
 **filter_region** | **str**|  | [optional] 
 **filter_region__icontains** | **str**|  | [optional] 
 **filter_region__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_search** | **str**| A search term. | [optional] 
 **sort** | [**list[str]**](str.md)| [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) | [optional] 

### Return type

[**OverviewServiceResponse**](OverviewServiceResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

