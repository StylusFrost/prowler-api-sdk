# swagger_client.TenantApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenants_create**](TenantApi.md#tenants_create) | **POST** /api/v1/tenants | Create a new tenant
[**tenants_destroy**](TenantApi.md#tenants_destroy) | **DELETE** /api/v1/tenants/{id} | Delete a tenant
[**tenants_list**](TenantApi.md#tenants_list) | **GET** /api/v1/tenants | List all tenants
[**tenants_memberships_destroy**](TenantApi.md#tenants_memberships_destroy) | **DELETE** /api/v1/tenants/{tenant_pk}/memberships/{id} | Delete tenant memberships
[**tenants_memberships_list**](TenantApi.md#tenants_memberships_list) | **GET** /api/v1/tenants/{tenant_pk}/memberships | List tenant memberships
[**tenants_partial_update**](TenantApi.md#tenants_partial_update) | **PATCH** /api/v1/tenants/{id} | Partially update a tenant
[**tenants_retrieve**](TenantApi.md#tenants_retrieve) | **GET** /api/v1/tenants/{id} | Retrieve data from a tenant

# **tenants_create**
> TenantResponse tenants_create(body)

Create a new tenant

Add a new tenant to the system by providing the required tenant details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TenantApi(swagger_client.ApiClient(configuration))
body = swagger_client.TenantRequest() # TenantRequest | 

try:
    # Create a new tenant
    api_response = api_instance.tenants_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->tenants_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TenantRequest**](TenantRequest.md)|  | 

### Return type

[**TenantResponse**](TenantResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_destroy**
> tenants_destroy(id)

Delete a tenant

Remove a tenant from the system by their ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TenantApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this tenant.

try:
    # Delete a tenant
    api_instance.tenants_destroy(id)
except ApiException as e:
    print("Exception when calling TenantApi->tenants_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this tenant. | 

### Return type

void (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_list**
> PaginatedTenantList tenants_list(fields_tenants=fields_tenants, filter_inserted_at=filter_inserted_at, filter_inserted_at__date=filter_inserted_at__date, filter_inserted_at__gte=filter_inserted_at__gte, filter_inserted_at__lte=filter_inserted_at__lte, filter_name=filter_name, filter_name__icontains=filter_name__icontains, filter_search=filter_search, filter_updated_at=filter_updated_at, filter_updated_at__gte=filter_updated_at__gte, filter_updated_at__lte=filter_updated_at__lte, page_number=page_number, page_size=page_size, sort=sort)

List all tenants

Retrieve a list of all tenants with options for filtering by various criteria.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TenantApi(swagger_client.ApiClient(configuration))
fields_tenants = ['fields_tenants_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)
filter_inserted_at = '2013-10-20' # date |  (optional)
filter_inserted_at__date = '2013-10-20' # date |  (optional)
filter_inserted_at__gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_inserted_at__lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_name = 'filter_name_example' # str |  (optional)
filter_name__icontains = 'filter_name__icontains_example' # str |  (optional)
filter_search = 'filter_search_example' # str | A search term. (optional)
filter_updated_at = '2013-10-20' # date |  (optional)
filter_updated_at__gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_updated_at__lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
page_number = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
sort = ['sort_example'] # list[str] | [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) (optional)

try:
    # List all tenants
    api_response = api_instance.tenants_list(fields_tenants=fields_tenants, filter_inserted_at=filter_inserted_at, filter_inserted_at__date=filter_inserted_at__date, filter_inserted_at__gte=filter_inserted_at__gte, filter_inserted_at__lte=filter_inserted_at__lte, filter_name=filter_name, filter_name__icontains=filter_name__icontains, filter_search=filter_search, filter_updated_at=filter_updated_at, filter_updated_at__gte=filter_updated_at__gte, filter_updated_at__lte=filter_updated_at__lte, page_number=page_number, page_size=page_size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->tenants_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields_tenants** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 
 **filter_inserted_at** | **date**|  | [optional] 
 **filter_inserted_at__date** | **date**|  | [optional] 
 **filter_inserted_at__gte** | **datetime**|  | [optional] 
 **filter_inserted_at__lte** | **datetime**|  | [optional] 
 **filter_name** | **str**|  | [optional] 
 **filter_name__icontains** | **str**|  | [optional] 
 **filter_search** | **str**| A search term. | [optional] 
 **filter_updated_at** | **date**|  | [optional] 
 **filter_updated_at__gte** | **datetime**|  | [optional] 
 **filter_updated_at__lte** | **datetime**|  | [optional] 
 **page_number** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **sort** | [**list[str]**](str.md)| [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) | [optional] 

### Return type

[**PaginatedTenantList**](PaginatedTenantList.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_memberships_destroy**
> tenants_memberships_destroy(id, tenant_pk)

Delete tenant memberships

Delete the membership details of users in a tenant. You need to be one of the owners to delete a membership that is not yours. If you are the last owner of a tenant, you cannot delete your own membership.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TenantApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this membership.
tenant_pk = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Delete tenant memberships
    api_instance.tenants_memberships_destroy(id, tenant_pk)
except ApiException as e:
    print("Exception when calling TenantApi->tenants_memberships_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this membership. | 
 **tenant_pk** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_memberships_list**
> PaginatedMembershipList tenants_memberships_list(tenant_pk, fields_memberships=fields_memberships, filter_search=filter_search, page_number=page_number, page_size=page_size, sort=sort)

List tenant memberships

List the membership details of users in a tenant you are a part of.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TenantApi(swagger_client.ApiClient(configuration))
tenant_pk = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Tenant ID
fields_memberships = ['fields_memberships_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)
filter_search = 'filter_search_example' # str | A search term. (optional)
page_number = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
sort = ['sort_example'] # list[str] | [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) (optional)

try:
    # List tenant memberships
    api_response = api_instance.tenants_memberships_list(tenant_pk, fields_memberships=fields_memberships, filter_search=filter_search, page_number=page_number, page_size=page_size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->tenants_memberships_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_pk** | [**str**](.md)| Tenant ID | 
 **fields_memberships** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 
 **filter_search** | **str**| A search term. | [optional] 
 **page_number** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **sort** | [**list[str]**](str.md)| [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) | [optional] 

### Return type

[**PaginatedMembershipList**](PaginatedMembershipList.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_partial_update**
> TenantResponse tenants_partial_update(body, id)

Partially update a tenant

Update certain fields of an existing tenant's information without affecting other fields.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TenantApi(swagger_client.ApiClient(configuration))
body = swagger_client.PatchedTenantRequest() # PatchedTenantRequest | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this tenant.

try:
    # Partially update a tenant
    api_response = api_instance.tenants_partial_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->tenants_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchedTenantRequest**](PatchedTenantRequest.md)|  | 
 **id** | [**str**](.md)| A UUID string identifying this tenant. | 

### Return type

[**TenantResponse**](TenantResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_retrieve**
> TenantResponse tenants_retrieve(id, fields_tenants=fields_tenants)

Retrieve data from a tenant

Fetch detailed information about a specific tenant by their ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TenantApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this tenant.
fields_tenants = ['fields_tenants_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)

try:
    # Retrieve data from a tenant
    api_response = api_instance.tenants_retrieve(id, fields_tenants=fields_tenants)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->tenants_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this tenant. | 
 **fields_tenants** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 

### Return type

[**TenantResponse**](TenantResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

