# swagger_client.ProviderApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**providers_connection_create**](ProviderApi.md#providers_connection_create) | **POST** /api/v1/providers/{id}/connection | Check connection
[**providers_create**](ProviderApi.md#providers_create) | **POST** /api/v1/providers | Create a new provider
[**providers_destroy**](ProviderApi.md#providers_destroy) | **DELETE** /api/v1/providers/{id} | Delete a provider
[**providers_list**](ProviderApi.md#providers_list) | **GET** /api/v1/providers | List all providers
[**providers_partial_update**](ProviderApi.md#providers_partial_update) | **PATCH** /api/v1/providers/{id} | Partially update a provider
[**providers_retrieve**](ProviderApi.md#providers_retrieve) | **GET** /api/v1/providers/{id} | Retrieve data from a provider
[**providers_secrets_create**](ProviderApi.md#providers_secrets_create) | **POST** /api/v1/providers/secrets | Create a new secret
[**providers_secrets_destroy**](ProviderApi.md#providers_secrets_destroy) | **DELETE** /api/v1/providers/secrets/{id} | Delete a secret
[**providers_secrets_list**](ProviderApi.md#providers_secrets_list) | **GET** /api/v1/providers/secrets | List all secrets
[**providers_secrets_partial_update**](ProviderApi.md#providers_secrets_partial_update) | **PATCH** /api/v1/providers/secrets/{id} | Partially update a secret
[**providers_secrets_retrieve**](ProviderApi.md#providers_secrets_retrieve) | **GET** /api/v1/providers/secrets/{id} | Retrieve data from a secret

# **providers_connection_create**
> OpenApiResponseResponse providers_connection_create(id)

Check connection

Try to verify connection. For instance, Role & Credentials are set correctly

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProviderApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this provider.

try:
    # Check connection
    api_response = api_instance.providers_connection_create(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->providers_connection_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this provider. | 

### Return type

[**OpenApiResponseResponse**](OpenApiResponseResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_create**
> ProviderCreateResponse providers_create(body)

Create a new provider

Add a new provider to the system by providing the required provider details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProviderApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProviderCreateRequest() # ProviderCreateRequest | 

try:
    # Create a new provider
    api_response = api_instance.providers_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->providers_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProviderCreateRequest**](ProviderCreateRequest.md)|  | 

### Return type

[**ProviderCreateResponse**](ProviderCreateResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_destroy**
> OpenApiResponseResponse providers_destroy(id)

Delete a provider

Remove a provider from the system by their ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProviderApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this provider.

try:
    # Delete a provider
    api_response = api_instance.providers_destroy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->providers_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this provider. | 

### Return type

[**OpenApiResponseResponse**](OpenApiResponseResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_list**
> PaginatedProviderList providers_list(fields_providers=fields_providers, filter_alias=filter_alias, filter_alias__icontains=filter_alias__icontains, filter_alias__in=filter_alias__in, filter_connected=filter_connected, filter_id=filter_id, filter_id__in=filter_id__in, filter_inserted_at=filter_inserted_at, filter_inserted_at__gte=filter_inserted_at__gte, filter_inserted_at__lte=filter_inserted_at__lte, filter_provider=filter_provider, filter_provider__in=filter_provider__in, filter_search=filter_search, filter_uid=filter_uid, filter_uid__icontains=filter_uid__icontains, filter_uid__in=filter_uid__in, filter_updated_at=filter_updated_at, filter_updated_at__gte=filter_updated_at__gte, filter_updated_at__lte=filter_updated_at__lte, include=include, page_number=page_number, page_size=page_size, sort=sort)

List all providers

Retrieve a list of all providers with options for filtering by various criteria.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProviderApi(swagger_client.ApiClient(configuration))
fields_providers = ['fields_providers_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)
filter_alias = 'filter_alias_example' # str |  (optional)
filter_alias__icontains = 'filter_alias__icontains_example' # str |  (optional)
filter_alias__in = ['filter_alias__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_connected = true # bool |  (optional)
filter_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
filter_id__in = ['filter_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_inserted_at = '2013-10-20' # date |  (optional)
filter_inserted_at__gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_inserted_at__lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_provider = 'filter_provider_example' # str | * `aws` - AWS * `azure` - Azure * `gcp` - GCP * `kubernetes` - Kubernetes (optional)
filter_provider__in = ['filter_provider__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_search = 'filter_search_example' # str | A search term. (optional)
filter_uid = 'filter_uid_example' # str |  (optional)
filter_uid__icontains = 'filter_uid__icontains_example' # str |  (optional)
filter_uid__in = ['filter_uid__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
filter_updated_at = '2013-10-20' # date |  (optional)
filter_updated_at__gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_updated_at__lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
include = ['include_example'] # list[str] | include query parameter to allow the client to customize which related resources should be returned. (optional)
page_number = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
sort = ['sort_example'] # list[str] | [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) (optional)

try:
    # List all providers
    api_response = api_instance.providers_list(fields_providers=fields_providers, filter_alias=filter_alias, filter_alias__icontains=filter_alias__icontains, filter_alias__in=filter_alias__in, filter_connected=filter_connected, filter_id=filter_id, filter_id__in=filter_id__in, filter_inserted_at=filter_inserted_at, filter_inserted_at__gte=filter_inserted_at__gte, filter_inserted_at__lte=filter_inserted_at__lte, filter_provider=filter_provider, filter_provider__in=filter_provider__in, filter_search=filter_search, filter_uid=filter_uid, filter_uid__icontains=filter_uid__icontains, filter_uid__in=filter_uid__in, filter_updated_at=filter_updated_at, filter_updated_at__gte=filter_updated_at__gte, filter_updated_at__lte=filter_updated_at__lte, include=include, page_number=page_number, page_size=page_size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->providers_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields_providers** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 
 **filter_alias** | **str**|  | [optional] 
 **filter_alias__icontains** | **str**|  | [optional] 
 **filter_alias__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_connected** | **bool**|  | [optional] 
 **filter_id** | [**str**](.md)|  | [optional] 
 **filter_id__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_inserted_at** | **date**|  | [optional] 
 **filter_inserted_at__gte** | **datetime**|  | [optional] 
 **filter_inserted_at__lte** | **datetime**|  | [optional] 
 **filter_provider** | **str**| * &#x60;aws&#x60; - AWS * &#x60;azure&#x60; - Azure * &#x60;gcp&#x60; - GCP * &#x60;kubernetes&#x60; - Kubernetes | [optional] 
 **filter_provider__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_search** | **str**| A search term. | [optional] 
 **filter_uid** | **str**|  | [optional] 
 **filter_uid__icontains** | **str**|  | [optional] 
 **filter_uid__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **filter_updated_at** | **date**|  | [optional] 
 **filter_updated_at__gte** | **datetime**|  | [optional] 
 **filter_updated_at__lte** | **datetime**|  | [optional] 
 **include** | [**list[str]**](str.md)| include query parameter to allow the client to customize which related resources should be returned. | [optional] 
 **page_number** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **sort** | [**list[str]**](str.md)| [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) | [optional] 

### Return type

[**PaginatedProviderList**](PaginatedProviderList.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_partial_update**
> SerializerMetaclassResponse providers_partial_update(body, id)

Partially update a provider

Update certain fields of an existing provider's information without affecting other fields.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProviderApi(swagger_client.ApiClient(configuration))
body = swagger_client.PatchedProviderUpdateRequest() # PatchedProviderUpdateRequest | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this provider.

try:
    # Partially update a provider
    api_response = api_instance.providers_partial_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->providers_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchedProviderUpdateRequest**](PatchedProviderUpdateRequest.md)|  | 
 **id** | [**str**](.md)| A UUID string identifying this provider. | 

### Return type

[**SerializerMetaclassResponse**](SerializerMetaclassResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_retrieve**
> ProviderResponse providers_retrieve(id, fields_providers=fields_providers, include=include)

Retrieve data from a provider

Fetch detailed information about a specific provider by their ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProviderApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this provider.
fields_providers = ['fields_providers_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)
include = ['include_example'] # list[str] | include query parameter to allow the client to customize which related resources should be returned. (optional)

try:
    # Retrieve data from a provider
    api_response = api_instance.providers_retrieve(id, fields_providers=fields_providers, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->providers_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this provider. | 
 **fields_providers** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 
 **include** | [**list[str]**](str.md)| include query parameter to allow the client to customize which related resources should be returned. | [optional] 

### Return type

[**ProviderResponse**](ProviderResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_secrets_create**
> ProviderSecretCreateResponse providers_secrets_create(body)

Create a new secret

Add a new secret to the system by providing the required secret details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProviderApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProviderSecretCreateRequest() # ProviderSecretCreateRequest | 

try:
    # Create a new secret
    api_response = api_instance.providers_secrets_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->providers_secrets_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProviderSecretCreateRequest**](ProviderSecretCreateRequest.md)|  | 

### Return type

[**ProviderSecretCreateResponse**](ProviderSecretCreateResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_secrets_destroy**
> providers_secrets_destroy(id)

Delete a secret

Remove a secret from the system by their ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProviderApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Delete a secret
    api_instance.providers_secrets_destroy(id)
except ApiException as e:
    print("Exception when calling ProviderApi->providers_secrets_destroy: %s\n" % e)
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

# **providers_secrets_list**
> PaginatedProviderSecretList providers_secrets_list(fields_provider_secrets=fields_provider_secrets, filter_inserted_at=filter_inserted_at, filter_name=filter_name, filter_name__icontains=filter_name__icontains, filter_provider=filter_provider, filter_search=filter_search, filter_updated_at=filter_updated_at, page_number=page_number, page_size=page_size, sort=sort)

List all secrets

Retrieve a list of all secrets with options for filtering by various criteria.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProviderApi(swagger_client.ApiClient(configuration))
fields_provider_secrets = ['fields_provider_secrets_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)
filter_inserted_at = '2013-10-20' # date |  (optional)
filter_name = 'filter_name_example' # str |  (optional)
filter_name__icontains = 'filter_name__icontains_example' # str |  (optional)
filter_provider = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
filter_search = 'filter_search_example' # str | A search term. (optional)
filter_updated_at = '2013-10-20' # date |  (optional)
page_number = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
sort = ['sort_example'] # list[str] | [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) (optional)

try:
    # List all secrets
    api_response = api_instance.providers_secrets_list(fields_provider_secrets=fields_provider_secrets, filter_inserted_at=filter_inserted_at, filter_name=filter_name, filter_name__icontains=filter_name__icontains, filter_provider=filter_provider, filter_search=filter_search, filter_updated_at=filter_updated_at, page_number=page_number, page_size=page_size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->providers_secrets_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields_provider_secrets** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 
 **filter_inserted_at** | **date**|  | [optional] 
 **filter_name** | **str**|  | [optional] 
 **filter_name__icontains** | **str**|  | [optional] 
 **filter_provider** | [**str**](.md)|  | [optional] 
 **filter_search** | **str**| A search term. | [optional] 
 **filter_updated_at** | **date**|  | [optional] 
 **page_number** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **sort** | [**list[str]**](str.md)| [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) | [optional] 

### Return type

[**PaginatedProviderSecretList**](PaginatedProviderSecretList.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_secrets_partial_update**
> ProviderSecretUpdateResponse providers_secrets_partial_update(body, id)

Partially update a secret

Update certain fields of an existing secret's information without affecting other fields.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProviderApi(swagger_client.ApiClient(configuration))
body = swagger_client.PatchedProviderSecretUpdateRequest() # PatchedProviderSecretUpdateRequest | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Partially update a secret
    api_response = api_instance.providers_secrets_partial_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->providers_secrets_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchedProviderSecretUpdateRequest**](PatchedProviderSecretUpdateRequest.md)|  | 
 **id** | [**str**](.md)|  | 

### Return type

[**ProviderSecretUpdateResponse**](ProviderSecretUpdateResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_secrets_retrieve**
> ProviderSecretResponse providers_secrets_retrieve(id, fields_provider_secrets=fields_provider_secrets)

Retrieve data from a secret

Fetch detailed information about a specific secret by their ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProviderApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
fields_provider_secrets = ['fields_provider_secrets_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)

try:
    # Retrieve data from a secret
    api_response = api_instance.providers_secrets_retrieve(id, fields_provider_secrets=fields_provider_secrets)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->providers_secrets_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **fields_provider_secrets** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 

### Return type

[**ProviderSecretResponse**](ProviderSecretResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

