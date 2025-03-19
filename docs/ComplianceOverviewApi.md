# swagger_client.ComplianceOverviewApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compliance_overviews_list**](ComplianceOverviewApi.md#compliance_overviews_list) | **GET** /api/v1/compliance-overviews | List compliance overviews for a scan
[**compliance_overviews_retrieve**](ComplianceOverviewApi.md#compliance_overviews_retrieve) | **GET** /api/v1/compliance-overviews/{id} | Retrieve data from a specific compliance overview

# **compliance_overviews_list**
> PaginatedComplianceOverviewList compliance_overviews_list(filter_scan_id, fields_compliance_overviews=fields_compliance_overviews, filter_compliance_id=filter_compliance_id, filter_compliance_id__icontains=filter_compliance_id__icontains, filter_framework=filter_framework, filter_framework__icontains=filter_framework__icontains, filter_framework__iexact=filter_framework__iexact, filter_inserted_at=filter_inserted_at, filter_inserted_at__date=filter_inserted_at__date, filter_inserted_at__gte=filter_inserted_at__gte, filter_inserted_at__lte=filter_inserted_at__lte, filter_provider_type=filter_provider_type, filter_provider_type__in=filter_provider_type__in, filter_region=filter_region, filter_region__icontains=filter_region__icontains, filter_region__in=filter_region__in, filter_search=filter_search, filter_version=filter_version, filter_version__icontains=filter_version__icontains, page_number=page_number, page_size=page_size, sort=sort)

List compliance overviews for a scan

Retrieve an overview of all the compliance in a given scan. If no region filters are provided, the region with the most fails will be returned by default.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ComplianceOverviewApi(swagger_client.ApiClient(configuration))
filter_scan_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Related scan ID.
fields_compliance_overviews = ['fields_compliance_overviews_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)
filter_compliance_id = 'filter_compliance_id_example' # str |  (optional)
filter_compliance_id__icontains = 'filter_compliance_id__icontains_example' # str |  (optional)
filter_framework = 'filter_framework_example' # str |  (optional)
filter_framework__icontains = 'filter_framework__icontains_example' # str |  (optional)
filter_framework__iexact = 'filter_framework__iexact_example' # str |  (optional)
filter_inserted_at = '2013-10-20' # date |  (optional)
filter_inserted_at__date = '2013-10-20' # date |  (optional)
filter_inserted_at__gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_inserted_at__lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_provider_type = 'filter_provider_type_example' # str | * `aws` - AWS * `azure` - Azure * `gcp` - GCP * `kubernetes` - Kubernetes (optional)
filter_provider_type__in = ['filter_provider_type__in_example'] # list[str] | Multiple values may be separated by commas.  * `aws` - AWS * `azure` - Azure * `gcp` - GCP * `kubernetes` - Kubernetes (optional)
filter_region = 'filter_region_example' # str |  (optional)
filter_region__icontains = 'filter_region__icontains_example' # str |  (optional)
filter_region__in = ['filter_region__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_search = 'filter_search_example' # str | A search term. (optional)
filter_version = 'filter_version_example' # str |  (optional)
filter_version__icontains = 'filter_version__icontains_example' # str |  (optional)
page_number = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
sort = ['sort_example'] # list[str] | [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) (optional)

try:
    # List compliance overviews for a scan
    api_response = api_instance.compliance_overviews_list(filter_scan_id, fields_compliance_overviews=fields_compliance_overviews, filter_compliance_id=filter_compliance_id, filter_compliance_id__icontains=filter_compliance_id__icontains, filter_framework=filter_framework, filter_framework__icontains=filter_framework__icontains, filter_framework__iexact=filter_framework__iexact, filter_inserted_at=filter_inserted_at, filter_inserted_at__date=filter_inserted_at__date, filter_inserted_at__gte=filter_inserted_at__gte, filter_inserted_at__lte=filter_inserted_at__lte, filter_provider_type=filter_provider_type, filter_provider_type__in=filter_provider_type__in, filter_region=filter_region, filter_region__icontains=filter_region__icontains, filter_region__in=filter_region__in, filter_search=filter_search, filter_version=filter_version, filter_version__icontains=filter_version__icontains, page_number=page_number, page_size=page_size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceOverviewApi->compliance_overviews_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_scan_id** | [**str**](.md)| Related scan ID. | 
 **fields_compliance_overviews** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 
 **filter_compliance_id** | **str**|  | [optional] 
 **filter_compliance_id__icontains** | **str**|  | [optional] 
 **filter_framework** | **str**|  | [optional] 
 **filter_framework__icontains** | **str**|  | [optional] 
 **filter_framework__iexact** | **str**|  | [optional] 
 **filter_inserted_at** | **date**|  | [optional] 
 **filter_inserted_at__date** | **date**|  | [optional] 
 **filter_inserted_at__gte** | **datetime**|  | [optional] 
 **filter_inserted_at__lte** | **datetime**|  | [optional] 
 **filter_provider_type** | **str**| * &#x60;aws&#x60; - AWS * &#x60;azure&#x60; - Azure * &#x60;gcp&#x60; - GCP * &#x60;kubernetes&#x60; - Kubernetes | [optional] 
 **filter_provider_type__in** | [**list[str]**](str.md)| Multiple values may be separated by commas.  * &#x60;aws&#x60; - AWS * &#x60;azure&#x60; - Azure * &#x60;gcp&#x60; - GCP * &#x60;kubernetes&#x60; - Kubernetes | [optional] 
 **filter_region** | **str**|  | [optional] 
 **filter_region__icontains** | **str**|  | [optional] 
 **filter_region__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_search** | **str**| A search term. | [optional] 
 **filter_version** | **str**|  | [optional] 
 **filter_version__icontains** | **str**|  | [optional] 
 **page_number** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **sort** | [**list[str]**](str.md)| [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) | [optional] 

### Return type

[**PaginatedComplianceOverviewList**](PaginatedComplianceOverviewList.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compliance_overviews_retrieve**
> ComplianceOverviewFullResponse compliance_overviews_retrieve(id, fields_compliance_overviews=fields_compliance_overviews)

Retrieve data from a specific compliance overview

Fetch detailed information about a specific compliance overview by its ID, including detailed requirement information and check's status.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ComplianceOverviewApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this compliance overview.
fields_compliance_overviews = ['fields_compliance_overviews_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)

try:
    # Retrieve data from a specific compliance overview
    api_response = api_instance.compliance_overviews_retrieve(id, fields_compliance_overviews=fields_compliance_overviews)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceOverviewApi->compliance_overviews_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this compliance overview. | 
 **fields_compliance_overviews** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 

### Return type

[**ComplianceOverviewFullResponse**](ComplianceOverviewFullResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

