# swagger_client.IntegrationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**integrations_create**](IntegrationApi.md#integrations_create) | **POST** /api/v1/integrations | Create a new integration
[**integrations_destroy**](IntegrationApi.md#integrations_destroy) | **DELETE** /api/v1/integrations/{id} | Delete an integration
[**integrations_list**](IntegrationApi.md#integrations_list) | **GET** /api/v1/integrations | List all integrations
[**integrations_partial_update**](IntegrationApi.md#integrations_partial_update) | **PATCH** /api/v1/integrations/{id} | Partially update an integration
[**integrations_retrieve**](IntegrationApi.md#integrations_retrieve) | **GET** /api/v1/integrations/{id} | Retrieve integration details

# **integrations_create**
> IntegrationCreateResponse integrations_create(body)

Create a new integration

Register a new integration with the system, providing necessary configuration details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.IntegrationApi(swagger_client.ApiClient(configuration))
body = swagger_client.IntegrationCreateRequest() # IntegrationCreateRequest | 

try:
    # Create a new integration
    api_response = api_instance.integrations_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->integrations_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IntegrationCreateRequest**](IntegrationCreateRequest.md)|  | 

### Return type

[**IntegrationCreateResponse**](IntegrationCreateResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integrations_destroy**
> integrations_destroy(id)

Delete an integration

Remove an integration from the system by its ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.IntegrationApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this integration.

try:
    # Delete an integration
    api_instance.integrations_destroy(id)
except ApiException as e:
    print("Exception when calling IntegrationApi->integrations_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this integration. | 

### Return type

void (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integrations_list**
> PaginatedIntegrationList integrations_list(fields_integrations=fields_integrations, filter_inserted_at=filter_inserted_at, filter_inserted_at__date=filter_inserted_at__date, filter_inserted_at__gte=filter_inserted_at__gte, filter_inserted_at__lte=filter_inserted_at__lte, filter_integration_type=filter_integration_type, filter_integration_type__in=filter_integration_type__in, filter_search=filter_search, include=include, page_number=page_number, page_size=page_size, sort=sort)

List all integrations

Retrieve a list of all configured integrations with options for filtering by various criteria.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.IntegrationApi(swagger_client.ApiClient(configuration))
fields_integrations = ['fields_integrations_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)
filter_inserted_at = '2013-10-20' # date |  (optional)
filter_inserted_at__date = '2013-10-20' # date |  (optional)
filter_inserted_at__gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_inserted_at__lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter_integration_type = 'filter_integration_type_example' # str | * `amazon_s3` - Amazon S3 * `saml` - SAML * `aws_security_hub` - AWS Security Hub * `jira` - JIRA * `slack` - Slack (optional)
filter_integration_type__in = ['filter_integration_type__in_example'] # list[str] | Multiple values may be separated by commas.  * `amazon_s3` - Amazon S3 * `saml` - SAML * `aws_security_hub` - AWS Security Hub * `jira` - JIRA * `slack` - Slack (optional)
filter_search = 'filter_search_example' # str | A search term. (optional)
include = ['include_example'] # list[str] | include query parameter to allow the client to customize which related resources should be returned. (optional)
page_number = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
sort = ['sort_example'] # list[str] | [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) (optional)

try:
    # List all integrations
    api_response = api_instance.integrations_list(fields_integrations=fields_integrations, filter_inserted_at=filter_inserted_at, filter_inserted_at__date=filter_inserted_at__date, filter_inserted_at__gte=filter_inserted_at__gte, filter_inserted_at__lte=filter_inserted_at__lte, filter_integration_type=filter_integration_type, filter_integration_type__in=filter_integration_type__in, filter_search=filter_search, include=include, page_number=page_number, page_size=page_size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->integrations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields_integrations** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 
 **filter_inserted_at** | **date**|  | [optional] 
 **filter_inserted_at__date** | **date**|  | [optional] 
 **filter_inserted_at__gte** | **datetime**|  | [optional] 
 **filter_inserted_at__lte** | **datetime**|  | [optional] 
 **filter_integration_type** | **str**| * &#x60;amazon_s3&#x60; - Amazon S3 * &#x60;saml&#x60; - SAML * &#x60;aws_security_hub&#x60; - AWS Security Hub * &#x60;jira&#x60; - JIRA * &#x60;slack&#x60; - Slack | [optional] 
 **filter_integration_type__in** | [**list[str]**](str.md)| Multiple values may be separated by commas.  * &#x60;amazon_s3&#x60; - Amazon S3 * &#x60;saml&#x60; - SAML * &#x60;aws_security_hub&#x60; - AWS Security Hub * &#x60;jira&#x60; - JIRA * &#x60;slack&#x60; - Slack | [optional] 
 **filter_search** | **str**| A search term. | [optional] 
 **include** | [**list[str]**](str.md)| include query parameter to allow the client to customize which related resources should be returned. | [optional] 
 **page_number** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **sort** | [**list[str]**](str.md)| [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) | [optional] 

### Return type

[**PaginatedIntegrationList**](PaginatedIntegrationList.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integrations_partial_update**
> IntegrationUpdateResponse integrations_partial_update(body, id)

Partially update an integration

Modify certain fields of an existing integration without affecting other settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.IntegrationApi(swagger_client.ApiClient(configuration))
body = swagger_client.PatchedIntegrationUpdateRequest() # PatchedIntegrationUpdateRequest | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this integration.

try:
    # Partially update an integration
    api_response = api_instance.integrations_partial_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->integrations_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchedIntegrationUpdateRequest**](PatchedIntegrationUpdateRequest.md)|  | 
 **id** | [**str**](.md)| A UUID string identifying this integration. | 

### Return type

[**IntegrationUpdateResponse**](IntegrationUpdateResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integrations_retrieve**
> IntegrationResponse integrations_retrieve(id, fields_integrations=fields_integrations, include=include)

Retrieve integration details

Fetch detailed information about a specific integration by its ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.IntegrationApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this integration.
fields_integrations = ['fields_integrations_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)
include = ['include_example'] # list[str] | include query parameter to allow the client to customize which related resources should be returned. (optional)

try:
    # Retrieve integration details
    api_response = api_instance.integrations_retrieve(id, fields_integrations=fields_integrations, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->integrations_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this integration. | 
 **fields_integrations** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 
 **include** | [**list[str]**](str.md)| include query parameter to allow the client to customize which related resources should be returned. | [optional] 

### Return type

[**IntegrationResponse**](IntegrationResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

