# swagger_client.ResourceApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resources_list**](ResourceApi.md#resources_list) | **GET** /api/v1/resources | List all resources
[**resources_retrieve**](ResourceApi.md#resources_retrieve) | **GET** /api/v1/resources/{id} | Retrieve data for a resource

# **resources_list**
> PaginatedResourceList resources_list(fields_resources=fields_resources, filter_inserted_at=filter_inserted_at, filter_inserted_at__gte=filter_inserted_at__gte, filter_inserted_at__lte=filter_inserted_at__lte, filter_name=filter_name, filter_name__icontains=filter_name__icontains, filter_provider=filter_provider, filter_provider__in=filter_provider__in, filter_provider_alias=filter_provider_alias, filter_provider_alias__icontains=filter_provider_alias__icontains, filter_provider_alias__in=filter_provider_alias__in, filter_provider_type=filter_provider_type, filter_provider_type__in=filter_provider_type__in, filter_provider_uid=filter_provider_uid, filter_provider_uid__icontains=filter_provider_uid__icontains, filter_provider_uid__in=filter_provider_uid__in, filter_region=filter_region, filter_region__icontains=filter_region__icontains, filter_region__in=filter_region__in, filter_search=filter_search, filter_service=filter_service, filter_service__icontains=filter_service__icontains, filter_service__in=filter_service__in, filter_tag=filter_tag, filter_tag_key=filter_tag_key, filter_tag_value=filter_tag_value, filter_tags=filter_tags, filter_type=filter_type, filter_type__icontains=filter_type__icontains, filter_type__in=filter_type__in, filter_uid=filter_uid, filter_uid__icontains=filter_uid__icontains, filter_updated_at=filter_updated_at, filter_updated_at__gte=filter_updated_at__gte, filter_updated_at__lte=filter_updated_at__lte, include=include, page_number=page_number, page_size=page_size, sort=sort)

List all resources

Retrieve a list of all resources with options for filtering by various criteria. Resources are objects that are discovered by Prowler. They can be anything from a single host to a whole VPC.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ResourceApi(swagger_client.ApiClient(configuration))
fields_resources = ['fields_resources_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)
filter_inserted_at = '2013-10-20' # date |  (optional)
filter_inserted_at__gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_inserted_at__lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_name = 'filter_name_example' # str |  (optional)
filter_name__icontains = 'filter_name__icontains_example' # str |  (optional)
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
filter_search = 'filter_search_example' # str | A search term. (optional)
filter_service = 'filter_service_example' # str |  (optional)
filter_service__icontains = 'filter_service__icontains_example' # str |  (optional)
filter_service__in = ['filter_service__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_tag = 'filter_tag_example' # str |  (optional)
filter_tag_key = 'filter_tag_key_example' # str |  (optional)
filter_tag_value = 'filter_tag_value_example' # str |  (optional)
filter_tags = 'filter_tags_example' # str |  (optional)
filter_type = 'filter_type_example' # str |  (optional)
filter_type__icontains = 'filter_type__icontains_example' # str |  (optional)
filter_type__in = ['filter_type__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_uid = 'filter_uid_example' # str |  (optional)
filter_uid__icontains = 'filter_uid__icontains_example' # str |  (optional)
filter_updated_at = '2013-10-20' # date |  (optional)
filter_updated_at__gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_updated_at__lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
include = ['include_example'] # list[str] | include query parameter to allow the client to customize which related resources should be returned. (optional)
page_number = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
sort = ['sort_example'] # list[str] | [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) (optional)

try:
    # List all resources
    api_response = api_instance.resources_list(fields_resources=fields_resources, filter_inserted_at=filter_inserted_at, filter_inserted_at__gte=filter_inserted_at__gte, filter_inserted_at__lte=filter_inserted_at__lte, filter_name=filter_name, filter_name__icontains=filter_name__icontains, filter_provider=filter_provider, filter_provider__in=filter_provider__in, filter_provider_alias=filter_provider_alias, filter_provider_alias__icontains=filter_provider_alias__icontains, filter_provider_alias__in=filter_provider_alias__in, filter_provider_type=filter_provider_type, filter_provider_type__in=filter_provider_type__in, filter_provider_uid=filter_provider_uid, filter_provider_uid__icontains=filter_provider_uid__icontains, filter_provider_uid__in=filter_provider_uid__in, filter_region=filter_region, filter_region__icontains=filter_region__icontains, filter_region__in=filter_region__in, filter_search=filter_search, filter_service=filter_service, filter_service__icontains=filter_service__icontains, filter_service__in=filter_service__in, filter_tag=filter_tag, filter_tag_key=filter_tag_key, filter_tag_value=filter_tag_value, filter_tags=filter_tags, filter_type=filter_type, filter_type__icontains=filter_type__icontains, filter_type__in=filter_type__in, filter_uid=filter_uid, filter_uid__icontains=filter_uid__icontains, filter_updated_at=filter_updated_at, filter_updated_at__gte=filter_updated_at__gte, filter_updated_at__lte=filter_updated_at__lte, include=include, page_number=page_number, page_size=page_size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceApi->resources_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields_resources** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 
 **filter_inserted_at** | **date**|  | [optional] 
 **filter_inserted_at__gte** | **datetime**|  | [optional] 
 **filter_inserted_at__lte** | **datetime**|  | [optional] 
 **filter_name** | **str**|  | [optional] 
 **filter_name__icontains** | **str**|  | [optional] 
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
 **filter_search** | **str**| A search term. | [optional] 
 **filter_service** | **str**|  | [optional] 
 **filter_service__icontains** | **str**|  | [optional] 
 **filter_service__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_tag** | **str**|  | [optional] 
 **filter_tag_key** | **str**|  | [optional] 
 **filter_tag_value** | **str**|  | [optional] 
 **filter_tags** | **str**|  | [optional] 
 **filter_type** | **str**|  | [optional] 
 **filter_type__icontains** | **str**|  | [optional] 
 **filter_type__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_uid** | **str**|  | [optional] 
 **filter_uid__icontains** | **str**|  | [optional] 
 **filter_updated_at** | **date**|  | [optional] 
 **filter_updated_at__gte** | **datetime**|  | [optional] 
 **filter_updated_at__lte** | **datetime**|  | [optional] 
 **include** | [**list[str]**](str.md)| include query parameter to allow the client to customize which related resources should be returned. | [optional] 
 **page_number** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **sort** | [**list[str]**](str.md)| [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) | [optional] 

### Return type

[**PaginatedResourceList**](PaginatedResourceList.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_retrieve**
> ResourceResponse resources_retrieve(id, fields_resources=fields_resources, include=include)

Retrieve data for a resource

Fetch detailed information about a specific resource by their ID. A Resource is an object that is discovered by Prowler. It can be anything from a single host to a whole VPC.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ResourceApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this resource.
fields_resources = ['fields_resources_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)
include = ['include_example'] # list[str] | include query parameter to allow the client to customize which related resources should be returned. (optional)

try:
    # Retrieve data for a resource
    api_response = api_instance.resources_retrieve(id, fields_resources=fields_resources, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceApi->resources_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this resource. | 
 **fields_resources** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 
 **include** | [**list[str]**](str.md)| include query parameter to allow the client to customize which related resources should be returned. | [optional] 

### Return type

[**ResourceResponse**](ResourceResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

