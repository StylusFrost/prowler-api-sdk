# swagger_client.TaskApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tasks_destroy**](TaskApi.md#tasks_destroy) | **DELETE** /api/v1/tasks/{id} | Revoke a task
[**tasks_list**](TaskApi.md#tasks_list) | **GET** /api/v1/tasks | List all tasks
[**tasks_retrieve**](TaskApi.md#tasks_retrieve) | **GET** /api/v1/tasks/{id} | Retrieve data from a specific task

# **tasks_destroy**
> OpenApiResponseResponse tasks_destroy(id)

Revoke a task

Try to revoke a task using its ID. Only tasks that are not yet in progress can be revoked.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TaskApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this task.

try:
    # Revoke a task
    api_response = api_instance.tasks_destroy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskApi->tasks_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this task. | 

### Return type

[**OpenApiResponseResponse**](OpenApiResponseResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_list**
> PaginatedTaskList tasks_list(fields_tasks=fields_tasks, filter_name=filter_name, filter_name__icontains=filter_name__icontains, filter_search=filter_search, filter_state=filter_state, page_number=page_number, page_size=page_size, sort=sort)

List all tasks

Retrieve a list of all tasks with options for filtering by name, state, and other criteria.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TaskApi(swagger_client.ApiClient(configuration))
fields_tasks = ['fields_tasks_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)
filter_name = 'filter_name_example' # str |  (optional)
filter_name__icontains = 'filter_name__icontains_example' # str |  (optional)
filter_search = 'filter_search_example' # str | A search term. (optional)
filter_state = 'filter_state_example' # str | Current state of the task being run  * `available` - Available * `scheduled` - Scheduled * `executing` - Executing * `completed` - Completed * `failed` - Failed * `cancelled` - Cancelled (optional)
page_number = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
sort = ['sort_example'] # list[str] | [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) (optional)

try:
    # List all tasks
    api_response = api_instance.tasks_list(fields_tasks=fields_tasks, filter_name=filter_name, filter_name__icontains=filter_name__icontains, filter_search=filter_search, filter_state=filter_state, page_number=page_number, page_size=page_size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskApi->tasks_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields_tasks** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 
 **filter_name** | **str**|  | [optional] 
 **filter_name__icontains** | **str**|  | [optional] 
 **filter_search** | **str**| A search term. | [optional] 
 **filter_state** | **str**| Current state of the task being run  * &#x60;available&#x60; - Available * &#x60;scheduled&#x60; - Scheduled * &#x60;executing&#x60; - Executing * &#x60;completed&#x60; - Completed * &#x60;failed&#x60; - Failed * &#x60;cancelled&#x60; - Cancelled | [optional] 
 **page_number** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **sort** | [**list[str]**](str.md)| [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting) | [optional] 

### Return type

[**PaginatedTaskList**](PaginatedTaskList.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_retrieve**
> TaskResponse tasks_retrieve(id, fields_tasks=fields_tasks)

Retrieve data from a specific task

Fetch detailed information about a specific task by its ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TaskApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this task.
fields_tasks = ['fields_tasks_example'] # list[str] | endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. (optional)

try:
    # Retrieve data from a specific task
    api_response = api_instance.tasks_retrieve(id, fields_tasks=fields_tasks)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskApi->tasks_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this task. | 
 **fields_tasks** | [**list[str]**](str.md)| endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter. | [optional] 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

