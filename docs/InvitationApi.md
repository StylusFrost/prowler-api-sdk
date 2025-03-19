# swagger_client.InvitationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invitations_accept_create**](InvitationApi.md#invitations_accept_create) | **POST** /api/v1/invitations/accept | Accept an invitation
[**tenants_invitations_create**](InvitationApi.md#tenants_invitations_create) | **POST** /api/v1/tenants/invitations | Invite a user to a tenant
[**tenants_invitations_destroy**](InvitationApi.md#tenants_invitations_destroy) | **DELETE** /api/v1/tenants/invitations/{id} | Revoke a tenant invitation
[**tenants_invitations_list**](InvitationApi.md#tenants_invitations_list) | **GET** /api/v1/tenants/invitations | List all invitations
[**tenants_invitations_partial_update**](InvitationApi.md#tenants_invitations_partial_update) | **PATCH** /api/v1/tenants/invitations/{id} | Partially update a tenant invitation
[**tenants_invitations_retrieve**](InvitationApi.md#tenants_invitations_retrieve) | **GET** /api/v1/tenants/invitations/{id} | Retrieve data from a tenant invitation

# **invitations_accept_create**
> OpenApiResponseResponse invitations_accept_create(body)

Accept an invitation

Accept an invitation to an existing tenant. This invitation cannot be expired and the emails must match.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InvitationApi(swagger_client.ApiClient(configuration))
body = swagger_client.InvitationAcceptRequest() # InvitationAcceptRequest | 

try:
    # Accept an invitation
    api_response = api_instance.invitations_accept_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationApi->invitations_accept_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InvitationAcceptRequest**](InvitationAcceptRequest.md)|  | 

### Return type

[**OpenApiResponseResponse**](OpenApiResponseResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_invitations_create**
> InvitationCreateResponse tenants_invitations_create(body)

Invite a user to a tenant

Add a new tenant invitation to the system by providing the required invitation details. The invited user will have to accept the invitations or create an account using the given code.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InvitationApi(swagger_client.ApiClient(configuration))
body = swagger_client.InvitationCreateRequest() # InvitationCreateRequest | 

try:
    # Invite a user to a tenant
    api_response = api_instance.tenants_invitations_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationApi->tenants_invitations_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InvitationCreateRequest**](InvitationCreateRequest.md)|  | 

### Return type

[**InvitationCreateResponse**](InvitationCreateResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_invitations_destroy**
> tenants_invitations_destroy(id)

Revoke a tenant invitation

Revoke a tenant invitation from the system by their ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InvitationApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Revoke a tenant invitation
    api_instance.tenants_invitations_destroy(id)
except ApiException as e:
    print("Exception when calling InvitationApi->tenants_invitations_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_invitations_list**
> PaginatedInvitationList tenants_invitations_list(fields_invitations=fields_invitations, filter_email=filter_email, filter_email__icontains=filter_email__icontains, filter_expires_at=filter_expires_at, filter_expires_at__date=filter_expires_at__date, filter_expires_at__gte=filter_expires_at__gte, filter_expires_at__lte=filter_expires_at__lte, filter_inserted_at=filter_inserted_at, filter_inserted_at__date=filter_inserted_at__date, filter_inserted_at__gte=filter_inserted_at__gte, filter_inserted_at__lte=filter_inserted_at__lte, filter_inviter=filter_inviter, filter_search=filter_search, filter_state=filter_state, filter_state__in=filter_state__in, filter_updated_at=filter_updated_at, filter_updated_at__date=filter_updated_at__date, filter_updated_at__gte=filter_updated_at__gte, filter_updated_at__lte=filter_updated_at__lte, page_number=page_number, page_size=page_size, sort=sort)

List all invitations

Retrieve a list of all tenant invitations with options for filtering by various criteria.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InvitationApi(swagger_client.ApiClient(configuration))
fields_invitations = ['fields_invitations_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)
filter_email = 'filter_email_example' # str |  (optional)
filter_email__icontains = 'filter_email__icontains_example' # str |  (optional)
filter_expires_at = '2013-10-20' # date |  (optional)
filter_expires_at__date = '2013-10-20' # date |  (optional)
filter_expires_at__gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_expires_at__lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_inserted_at = '2013-10-20' # date |  (optional)
filter_inserted_at__date = '2013-10-20' # date |  (optional)
filter_inserted_at__gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_inserted_at__lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_inviter = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
filter_search = 'filter_search_example' # str | A search term. (optional)
filter_state = 'filter_state_example' # str | * `pending` - Invitation is pending * `accepted` - Invitation was accepted by a user * `expired` - Invitation expired after the configured time * `revoked` - Invitation was revoked by a user (optional)
filter_state__in = ['filter_state__in_example'] # list[str] | Multiple values may be separated by commas.  * `pending` - Invitation is pending * `accepted` - Invitation was accepted by a user * `expired` - Invitation expired after the configured time * `revoked` - Invitation was revoked by a user (optional)
filter_updated_at = '2013-10-20' # date |  (optional)
filter_updated_at__date = '2013-10-20' # date |  (optional)
filter_updated_at__gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_updated_at__lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
page_number = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
sort = ['sort_example'] # list[str] | [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) (optional)

try:
    # List all invitations
    api_response = api_instance.tenants_invitations_list(fields_invitations=fields_invitations, filter_email=filter_email, filter_email__icontains=filter_email__icontains, filter_expires_at=filter_expires_at, filter_expires_at__date=filter_expires_at__date, filter_expires_at__gte=filter_expires_at__gte, filter_expires_at__lte=filter_expires_at__lte, filter_inserted_at=filter_inserted_at, filter_inserted_at__date=filter_inserted_at__date, filter_inserted_at__gte=filter_inserted_at__gte, filter_inserted_at__lte=filter_inserted_at__lte, filter_inviter=filter_inviter, filter_search=filter_search, filter_state=filter_state, filter_state__in=filter_state__in, filter_updated_at=filter_updated_at, filter_updated_at__date=filter_updated_at__date, filter_updated_at__gte=filter_updated_at__gte, filter_updated_at__lte=filter_updated_at__lte, page_number=page_number, page_size=page_size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationApi->tenants_invitations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields_invitations** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 
 **filter_email** | **str**|  | [optional] 
 **filter_email__icontains** | **str**|  | [optional] 
 **filter_expires_at** | **date**|  | [optional] 
 **filter_expires_at__date** | **date**|  | [optional] 
 **filter_expires_at__gte** | **datetime**|  | [optional] 
 **filter_expires_at__lte** | **datetime**|  | [optional] 
 **filter_inserted_at** | **date**|  | [optional] 
 **filter_inserted_at__date** | **date**|  | [optional] 
 **filter_inserted_at__gte** | **datetime**|  | [optional] 
 **filter_inserted_at__lte** | **datetime**|  | [optional] 
 **filter_inviter** | [**str**](.md)|  | [optional] 
 **filter_search** | **str**| A search term. | [optional] 
 **filter_state** | **str**| * &#x60;pending&#x60; - Invitation is pending * &#x60;accepted&#x60; - Invitation was accepted by a user * &#x60;expired&#x60; - Invitation expired after the configured time * &#x60;revoked&#x60; - Invitation was revoked by a user | [optional] 
 **filter_state__in** | [**list[str]**](str.md)| Multiple values may be separated by commas.  * &#x60;pending&#x60; - Invitation is pending * &#x60;accepted&#x60; - Invitation was accepted by a user * &#x60;expired&#x60; - Invitation expired after the configured time * &#x60;revoked&#x60; - Invitation was revoked by a user | [optional] 
 **filter_updated_at** | **date**|  | [optional] 
 **filter_updated_at__date** | **date**|  | [optional] 
 **filter_updated_at__gte** | **datetime**|  | [optional] 
 **filter_updated_at__lte** | **datetime**|  | [optional] 
 **page_number** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **sort** | [**list[str]**](str.md)| [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) | [optional] 

### Return type

[**PaginatedInvitationList**](PaginatedInvitationList.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_invitations_partial_update**
> InvitationUpdateResponse tenants_invitations_partial_update(body, id)

Partially update a tenant invitation

Update certain fields of an existing tenant invitation's information without affecting other fields.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InvitationApi(swagger_client.ApiClient(configuration))
body = swagger_client.PatchedInvitationUpdateRequest() # PatchedInvitationUpdateRequest | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Partially update a tenant invitation
    api_response = api_instance.tenants_invitations_partial_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationApi->tenants_invitations_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchedInvitationUpdateRequest**](PatchedInvitationUpdateRequest.md)|  | 
 **id** | [**str**](.md)|  | 

### Return type

[**InvitationUpdateResponse**](InvitationUpdateResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_invitations_retrieve**
> InvitationResponse tenants_invitations_retrieve(id, fields_invitations=fields_invitations)

Retrieve data from a tenant invitation

Fetch detailed information about a specific invitation by its ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InvitationApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
fields_invitations = ['fields_invitations_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)

try:
    # Retrieve data from a tenant invitation
    api_response = api_instance.tenants_invitations_retrieve(id, fields_invitations=fields_invitations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationApi->tenants_invitations_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **fields_invitations** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 

### Return type

[**InvitationResponse**](InvitationResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

