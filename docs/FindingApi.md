# swagger_client.FindingApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**findings_findings_services_regions_retrieve**](FindingApi.md#findings_findings_services_regions_retrieve) | **GET** /api/v1/findings/findings_services_regions | Retrieve the services and regions that are impacted by findings
[**findings_list**](FindingApi.md#findings_list) | **GET** /api/v1/findings | List all findings
[**findings_metadata_retrieve**](FindingApi.md#findings_metadata_retrieve) | **GET** /api/v1/findings/metadata | Retrieve metadata values from findings
[**findings_retrieve**](FindingApi.md#findings_retrieve) | **GET** /api/v1/findings/{id} | Retrieve data from a specific finding

# **findings_findings_services_regions_retrieve**
> FindingDynamicFilterResponse findings_findings_services_regions_retrieve(fields_finding_dynamic_filters=fields_finding_dynamic_filters, filter_check_id=filter_check_id, filter_check_id__icontains=filter_check_id__icontains, filter_check_id__in=filter_check_id__in, filter_delta=filter_delta, filter_delta__in=filter_delta__in, filter_id=filter_id, filter_id__in=filter_id__in, filter_impact=filter_impact, filter_impact__in=filter_impact__in, filter_inserted_at=filter_inserted_at, filter_inserted_at__date=filter_inserted_at__date, filter_inserted_at__gte=filter_inserted_at__gte, filter_inserted_at__lte=filter_inserted_at__lte, filter_provider=filter_provider, filter_provider__in=filter_provider__in, filter_provider_alias=filter_provider_alias, filter_provider_alias__icontains=filter_provider_alias__icontains, filter_provider_alias__in=filter_provider_alias__in, filter_provider_type=filter_provider_type, filter_provider_type__in=filter_provider_type__in, filter_provider_uid=filter_provider_uid, filter_provider_uid__icontains=filter_provider_uid__icontains, filter_provider_uid__in=filter_provider_uid__in, filter_region=filter_region, filter_region__icontains=filter_region__icontains, filter_region__in=filter_region__in, filter_resource_name=filter_resource_name, filter_resource_name__icontains=filter_resource_name__icontains, filter_resource_name__in=filter_resource_name__in, filter_resource_type=filter_resource_type, filter_resource_type__icontains=filter_resource_type__icontains, filter_resource_type__in=filter_resource_type__in, filter_resource_uid=filter_resource_uid, filter_resource_uid__icontains=filter_resource_uid__icontains, filter_resource_uid__in=filter_resource_uid__in, filter_resources=filter_resources, filter_scan=filter_scan, filter_scan__in=filter_scan__in, filter_search=filter_search, filter_service=filter_service, filter_service__icontains=filter_service__icontains, filter_service__in=filter_service__in, filter_severity=filter_severity, filter_severity__in=filter_severity__in, filter_status=filter_status, filter_status__in=filter_status__in, filter_uid=filter_uid, filter_uid__in=filter_uid__in, filter_updated_at=filter_updated_at, filter_updated_at__gte=filter_updated_at__gte, filter_updated_at__lte=filter_updated_at__lte, sort=sort)

Retrieve the services and regions that are impacted by findings

Fetch services and regions affected in findings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FindingApi(swagger_client.ApiClient(configuration))
fields_finding_dynamic_filters = ['fields_finding_dynamic_filters_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)
filter_check_id = 'filter_check_id_example' # str |  (optional)
filter_check_id__icontains = 'filter_check_id__icontains_example' # str |  (optional)
filter_check_id__in = ['filter_check_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_delta = 'filter_delta_example' # str | * `new` - New * `changed` - Changed (optional)
filter_delta__in = ['filter_delta__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
filter_id__in = ['filter_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_impact = 'filter_impact_example' # str | * `critical` - Critical * `high` - High * `medium` - Medium * `low` - Low * `informational` - Informational (optional)
filter_impact__in = ['filter_impact__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_inserted_at = '2013-10-20' # date |  (optional)
filter_inserted_at__date = '2013-10-20' # date |  (optional)
filter_inserted_at__gte = '2013-10-20' # date | Maximum date range is 7 days. (optional)
filter_inserted_at__lte = '2013-10-20' # date | Maximum date range is 7 days. (optional)
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
filter_region = 'filter_region_example' # str |  (optional)
filter_region__icontains = 'filter_region__icontains_example' # str |  (optional)
filter_region__in = ['filter_region__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_resource_name = 'filter_resource_name_example' # str |  (optional)
filter_resource_name__icontains = 'filter_resource_name__icontains_example' # str |  (optional)
filter_resource_name__in = ['filter_resource_name__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_resource_type = 'filter_resource_type_example' # str |  (optional)
filter_resource_type__icontains = 'filter_resource_type__icontains_example' # str |  (optional)
filter_resource_type__in = ['filter_resource_type__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_resource_uid = 'filter_resource_uid_example' # str |  (optional)
filter_resource_uid__icontains = 'filter_resource_uid__icontains_example' # str |  (optional)
filter_resource_uid__in = ['filter_resource_uid__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_resources = ['filter_resources_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_scan = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
filter_scan__in = ['filter_scan__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_search = 'filter_search_example' # str | A search term. (optional)
filter_service = 'filter_service_example' # str |  (optional)
filter_service__icontains = 'filter_service__icontains_example' # str |  (optional)
filter_service__in = ['filter_service__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_severity = 'filter_severity_example' # str | * `critical` - Critical * `high` - High * `medium` - Medium * `low` - Low * `informational` - Informational (optional)
filter_severity__in = ['filter_severity__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_status = 'filter_status_example' # str | * `FAIL` - Fail * `PASS` - Pass * `MANUAL` - Manual * `MUTED` - Muted (optional)
filter_status__in = ['filter_status__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_uid = 'filter_uid_example' # str |  (optional)
filter_uid__in = ['filter_uid__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_updated_at = '2013-10-20' # date |  (optional)
filter_updated_at__gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_updated_at__lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
sort = ['sort_example'] # list[str] | [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) (optional)

try:
    # Retrieve the services and regions that are impacted by findings
    api_response = api_instance.findings_findings_services_regions_retrieve(fields_finding_dynamic_filters=fields_finding_dynamic_filters, filter_check_id=filter_check_id, filter_check_id__icontains=filter_check_id__icontains, filter_check_id__in=filter_check_id__in, filter_delta=filter_delta, filter_delta__in=filter_delta__in, filter_id=filter_id, filter_id__in=filter_id__in, filter_impact=filter_impact, filter_impact__in=filter_impact__in, filter_inserted_at=filter_inserted_at, filter_inserted_at__date=filter_inserted_at__date, filter_inserted_at__gte=filter_inserted_at__gte, filter_inserted_at__lte=filter_inserted_at__lte, filter_provider=filter_provider, filter_provider__in=filter_provider__in, filter_provider_alias=filter_provider_alias, filter_provider_alias__icontains=filter_provider_alias__icontains, filter_provider_alias__in=filter_provider_alias__in, filter_provider_type=filter_provider_type, filter_provider_type__in=filter_provider_type__in, filter_provider_uid=filter_provider_uid, filter_provider_uid__icontains=filter_provider_uid__icontains, filter_provider_uid__in=filter_provider_uid__in, filter_region=filter_region, filter_region__icontains=filter_region__icontains, filter_region__in=filter_region__in, filter_resource_name=filter_resource_name, filter_resource_name__icontains=filter_resource_name__icontains, filter_resource_name__in=filter_resource_name__in, filter_resource_type=filter_resource_type, filter_resource_type__icontains=filter_resource_type__icontains, filter_resource_type__in=filter_resource_type__in, filter_resource_uid=filter_resource_uid, filter_resource_uid__icontains=filter_resource_uid__icontains, filter_resource_uid__in=filter_resource_uid__in, filter_resources=filter_resources, filter_scan=filter_scan, filter_scan__in=filter_scan__in, filter_search=filter_search, filter_service=filter_service, filter_service__icontains=filter_service__icontains, filter_service__in=filter_service__in, filter_severity=filter_severity, filter_severity__in=filter_severity__in, filter_status=filter_status, filter_status__in=filter_status__in, filter_uid=filter_uid, filter_uid__in=filter_uid__in, filter_updated_at=filter_updated_at, filter_updated_at__gte=filter_updated_at__gte, filter_updated_at__lte=filter_updated_at__lte, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FindingApi->findings_findings_services_regions_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields_finding_dynamic_filters** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 
 **filter_check_id** | **str**|  | [optional] 
 **filter_check_id__icontains** | **str**|  | [optional] 
 **filter_check_id__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_delta** | **str**| * &#x60;new&#x60; - New * &#x60;changed&#x60; - Changed | [optional] 
 **filter_delta__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_id** | [**str**](.md)|  | [optional] 
 **filter_id__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_impact** | **str**| * &#x60;critical&#x60; - Critical * &#x60;high&#x60; - High * &#x60;medium&#x60; - Medium * &#x60;low&#x60; - Low * &#x60;informational&#x60; - Informational | [optional] 
 **filter_impact__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_inserted_at** | **date**|  | [optional] 
 **filter_inserted_at__date** | **date**|  | [optional] 
 **filter_inserted_at__gte** | **date**| Maximum date range is 7 days. | [optional] 
 **filter_inserted_at__lte** | **date**| Maximum date range is 7 days. | [optional] 
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
 **filter_region** | **str**|  | [optional] 
 **filter_region__icontains** | **str**|  | [optional] 
 **filter_region__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_resource_name** | **str**|  | [optional] 
 **filter_resource_name__icontains** | **str**|  | [optional] 
 **filter_resource_name__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_resource_type** | **str**|  | [optional] 
 **filter_resource_type__icontains** | **str**|  | [optional] 
 **filter_resource_type__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_resource_uid** | **str**|  | [optional] 
 **filter_resource_uid__icontains** | **str**|  | [optional] 
 **filter_resource_uid__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_resources** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_scan** | [**str**](.md)|  | [optional] 
 **filter_scan__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_search** | **str**| A search term. | [optional] 
 **filter_service** | **str**|  | [optional] 
 **filter_service__icontains** | **str**|  | [optional] 
 **filter_service__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_severity** | **str**| * &#x60;critical&#x60; - Critical * &#x60;high&#x60; - High * &#x60;medium&#x60; - Medium * &#x60;low&#x60; - Low * &#x60;informational&#x60; - Informational | [optional] 
 **filter_severity__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_status** | **str**| * &#x60;FAIL&#x60; - Fail * &#x60;PASS&#x60; - Pass * &#x60;MANUAL&#x60; - Manual * &#x60;MUTED&#x60; - Muted | [optional] 
 **filter_status__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_uid** | **str**|  | [optional] 
 **filter_uid__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_updated_at** | **date**|  | [optional] 
 **filter_updated_at__gte** | **datetime**|  | [optional] 
 **filter_updated_at__lte** | **datetime**|  | [optional] 
 **sort** | [**list[str]**](str.md)| [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) | [optional] 

### Return type

[**FindingDynamicFilterResponse**](FindingDynamicFilterResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_list**
> PaginatedFindingList findings_list(filter_inserted_at, fields_findings=fields_findings, filter_check_id=filter_check_id, filter_check_id__icontains=filter_check_id__icontains, filter_check_id__in=filter_check_id__in, filter_delta=filter_delta, filter_delta__in=filter_delta__in, filter_id=filter_id, filter_id__in=filter_id__in, filter_impact=filter_impact, filter_impact__in=filter_impact__in, filter_inserted_at__date=filter_inserted_at__date, filter_inserted_at__gte=filter_inserted_at__gte, filter_inserted_at__lte=filter_inserted_at__lte, filter_provider=filter_provider, filter_provider__in=filter_provider__in, filter_provider_alias=filter_provider_alias, filter_provider_alias__icontains=filter_provider_alias__icontains, filter_provider_alias__in=filter_provider_alias__in, filter_provider_type=filter_provider_type, filter_provider_type__in=filter_provider_type__in, filter_provider_uid=filter_provider_uid, filter_provider_uid__icontains=filter_provider_uid__icontains, filter_provider_uid__in=filter_provider_uid__in, filter_region=filter_region, filter_region__icontains=filter_region__icontains, filter_region__in=filter_region__in, filter_resource_name=filter_resource_name, filter_resource_name__icontains=filter_resource_name__icontains, filter_resource_name__in=filter_resource_name__in, filter_resource_type=filter_resource_type, filter_resource_type__icontains=filter_resource_type__icontains, filter_resource_type__in=filter_resource_type__in, filter_resource_uid=filter_resource_uid, filter_resource_uid__icontains=filter_resource_uid__icontains, filter_resource_uid__in=filter_resource_uid__in, filter_resources=filter_resources, filter_scan=filter_scan, filter_scan__in=filter_scan__in, filter_search=filter_search, filter_service=filter_service, filter_service__icontains=filter_service__icontains, filter_service__in=filter_service__in, filter_severity=filter_severity, filter_severity__in=filter_severity__in, filter_status=filter_status, filter_status__in=filter_status__in, filter_uid=filter_uid, filter_uid__in=filter_uid__in, filter_updated_at=filter_updated_at, filter_updated_at__gte=filter_updated_at__gte, filter_updated_at__lte=filter_updated_at__lte, include=include, page_number=page_number, page_size=page_size, sort=sort)

List all findings

Retrieve a list of all findings with options for filtering by various criteria.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FindingApi(swagger_client.ApiClient(configuration))
filter_inserted_at = '2013-10-20' # date | At least one of the variations of the `filter[inserted_at]` filter must be provided.
fields_findings = ['fields_findings_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)
filter_check_id = 'filter_check_id_example' # str |  (optional)
filter_check_id__icontains = 'filter_check_id__icontains_example' # str |  (optional)
filter_check_id__in = ['filter_check_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_delta = 'filter_delta_example' # str | * `new` - New * `changed` - Changed (optional)
filter_delta__in = ['filter_delta__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
filter_id__in = ['filter_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_impact = 'filter_impact_example' # str | * `critical` - Critical * `high` - High * `medium` - Medium * `low` - Low * `informational` - Informational (optional)
filter_impact__in = ['filter_impact__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_inserted_at__date = '2013-10-20' # date |  (optional)
filter_inserted_at__gte = '2013-10-20' # date | Maximum date range is 7 days. (optional)
filter_inserted_at__lte = '2013-10-20' # date | Maximum date range is 7 days. (optional)
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
filter_region = 'filter_region_example' # str |  (optional)
filter_region__icontains = 'filter_region__icontains_example' # str |  (optional)
filter_region__in = ['filter_region__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_resource_name = 'filter_resource_name_example' # str |  (optional)
filter_resource_name__icontains = 'filter_resource_name__icontains_example' # str |  (optional)
filter_resource_name__in = ['filter_resource_name__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_resource_type = 'filter_resource_type_example' # str |  (optional)
filter_resource_type__icontains = 'filter_resource_type__icontains_example' # str |  (optional)
filter_resource_type__in = ['filter_resource_type__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_resource_uid = 'filter_resource_uid_example' # str |  (optional)
filter_resource_uid__icontains = 'filter_resource_uid__icontains_example' # str |  (optional)
filter_resource_uid__in = ['filter_resource_uid__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_resources = ['filter_resources_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_scan = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
filter_scan__in = ['filter_scan__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_search = 'filter_search_example' # str | A search term. (optional)
filter_service = 'filter_service_example' # str |  (optional)
filter_service__icontains = 'filter_service__icontains_example' # str |  (optional)
filter_service__in = ['filter_service__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_severity = 'filter_severity_example' # str | * `critical` - Critical * `high` - High * `medium` - Medium * `low` - Low * `informational` - Informational (optional)
filter_severity__in = ['filter_severity__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_status = 'filter_status_example' # str | * `FAIL` - Fail * `PASS` - Pass * `MANUAL` - Manual * `MUTED` - Muted (optional)
filter_status__in = ['filter_status__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_uid = 'filter_uid_example' # str |  (optional)
filter_uid__in = ['filter_uid__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_updated_at = '2013-10-20' # date |  (optional)
filter_updated_at__gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_updated_at__lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
include = ['include_example'] # list[str] | include query parameter to allow the client to customize which related resources should be returned. (optional)
page_number = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
sort = ['sort_example'] # list[str] | [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) (optional)

try:
    # List all findings
    api_response = api_instance.findings_list(filter_inserted_at, fields_findings=fields_findings, filter_check_id=filter_check_id, filter_check_id__icontains=filter_check_id__icontains, filter_check_id__in=filter_check_id__in, filter_delta=filter_delta, filter_delta__in=filter_delta__in, filter_id=filter_id, filter_id__in=filter_id__in, filter_impact=filter_impact, filter_impact__in=filter_impact__in, filter_inserted_at__date=filter_inserted_at__date, filter_inserted_at__gte=filter_inserted_at__gte, filter_inserted_at__lte=filter_inserted_at__lte, filter_provider=filter_provider, filter_provider__in=filter_provider__in, filter_provider_alias=filter_provider_alias, filter_provider_alias__icontains=filter_provider_alias__icontains, filter_provider_alias__in=filter_provider_alias__in, filter_provider_type=filter_provider_type, filter_provider_type__in=filter_provider_type__in, filter_provider_uid=filter_provider_uid, filter_provider_uid__icontains=filter_provider_uid__icontains, filter_provider_uid__in=filter_provider_uid__in, filter_region=filter_region, filter_region__icontains=filter_region__icontains, filter_region__in=filter_region__in, filter_resource_name=filter_resource_name, filter_resource_name__icontains=filter_resource_name__icontains, filter_resource_name__in=filter_resource_name__in, filter_resource_type=filter_resource_type, filter_resource_type__icontains=filter_resource_type__icontains, filter_resource_type__in=filter_resource_type__in, filter_resource_uid=filter_resource_uid, filter_resource_uid__icontains=filter_resource_uid__icontains, filter_resource_uid__in=filter_resource_uid__in, filter_resources=filter_resources, filter_scan=filter_scan, filter_scan__in=filter_scan__in, filter_search=filter_search, filter_service=filter_service, filter_service__icontains=filter_service__icontains, filter_service__in=filter_service__in, filter_severity=filter_severity, filter_severity__in=filter_severity__in, filter_status=filter_status, filter_status__in=filter_status__in, filter_uid=filter_uid, filter_uid__in=filter_uid__in, filter_updated_at=filter_updated_at, filter_updated_at__gte=filter_updated_at__gte, filter_updated_at__lte=filter_updated_at__lte, include=include, page_number=page_number, page_size=page_size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FindingApi->findings_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_inserted_at** | **date**| At least one of the variations of the &#x60;filter[inserted_at]&#x60; filter must be provided. | 
 **fields_findings** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 
 **filter_check_id** | **str**|  | [optional] 
 **filter_check_id__icontains** | **str**|  | [optional] 
 **filter_check_id__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_delta** | **str**| * &#x60;new&#x60; - New * &#x60;changed&#x60; - Changed | [optional] 
 **filter_delta__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_id** | [**str**](.md)|  | [optional] 
 **filter_id__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_impact** | **str**| * &#x60;critical&#x60; - Critical * &#x60;high&#x60; - High * &#x60;medium&#x60; - Medium * &#x60;low&#x60; - Low * &#x60;informational&#x60; - Informational | [optional] 
 **filter_impact__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_inserted_at__date** | **date**|  | [optional] 
 **filter_inserted_at__gte** | **date**| Maximum date range is 7 days. | [optional] 
 **filter_inserted_at__lte** | **date**| Maximum date range is 7 days. | [optional] 
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
 **filter_region** | **str**|  | [optional] 
 **filter_region__icontains** | **str**|  | [optional] 
 **filter_region__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_resource_name** | **str**|  | [optional] 
 **filter_resource_name__icontains** | **str**|  | [optional] 
 **filter_resource_name__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_resource_type** | **str**|  | [optional] 
 **filter_resource_type__icontains** | **str**|  | [optional] 
 **filter_resource_type__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_resource_uid** | **str**|  | [optional] 
 **filter_resource_uid__icontains** | **str**|  | [optional] 
 **filter_resource_uid__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_resources** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_scan** | [**str**](.md)|  | [optional] 
 **filter_scan__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_search** | **str**| A search term. | [optional] 
 **filter_service** | **str**|  | [optional] 
 **filter_service__icontains** | **str**|  | [optional] 
 **filter_service__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_severity** | **str**| * &#x60;critical&#x60; - Critical * &#x60;high&#x60; - High * &#x60;medium&#x60; - Medium * &#x60;low&#x60; - Low * &#x60;informational&#x60; - Informational | [optional] 
 **filter_severity__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_status** | **str**| * &#x60;FAIL&#x60; - Fail * &#x60;PASS&#x60; - Pass * &#x60;MANUAL&#x60; - Manual * &#x60;MUTED&#x60; - Muted | [optional] 
 **filter_status__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_uid** | **str**|  | [optional] 
 **filter_uid__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_updated_at** | **date**|  | [optional] 
 **filter_updated_at__gte** | **datetime**|  | [optional] 
 **filter_updated_at__lte** | **datetime**|  | [optional] 
 **include** | [**list[str]**](str.md)| include query parameter to allow the client to customize which related resources should be returned. | [optional] 
 **page_number** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **sort** | [**list[str]**](str.md)| [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) | [optional] 

### Return type

[**PaginatedFindingList**](PaginatedFindingList.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_metadata_retrieve**
> FindingMetadataResponse findings_metadata_retrieve(filter_inserted_at, fields_findings_metadata=fields_findings_metadata, filter_check_id=filter_check_id, filter_check_id__icontains=filter_check_id__icontains, filter_check_id__in=filter_check_id__in, filter_delta=filter_delta, filter_delta__in=filter_delta__in, filter_id=filter_id, filter_id__in=filter_id__in, filter_impact=filter_impact, filter_impact__in=filter_impact__in, filter_inserted_at__date=filter_inserted_at__date, filter_inserted_at__gte=filter_inserted_at__gte, filter_inserted_at__lte=filter_inserted_at__lte, filter_provider=filter_provider, filter_provider__in=filter_provider__in, filter_provider_alias=filter_provider_alias, filter_provider_alias__icontains=filter_provider_alias__icontains, filter_provider_alias__in=filter_provider_alias__in, filter_provider_type=filter_provider_type, filter_provider_type__in=filter_provider_type__in, filter_provider_uid=filter_provider_uid, filter_provider_uid__icontains=filter_provider_uid__icontains, filter_provider_uid__in=filter_provider_uid__in, filter_region=filter_region, filter_region__icontains=filter_region__icontains, filter_region__in=filter_region__in, filter_resource_name=filter_resource_name, filter_resource_name__icontains=filter_resource_name__icontains, filter_resource_name__in=filter_resource_name__in, filter_resource_type=filter_resource_type, filter_resource_type__icontains=filter_resource_type__icontains, filter_resource_type__in=filter_resource_type__in, filter_resource_uid=filter_resource_uid, filter_resource_uid__icontains=filter_resource_uid__icontains, filter_resource_uid__in=filter_resource_uid__in, filter_resources=filter_resources, filter_scan=filter_scan, filter_scan__in=filter_scan__in, filter_search=filter_search, filter_service=filter_service, filter_service__icontains=filter_service__icontains, filter_service__in=filter_service__in, filter_severity=filter_severity, filter_severity__in=filter_severity__in, filter_status=filter_status, filter_status__in=filter_status__in, filter_uid=filter_uid, filter_uid__in=filter_uid__in, filter_updated_at=filter_updated_at, filter_updated_at__gte=filter_updated_at__gte, filter_updated_at__lte=filter_updated_at__lte, sort=sort)

Retrieve metadata values from findings

Fetch unique metadata values from a set of findings. This is useful for dynamic filtering.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FindingApi(swagger_client.ApiClient(configuration))
filter_inserted_at = '2013-10-20' # date | At least one of the variations of the `filter[inserted_at]` filter must be provided.
fields_findings_metadata = ['fields_findings_metadata_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)
filter_check_id = 'filter_check_id_example' # str |  (optional)
filter_check_id__icontains = 'filter_check_id__icontains_example' # str |  (optional)
filter_check_id__in = ['filter_check_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_delta = 'filter_delta_example' # str | * `new` - New * `changed` - Changed (optional)
filter_delta__in = ['filter_delta__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
filter_id__in = ['filter_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_impact = 'filter_impact_example' # str | * `critical` - Critical * `high` - High * `medium` - Medium * `low` - Low * `informational` - Informational (optional)
filter_impact__in = ['filter_impact__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_inserted_at__date = '2013-10-20' # date |  (optional)
filter_inserted_at__gte = '2013-10-20' # date | Maximum date range is 7 days. (optional)
filter_inserted_at__lte = '2013-10-20' # date | Maximum date range is 7 days. (optional)
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
filter_region = 'filter_region_example' # str |  (optional)
filter_region__icontains = 'filter_region__icontains_example' # str |  (optional)
filter_region__in = ['filter_region__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_resource_name = 'filter_resource_name_example' # str |  (optional)
filter_resource_name__icontains = 'filter_resource_name__icontains_example' # str |  (optional)
filter_resource_name__in = ['filter_resource_name__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_resource_type = 'filter_resource_type_example' # str |  (optional)
filter_resource_type__icontains = 'filter_resource_type__icontains_example' # str |  (optional)
filter_resource_type__in = ['filter_resource_type__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_resource_uid = 'filter_resource_uid_example' # str |  (optional)
filter_resource_uid__icontains = 'filter_resource_uid__icontains_example' # str |  (optional)
filter_resource_uid__in = ['filter_resource_uid__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_resources = ['filter_resources_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_scan = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
filter_scan__in = ['filter_scan__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_search = 'filter_search_example' # str | A search term. (optional)
filter_service = 'filter_service_example' # str |  (optional)
filter_service__icontains = 'filter_service__icontains_example' # str |  (optional)
filter_service__in = ['filter_service__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_severity = 'filter_severity_example' # str | * `critical` - Critical * `high` - High * `medium` - Medium * `low` - Low * `informational` - Informational (optional)
filter_severity__in = ['filter_severity__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_status = 'filter_status_example' # str | * `FAIL` - Fail * `PASS` - Pass * `MANUAL` - Manual * `MUTED` - Muted (optional)
filter_status__in = ['filter_status__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_uid = 'filter_uid_example' # str |  (optional)
filter_uid__in = ['filter_uid__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_updated_at = '2013-10-20' # date |  (optional)
filter_updated_at__gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_updated_at__lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
sort = ['sort_example'] # list[str] | [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) (optional)

try:
    # Retrieve metadata values from findings
    api_response = api_instance.findings_metadata_retrieve(filter_inserted_at, fields_findings_metadata=fields_findings_metadata, filter_check_id=filter_check_id, filter_check_id__icontains=filter_check_id__icontains, filter_check_id__in=filter_check_id__in, filter_delta=filter_delta, filter_delta__in=filter_delta__in, filter_id=filter_id, filter_id__in=filter_id__in, filter_impact=filter_impact, filter_impact__in=filter_impact__in, filter_inserted_at__date=filter_inserted_at__date, filter_inserted_at__gte=filter_inserted_at__gte, filter_inserted_at__lte=filter_inserted_at__lte, filter_provider=filter_provider, filter_provider__in=filter_provider__in, filter_provider_alias=filter_provider_alias, filter_provider_alias__icontains=filter_provider_alias__icontains, filter_provider_alias__in=filter_provider_alias__in, filter_provider_type=filter_provider_type, filter_provider_type__in=filter_provider_type__in, filter_provider_uid=filter_provider_uid, filter_provider_uid__icontains=filter_provider_uid__icontains, filter_provider_uid__in=filter_provider_uid__in, filter_region=filter_region, filter_region__icontains=filter_region__icontains, filter_region__in=filter_region__in, filter_resource_name=filter_resource_name, filter_resource_name__icontains=filter_resource_name__icontains, filter_resource_name__in=filter_resource_name__in, filter_resource_type=filter_resource_type, filter_resource_type__icontains=filter_resource_type__icontains, filter_resource_type__in=filter_resource_type__in, filter_resource_uid=filter_resource_uid, filter_resource_uid__icontains=filter_resource_uid__icontains, filter_resource_uid__in=filter_resource_uid__in, filter_resources=filter_resources, filter_scan=filter_scan, filter_scan__in=filter_scan__in, filter_search=filter_search, filter_service=filter_service, filter_service__icontains=filter_service__icontains, filter_service__in=filter_service__in, filter_severity=filter_severity, filter_severity__in=filter_severity__in, filter_status=filter_status, filter_status__in=filter_status__in, filter_uid=filter_uid, filter_uid__in=filter_uid__in, filter_updated_at=filter_updated_at, filter_updated_at__gte=filter_updated_at__gte, filter_updated_at__lte=filter_updated_at__lte, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FindingApi->findings_metadata_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_inserted_at** | **date**| At least one of the variations of the &#x60;filter[inserted_at]&#x60; filter must be provided. | 
 **fields_findings_metadata** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 
 **filter_check_id** | **str**|  | [optional] 
 **filter_check_id__icontains** | **str**|  | [optional] 
 **filter_check_id__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_delta** | **str**| * &#x60;new&#x60; - New * &#x60;changed&#x60; - Changed | [optional] 
 **filter_delta__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_id** | [**str**](.md)|  | [optional] 
 **filter_id__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_impact** | **str**| * &#x60;critical&#x60; - Critical * &#x60;high&#x60; - High * &#x60;medium&#x60; - Medium * &#x60;low&#x60; - Low * &#x60;informational&#x60; - Informational | [optional] 
 **filter_impact__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_inserted_at__date** | **date**|  | [optional] 
 **filter_inserted_at__gte** | **date**| Maximum date range is 7 days. | [optional] 
 **filter_inserted_at__lte** | **date**| Maximum date range is 7 days. | [optional] 
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
 **filter_region** | **str**|  | [optional] 
 **filter_region__icontains** | **str**|  | [optional] 
 **filter_region__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_resource_name** | **str**|  | [optional] 
 **filter_resource_name__icontains** | **str**|  | [optional] 
 **filter_resource_name__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_resource_type** | **str**|  | [optional] 
 **filter_resource_type__icontains** | **str**|  | [optional] 
 **filter_resource_type__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_resource_uid** | **str**|  | [optional] 
 **filter_resource_uid__icontains** | **str**|  | [optional] 
 **filter_resource_uid__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_resources** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_scan** | [**str**](.md)|  | [optional] 
 **filter_scan__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_search** | **str**| A search term. | [optional] 
 **filter_service** | **str**|  | [optional] 
 **filter_service__icontains** | **str**|  | [optional] 
 **filter_service__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_severity** | **str**| * &#x60;critical&#x60; - Critical * &#x60;high&#x60; - High * &#x60;medium&#x60; - Medium * &#x60;low&#x60; - Low * &#x60;informational&#x60; - Informational | [optional] 
 **filter_severity__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_status** | **str**| * &#x60;FAIL&#x60; - Fail * &#x60;PASS&#x60; - Pass * &#x60;MANUAL&#x60; - Manual * &#x60;MUTED&#x60; - Muted | [optional] 
 **filter_status__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_uid** | **str**|  | [optional] 
 **filter_uid__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_updated_at** | **date**|  | [optional] 
 **filter_updated_at__gte** | **datetime**|  | [optional] 
 **filter_updated_at__lte** | **datetime**|  | [optional] 
 **sort** | [**list[str]**](str.md)| [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) | [optional] 

### Return type

[**FindingMetadataResponse**](FindingMetadataResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_retrieve**
> FindingResponse findings_retrieve(id, fields_findings=fields_findings, include=include)

Retrieve data from a specific finding

Fetch detailed information about a specific finding by its ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FindingApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this finding.
fields_findings = ['fields_findings_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)
include = ['include_example'] # list[str] | include query parameter to allow the client to customize which related resources should be returned. (optional)

try:
    # Retrieve data from a specific finding
    api_response = api_instance.findings_retrieve(id, fields_findings=fields_findings, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FindingApi->findings_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this finding. | 
 **fields_findings** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 
 **include** | [**list[str]**](str.md)| include query parameter to allow the client to customize which related resources should be returned. | [optional] 

### Return type

[**FindingResponse**](FindingResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

