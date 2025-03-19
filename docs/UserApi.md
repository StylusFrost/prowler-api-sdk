# swagger_client.UserApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_create**](UserApi.md#users_create) | **POST** /api/v1/users | Register a new user
[**users_destroy**](UserApi.md#users_destroy) | **DELETE** /api/v1/users/{id} | Delete the user account
[**users_list**](UserApi.md#users_list) | **GET** /api/v1/users | List all users
[**users_me_retrieve**](UserApi.md#users_me_retrieve) | **GET** /api/v1/users/me | Retrieve the current user&#x27;s information
[**users_memberships_list**](UserApi.md#users_memberships_list) | **GET** /api/v1/users/{user_pk}/memberships | List user memberships
[**users_memberships_retrieve**](UserApi.md#users_memberships_retrieve) | **GET** /api/v1/users/{user_pk}/memberships/{id} | Retrieve membership data from the user
[**users_partial_update**](UserApi.md#users_partial_update) | **PATCH** /api/v1/users/{id} | Update user information
[**users_relationships_roles_create**](UserApi.md#users_relationships_roles_create) | **POST** /api/v1/users/{id}/relationships/roles | Create a new user-roles relationship
[**users_relationships_roles_destroy**](UserApi.md#users_relationships_roles_destroy) | **DELETE** /api/v1/users/{id}/relationships/roles | Delete a user-roles relationship
[**users_relationships_roles_partial_update**](UserApi.md#users_relationships_roles_partial_update) | **PATCH** /api/v1/users/{id}/relationships/roles | Partially update a user-roles relationship
[**users_retrieve**](UserApi.md#users_retrieve) | **GET** /api/v1/users/{id} | Retrieve a user&#x27;s information

# **users_create**
> UserCreateResponse users_create(body, invitation_token=invitation_token)

Register a new user

Create a new user account by providing the necessary registration details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserCreateRequest() # UserCreateRequest | 
invitation_token = 'invitation_token_example' # str | Optional invitation code for joining an existing tenant. (optional)

try:
    # Register a new user
    api_response = api_instance.users_create(body, invitation_token=invitation_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->users_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserCreateRequest**](UserCreateRequest.md)|  | 
 **invitation_token** | **str**| Optional invitation code for joining an existing tenant. | [optional] 

### Return type

[**UserCreateResponse**](UserCreateResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_destroy**
> users_destroy(id)

Delete the user account

Remove the current user account from the system.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this user.

try:
    # Delete the user account
    api_instance.users_destroy(id)
except ApiException as e:
    print("Exception when calling UserApi->users_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this user. | 

### Return type

void (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_list**
> PaginatedUserList users_list(fields_users=fields_users, filter_company_name=filter_company_name, filter_company_name__icontains=filter_company_name__icontains, filter_date_joined=filter_date_joined, filter_date_joined__date=filter_date_joined__date, filter_date_joined__gte=filter_date_joined__gte, filter_date_joined__lte=filter_date_joined__lte, filter_email=filter_email, filter_email__icontains=filter_email__icontains, filter_is_active=filter_is_active, filter_name=filter_name, filter_name__icontains=filter_name__icontains, filter_search=filter_search, include=include, page_number=page_number, page_size=page_size, sort=sort)

List all users

Retrieve a list of all users with options for filtering by various criteria.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
fields_users = ['fields_users_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)
filter_company_name = 'filter_company_name_example' # str |  (optional)
filter_company_name__icontains = 'filter_company_name__icontains_example' # str |  (optional)
filter_date_joined = '2013-10-20' # date |  (optional)
filter_date_joined__date = '2013-10-20' # date |  (optional)
filter_date_joined__gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_date_joined__lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_email = 'filter_email_example' # str |  (optional)
filter_email__icontains = 'filter_email__icontains_example' # str |  (optional)
filter_is_active = true # bool |  (optional)
filter_name = 'filter_name_example' # str |  (optional)
filter_name__icontains = 'filter_name__icontains_example' # str |  (optional)
filter_search = 'filter_search_example' # str | A search term. (optional)
include = ['include_example'] # list[str] | include query parameter to allow the client to customize which related resources should be returned. (optional)
page_number = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
sort = ['sort_example'] # list[str] | [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) (optional)

try:
    # List all users
    api_response = api_instance.users_list(fields_users=fields_users, filter_company_name=filter_company_name, filter_company_name__icontains=filter_company_name__icontains, filter_date_joined=filter_date_joined, filter_date_joined__date=filter_date_joined__date, filter_date_joined__gte=filter_date_joined__gte, filter_date_joined__lte=filter_date_joined__lte, filter_email=filter_email, filter_email__icontains=filter_email__icontains, filter_is_active=filter_is_active, filter_name=filter_name, filter_name__icontains=filter_name__icontains, filter_search=filter_search, include=include, page_number=page_number, page_size=page_size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->users_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields_users** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 
 **filter_company_name** | **str**|  | [optional] 
 **filter_company_name__icontains** | **str**|  | [optional] 
 **filter_date_joined** | **date**|  | [optional] 
 **filter_date_joined__date** | **date**|  | [optional] 
 **filter_date_joined__gte** | **datetime**|  | [optional] 
 **filter_date_joined__lte** | **datetime**|  | [optional] 
 **filter_email** | **str**|  | [optional] 
 **filter_email__icontains** | **str**|  | [optional] 
 **filter_is_active** | **bool**|  | [optional] 
 **filter_name** | **str**|  | [optional] 
 **filter_name__icontains** | **str**|  | [optional] 
 **filter_search** | **str**| A search term. | [optional] 
 **include** | [**list[str]**](str.md)| include query parameter to allow the client to customize which related resources should be returned. | [optional] 
 **page_number** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **sort** | [**list[str]**](str.md)| [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) | [optional] 

### Return type

[**PaginatedUserList**](PaginatedUserList.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_me_retrieve**
> UserResponse users_me_retrieve(fields_users=fields_users, include=include)

Retrieve the current user's information

Fetch detailed information about the authenticated user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
fields_users = ['fields_users_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)
include = ['include_example'] # list[str] | include query parameter to allow the client to customize which related resources should be returned. (optional)

try:
    # Retrieve the current user's information
    api_response = api_instance.users_me_retrieve(fields_users=fields_users, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->users_me_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields_users** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 
 **include** | [**list[str]**](str.md)| include query parameter to allow the client to customize which related resources should be returned. | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_memberships_list**
> PaginatedMembershipList users_memberships_list(user_pk, fields_memberships=fields_memberships, filter_date_joined=filter_date_joined, filter_date_joined__date=filter_date_joined__date, filter_date_joined__gte=filter_date_joined__gte, filter_date_joined__lte=filter_date_joined__lte, filter_role=filter_role, filter_search=filter_search, filter_tenant=filter_tenant, page_number=page_number, page_size=page_size, sort=sort)

List user memberships

Retrieve a list of all user memberships with options for filtering by various criteria.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_pk = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
fields_memberships = ['fields_memberships_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)
filter_date_joined = '2013-10-20' # date |  (optional)
filter_date_joined__date = '2013-10-20' # date |  (optional)
filter_date_joined__gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_date_joined__lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_role = 'filter_role_example' # str | * `owner` - Owner * `member` - Member (optional)
filter_search = 'filter_search_example' # str | A search term. (optional)
filter_tenant = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
page_number = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
sort = ['sort_example'] # list[str] | [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) (optional)

try:
    # List user memberships
    api_response = api_instance.users_memberships_list(user_pk, fields_memberships=fields_memberships, filter_date_joined=filter_date_joined, filter_date_joined__date=filter_date_joined__date, filter_date_joined__gte=filter_date_joined__gte, filter_date_joined__lte=filter_date_joined__lte, filter_role=filter_role, filter_search=filter_search, filter_tenant=filter_tenant, page_number=page_number, page_size=page_size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->users_memberships_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_pk** | [**str**](.md)|  | 
 **fields_memberships** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 
 **filter_date_joined** | **date**|  | [optional] 
 **filter_date_joined__date** | **date**|  | [optional] 
 **filter_date_joined__gte** | **datetime**|  | [optional] 
 **filter_date_joined__lte** | **datetime**|  | [optional] 
 **filter_role** | **str**| * &#x60;owner&#x60; - Owner * &#x60;member&#x60; - Member | [optional] 
 **filter_search** | **str**| A search term. | [optional] 
 **filter_tenant** | [**str**](.md)|  | [optional] 
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

# **users_memberships_retrieve**
> MembershipResponse users_memberships_retrieve(id, user_pk, fields_memberships=fields_memberships)

Retrieve membership data from the user

Fetch detailed information about a specific user membership by their ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this membership.
user_pk = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
fields_memberships = ['fields_memberships_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)

try:
    # Retrieve membership data from the user
    api_response = api_instance.users_memberships_retrieve(id, user_pk, fields_memberships=fields_memberships)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->users_memberships_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this membership. | 
 **user_pk** | [**str**](.md)|  | 
 **fields_memberships** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 

### Return type

[**MembershipResponse**](MembershipResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_partial_update**
> UserUpdateResponse users_partial_update(body, id)

Update user information

Partially update information about a user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
body = swagger_client.PatchedUserUpdateRequest() # PatchedUserUpdateRequest | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this user.

try:
    # Update user information
    api_response = api_instance.users_partial_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->users_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchedUserUpdateRequest**](PatchedUserUpdateRequest.md)|  | 
 **id** | [**str**](.md)| A UUID string identifying this user. | 

### Return type

[**UserUpdateResponse**](UserUpdateResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_relationships_roles_create**
> users_relationships_roles_create(body)

Create a new user-roles relationship

Add a new user-roles relationship to the system by providing the required user-roles details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserRoleRelationshipRequest() # UserRoleRelationshipRequest | 

try:
    # Create a new user-roles relationship
    api_instance.users_relationships_roles_create(body)
except ApiException as e:
    print("Exception when calling UserApi->users_relationships_roles_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserRoleRelationshipRequest**](UserRoleRelationshipRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_relationships_roles_destroy**
> users_relationships_roles_destroy()

Delete a user-roles relationship

Remove the user-roles relationship from the system by their ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))

try:
    # Delete a user-roles relationship
    api_instance.users_relationships_roles_destroy()
except ApiException as e:
    print("Exception when calling UserApi->users_relationships_roles_destroy: %s\n" % e)
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

# **users_relationships_roles_partial_update**
> users_relationships_roles_partial_update(body)

Partially update a user-roles relationship

Update the user-roles relationship information without affecting other fields.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
body = swagger_client.PatchedUserRoleRelationshipRequest() # PatchedUserRoleRelationshipRequest | 

try:
    # Partially update a user-roles relationship
    api_instance.users_relationships_roles_partial_update(body)
except ApiException as e:
    print("Exception when calling UserApi->users_relationships_roles_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchedUserRoleRelationshipRequest**](PatchedUserRoleRelationshipRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_retrieve**
> UserResponse users_retrieve(id, fields_users=fields_users, include=include)

Retrieve a user's information

Fetch detailed information about an authenticated user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this user.
fields_users = ['fields_users_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)
include = ['include_example'] # list[str] | include query parameter to allow the client to customize which related resources should be returned. (optional)

try:
    # Retrieve a user's information
    api_response = api_instance.users_retrieve(id, fields_users=fields_users, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->users_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this user. | 
 **fields_users** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 
 **include** | [**list[str]**](str.md)| include query parameter to allow the client to customize which related resources should be returned. | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

