# swagger_client.RoleApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**roles_create**](RoleApi.md#roles_create) | **POST** /api/v1/roles | Create a new role
[**roles_destroy**](RoleApi.md#roles_destroy) | **DELETE** /api/v1/roles/{id} | Delete a role
[**roles_list**](RoleApi.md#roles_list) | **GET** /api/v1/roles | List all roles
[**roles_partial_update**](RoleApi.md#roles_partial_update) | **PATCH** /api/v1/roles/{id} | Partially update a role
[**roles_relationships_provider_groups_create**](RoleApi.md#roles_relationships_provider_groups_create) | **POST** /api/v1/roles/{id}/relationships/provider_groups | Create a new role-provider_groups relationship
[**roles_relationships_provider_groups_destroy**](RoleApi.md#roles_relationships_provider_groups_destroy) | **DELETE** /api/v1/roles/{id}/relationships/provider_groups | Delete a role-provider_groups relationship
[**roles_relationships_provider_groups_partial_update**](RoleApi.md#roles_relationships_provider_groups_partial_update) | **PATCH** /api/v1/roles/{id}/relationships/provider_groups | Partially update a role-provider_groups relationship
[**roles_retrieve**](RoleApi.md#roles_retrieve) | **GET** /api/v1/roles/{id} | Retrieve data from a role

# **roles_create**
> RoleCreateResponse roles_create(body)

Create a new role

Add a new role to the system by providing the required role details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RoleApi(swagger_client.ApiClient(configuration))
body = swagger_client.RoleCreateRequest() # RoleCreateRequest | 

try:
    # Create a new role
    api_response = api_instance.roles_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->roles_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleCreateRequest**](RoleCreateRequest.md)|  | 

### Return type

[**RoleCreateResponse**](RoleCreateResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_destroy**
> roles_destroy(id)

Delete a role

Remove a role from the system by their ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RoleApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this role.

try:
    # Delete a role
    api_instance.roles_destroy(id)
except ApiException as e:
    print("Exception when calling RoleApi->roles_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this role. | 

### Return type

void (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_list**
> PaginatedRoleList roles_list(fields_roles=fields_roles, filter_id=filter_id, filter_id__in=filter_id__in, filter_inserted_at=filter_inserted_at, filter_inserted_at__gte=filter_inserted_at__gte, filter_inserted_at__lte=filter_inserted_at__lte, filter_name=filter_name, filter_name__in=filter_name__in, filter_permission_state=filter_permission_state, filter_search=filter_search, filter_updated_at=filter_updated_at, filter_updated_at__gte=filter_updated_at__gte, filter_updated_at__lte=filter_updated_at__lte, page_number=page_number, page_size=page_size, sort=sort)

List all roles

Retrieve a list of all roles with options for filtering by various criteria.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RoleApi(swagger_client.ApiClient(configuration))
fields_roles = ['fields_roles_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)
filter_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
filter_id__in = ['filter_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_inserted_at = '2013-10-20' # date |  (optional)
filter_inserted_at__gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_inserted_at__lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_name = 'filter_name_example' # str |  (optional)
filter_name__in = ['filter_name__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_permission_state = 'filter_permission_state_example' # str | * `unlimited` - Unlimited permissions * `limited` - Limited permissions * `none` - No permissions (optional)
filter_search = 'filter_search_example' # str | A search term. (optional)
filter_updated_at = '2013-10-20' # date |  (optional)
filter_updated_at__gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_updated_at__lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
page_number = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
sort = ['sort_example'] # list[str] | [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) (optional)

try:
    # List all roles
    api_response = api_instance.roles_list(fields_roles=fields_roles, filter_id=filter_id, filter_id__in=filter_id__in, filter_inserted_at=filter_inserted_at, filter_inserted_at__gte=filter_inserted_at__gte, filter_inserted_at__lte=filter_inserted_at__lte, filter_name=filter_name, filter_name__in=filter_name__in, filter_permission_state=filter_permission_state, filter_search=filter_search, filter_updated_at=filter_updated_at, filter_updated_at__gte=filter_updated_at__gte, filter_updated_at__lte=filter_updated_at__lte, page_number=page_number, page_size=page_size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->roles_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields_roles** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 
 **filter_id** | [**str**](.md)|  | [optional] 
 **filter_id__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_inserted_at** | **date**|  | [optional] 
 **filter_inserted_at__gte** | **datetime**|  | [optional] 
 **filter_inserted_at__lte** | **datetime**|  | [optional] 
 **filter_name** | **str**|  | [optional] 
 **filter_name__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_permission_state** | **str**| * &#x60;unlimited&#x60; - Unlimited permissions * &#x60;limited&#x60; - Limited permissions * &#x60;none&#x60; - No permissions | [optional] 
 **filter_search** | **str**| A search term. | [optional] 
 **filter_updated_at** | **date**|  | [optional] 
 **filter_updated_at__gte** | **datetime**|  | [optional] 
 **filter_updated_at__lte** | **datetime**|  | [optional] 
 **page_number** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **sort** | [**list[str]**](str.md)| [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) | [optional] 

### Return type

[**PaginatedRoleList**](PaginatedRoleList.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_partial_update**
> SerializerMetaclassResponse roles_partial_update(body, id)

Partially update a role

Update certain fields of an existing role's information without affecting other fields.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RoleApi(swagger_client.ApiClient(configuration))
body = swagger_client.PatchedRoleUpdateRequest() # PatchedRoleUpdateRequest | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this role.

try:
    # Partially update a role
    api_response = api_instance.roles_partial_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->roles_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchedRoleUpdateRequest**](PatchedRoleUpdateRequest.md)|  | 
 **id** | [**str**](.md)| A UUID string identifying this role. | 

### Return type

[**SerializerMetaclassResponse**](SerializerMetaclassResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_relationships_provider_groups_create**
> roles_relationships_provider_groups_create(body)

Create a new role-provider_groups relationship

Add a new role-provider_groups relationship to the system by providing the required role-provider_groups details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RoleApi(swagger_client.ApiClient(configuration))
body = swagger_client.RoleProviderGroupRelationshipRequest() # RoleProviderGroupRelationshipRequest | 

try:
    # Create a new role-provider_groups relationship
    api_instance.roles_relationships_provider_groups_create(body)
except ApiException as e:
    print("Exception when calling RoleApi->roles_relationships_provider_groups_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleProviderGroupRelationshipRequest**](RoleProviderGroupRelationshipRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_relationships_provider_groups_destroy**
> roles_relationships_provider_groups_destroy()

Delete a role-provider_groups relationship

Remove the role-provider_groups relationship from the system by their ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RoleApi(swagger_client.ApiClient(configuration))

try:
    # Delete a role-provider_groups relationship
    api_instance.roles_relationships_provider_groups_destroy()
except ApiException as e:
    print("Exception when calling RoleApi->roles_relationships_provider_groups_destroy: %s\n" % e)
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

# **roles_relationships_provider_groups_partial_update**
> roles_relationships_provider_groups_partial_update(body)

Partially update a role-provider_groups relationship

Update the role-provider_groups relationship information without affecting other fields.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RoleApi(swagger_client.ApiClient(configuration))
body = swagger_client.PatchedRoleProviderGroupRelationshipRequest() # PatchedRoleProviderGroupRelationshipRequest | 

try:
    # Partially update a role-provider_groups relationship
    api_instance.roles_relationships_provider_groups_partial_update(body)
except ApiException as e:
    print("Exception when calling RoleApi->roles_relationships_provider_groups_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchedRoleProviderGroupRelationshipRequest**](PatchedRoleProviderGroupRelationshipRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_retrieve**
> RoleResponse roles_retrieve(id, fields_roles=fields_roles)

Retrieve data from a role

Fetch detailed information about a specific role by their ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RoleApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this role.
fields_roles = ['fields_roles_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)

try:
    # Retrieve data from a role
    api_response = api_instance.roles_retrieve(id, fields_roles=fields_roles)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->roles_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this role. | 
 **fields_roles** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 

### Return type

[**RoleResponse**](RoleResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

