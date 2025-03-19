# swagger_client.ProviderGroupApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**provider_groups_create**](ProviderGroupApi.md#provider_groups_create) | **POST** /api/v1/provider-groups | Create a new provider group
[**provider_groups_destroy**](ProviderGroupApi.md#provider_groups_destroy) | **DELETE** /api/v1/provider-groups/{id} | Delete a provider group
[**provider_groups_list**](ProviderGroupApi.md#provider_groups_list) | **GET** /api/v1/provider-groups | List all provider groups
[**provider_groups_partial_update**](ProviderGroupApi.md#provider_groups_partial_update) | **PATCH** /api/v1/provider-groups/{id} | Partially update a provider group
[**provider_groups_relationships_providers_create**](ProviderGroupApi.md#provider_groups_relationships_providers_create) | **POST** /api/v1/provider-groups/{id}/relationships/providers | Create a new provider_group-providers relationship
[**provider_groups_relationships_providers_destroy**](ProviderGroupApi.md#provider_groups_relationships_providers_destroy) | **DELETE** /api/v1/provider-groups/{id}/relationships/providers | Delete a provider_group-providers relationship
[**provider_groups_relationships_providers_partial_update**](ProviderGroupApi.md#provider_groups_relationships_providers_partial_update) | **PATCH** /api/v1/provider-groups/{id}/relationships/providers | Partially update a provider_group-providers relationship
[**provider_groups_retrieve**](ProviderGroupApi.md#provider_groups_retrieve) | **GET** /api/v1/provider-groups/{id} | Retrieve data from a provider group

# **provider_groups_create**
> ProviderGroupCreateResponse provider_groups_create(body)

Create a new provider group

Add a new provider group to the system by providing the required provider group details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProviderGroupApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProviderGroupCreateRequest() # ProviderGroupCreateRequest | 

try:
    # Create a new provider group
    api_response = api_instance.provider_groups_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderGroupApi->provider_groups_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProviderGroupCreateRequest**](ProviderGroupCreateRequest.md)|  | 

### Return type

[**ProviderGroupCreateResponse**](ProviderGroupCreateResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **provider_groups_destroy**
> provider_groups_destroy(id)

Delete a provider group

Remove a provider group from the system by their ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProviderGroupApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this provider group.

try:
    # Delete a provider group
    api_instance.provider_groups_destroy(id)
except ApiException as e:
    print("Exception when calling ProviderGroupApi->provider_groups_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this provider group. | 

### Return type

void (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **provider_groups_list**
> PaginatedProviderGroupList provider_groups_list(fields_provider_groups=fields_provider_groups, filter_id=filter_id, filter_id__in=filter_id__in, filter_inserted_at=filter_inserted_at, filter_inserted_at__gte=filter_inserted_at__gte, filter_inserted_at__lte=filter_inserted_at__lte, filter_name=filter_name, filter_name__in=filter_name__in, filter_search=filter_search, filter_updated_at=filter_updated_at, filter_updated_at__gte=filter_updated_at__gte, filter_updated_at__lte=filter_updated_at__lte, page_number=page_number, page_size=page_size, sort=sort)

List all provider groups

Retrieve a list of all provider groups with options for filtering by various criteria.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProviderGroupApi(swagger_client.ApiClient(configuration))
fields_provider_groups = ['fields_provider_groups_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)
filter_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
filter_id__in = ['filter_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_inserted_at = '2013-10-20' # date |  (optional)
filter_inserted_at__gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_inserted_at__lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_name = 'filter_name_example' # str |  (optional)
filter_name__in = ['filter_name__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_search = 'filter_search_example' # str | A search term. (optional)
filter_updated_at = '2013-10-20' # date |  (optional)
filter_updated_at__gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_updated_at__lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
page_number = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
sort = ['sort_example'] # list[str] | [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) (optional)

try:
    # List all provider groups
    api_response = api_instance.provider_groups_list(fields_provider_groups=fields_provider_groups, filter_id=filter_id, filter_id__in=filter_id__in, filter_inserted_at=filter_inserted_at, filter_inserted_at__gte=filter_inserted_at__gte, filter_inserted_at__lte=filter_inserted_at__lte, filter_name=filter_name, filter_name__in=filter_name__in, filter_search=filter_search, filter_updated_at=filter_updated_at, filter_updated_at__gte=filter_updated_at__gte, filter_updated_at__lte=filter_updated_at__lte, page_number=page_number, page_size=page_size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderGroupApi->provider_groups_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields_provider_groups** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 
 **filter_id** | [**str**](.md)|  | [optional] 
 **filter_id__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_inserted_at** | **date**|  | [optional] 
 **filter_inserted_at__gte** | **datetime**|  | [optional] 
 **filter_inserted_at__lte** | **datetime**|  | [optional] 
 **filter_name** | **str**|  | [optional] 
 **filter_name__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_search** | **str**| A search term. | [optional] 
 **filter_updated_at** | **date**|  | [optional] 
 **filter_updated_at__gte** | **datetime**|  | [optional] 
 **filter_updated_at__lte** | **datetime**|  | [optional] 
 **page_number** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **sort** | [**list[str]**](str.md)| [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) | [optional] 

### Return type

[**PaginatedProviderGroupList**](PaginatedProviderGroupList.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **provider_groups_partial_update**
> SerializerMetaclassResponse provider_groups_partial_update(body, id)

Partially update a provider group

Update certain fields of an existing provider group's information without affecting other fields.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProviderGroupApi(swagger_client.ApiClient(configuration))
body = swagger_client.PatchedProviderGroupUpdateRequest() # PatchedProviderGroupUpdateRequest | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this provider group.

try:
    # Partially update a provider group
    api_response = api_instance.provider_groups_partial_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderGroupApi->provider_groups_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchedProviderGroupUpdateRequest**](PatchedProviderGroupUpdateRequest.md)|  | 
 **id** | [**str**](.md)| A UUID string identifying this provider group. | 

### Return type

[**SerializerMetaclassResponse**](SerializerMetaclassResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **provider_groups_relationships_providers_create**
> provider_groups_relationships_providers_create(body)

Create a new provider_group-providers relationship

Add a new provider_group-providers relationship to the system by providing the required provider_group-providers details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProviderGroupApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProviderGroupMembershipRequest() # ProviderGroupMembershipRequest | 

try:
    # Create a new provider_group-providers relationship
    api_instance.provider_groups_relationships_providers_create(body)
except ApiException as e:
    print("Exception when calling ProviderGroupApi->provider_groups_relationships_providers_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProviderGroupMembershipRequest**](ProviderGroupMembershipRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **provider_groups_relationships_providers_destroy**
> provider_groups_relationships_providers_destroy()

Delete a provider_group-providers relationship

Remove the provider_group-providers relationship from the system by their ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProviderGroupApi(swagger_client.ApiClient(configuration))

try:
    # Delete a provider_group-providers relationship
    api_instance.provider_groups_relationships_providers_destroy()
except ApiException as e:
    print("Exception when calling ProviderGroupApi->provider_groups_relationships_providers_destroy: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **provider_groups_relationships_providers_partial_update**
> provider_groups_relationships_providers_partial_update(body)

Partially update a provider_group-providers relationship

Update the provider_group-providers relationship information without affecting other fields.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProviderGroupApi(swagger_client.ApiClient(configuration))
body = swagger_client.PatchedProviderGroupMembershipRequest() # PatchedProviderGroupMembershipRequest | 

try:
    # Partially update a provider_group-providers relationship
    api_instance.provider_groups_relationships_providers_partial_update(body)
except ApiException as e:
    print("Exception when calling ProviderGroupApi->provider_groups_relationships_providers_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchedProviderGroupMembershipRequest**](PatchedProviderGroupMembershipRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **provider_groups_retrieve**
> ProviderGroupResponse provider_groups_retrieve(id, fields_provider_groups=fields_provider_groups)

Retrieve data from a provider group

Fetch detailed information about a specific provider group by their ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProviderGroupApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this provider group.
fields_provider_groups = ['fields_provider_groups_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)

try:
    # Retrieve data from a provider group
    api_response = api_instance.provider_groups_retrieve(id, fields_provider_groups=fields_provider_groups)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderGroupApi->provider_groups_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this provider group. | 
 **fields_provider_groups** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 

### Return type

[**ProviderGroupResponse**](ProviderGroupResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

