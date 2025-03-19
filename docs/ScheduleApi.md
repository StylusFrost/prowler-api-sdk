# swagger_client.ScheduleApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schedules_daily_create**](ScheduleApi.md#schedules_daily_create) | **POST** /api/v1/schedules/daily | Create a daily schedule scan for a given provider

# **schedules_daily_create**
> OpenApiResponseResponse schedules_daily_create(body)

Create a daily schedule scan for a given provider

Schedules a daily scan for the specified provider. This endpoint creates a periodic task that will execute a scan every 24 hours.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ScheduleApi(swagger_client.ApiClient(configuration))
body = swagger_client.ScheduleDailyCreateRequest() # ScheduleDailyCreateRequest | 

try:
    # Create a daily schedule scan for a given provider
    api_response = api_instance.schedules_daily_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleApi->schedules_daily_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScheduleDailyCreateRequest**](ScheduleDailyCreateRequest.md)|  | 

### Return type

[**OpenApiResponseResponse**](OpenApiResponseResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

