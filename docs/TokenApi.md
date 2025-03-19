# swagger_client.TokenApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tokens_create**](TokenApi.md#tokens_create) | **POST** /api/v1/tokens | Obtain a token
[**tokens_refresh_create**](TokenApi.md#tokens_refresh_create) | **POST** /api/v1/tokens/refresh | Refresh a token
[**tokens_switch_create**](TokenApi.md#tokens_switch_create) | **POST** /api/v1/tokens/switch | Switch tenant using a valid tenant ID

# **tokens_create**
> TokenResponse tokens_create(body)

Obtain a token

Obtain a token by providing valid credentials and an optional tenant ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TokenApi(swagger_client.ApiClient(configuration))
body = swagger_client.TokenRequest() # TokenRequest | 

try:
    # Obtain a token
    api_response = api_instance.tokens_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->tokens_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokenRequest**](TokenRequest.md)|  | 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tokens_refresh_create**
> TokenRefreshResponse tokens_refresh_create(body)

Refresh a token

Refresh an access token by providing a valid refresh token. Former refresh tokens are invalidated when a new one is issued.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TokenApi(swagger_client.ApiClient(configuration))
body = swagger_client.TokenRefreshRequest() # TokenRefreshRequest | 

try:
    # Refresh a token
    api_response = api_instance.tokens_refresh_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->tokens_refresh_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokenRefreshRequest**](TokenRefreshRequest.md)|  | 

### Return type

[**TokenRefreshResponse**](TokenRefreshResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tokens_switch_create**
> TokenSwitchTenantResponse tokens_switch_create(body)

Switch tenant using a valid tenant ID

Switch tenant by providing a valid tenant ID. The authenticated user must belong to the tenant.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TokenApi(swagger_client.ApiClient(configuration))
body = swagger_client.TokenSwitchTenantRequest() # TokenSwitchTenantRequest | 

try:
    # Switch tenant using a valid tenant ID
    api_response = api_instance.tokens_switch_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->tokens_switch_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokenSwitchTenantRequest**](TokenSwitchTenantRequest.md)|  | 

### Return type

[**TokenSwitchTenantResponse**](TokenSwitchTenantResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

