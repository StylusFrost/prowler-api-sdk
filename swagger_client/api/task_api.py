# coding: utf-8

"""
    Prowler API

    Prowler API specification.  This file is auto-generated.  # noqa: E501

    OpenAPI spec version: 1.6.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class TaskApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def tasks_destroy(self, id, **kwargs):  # noqa: E501
        """Revoke a task  # noqa: E501

        Try to revoke a task using its ID. Only tasks that are not yet in progress can be revoked.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tasks_destroy(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: A UUID string identifying this task. (required)
        :return: OpenApiResponseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.tasks_destroy_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.tasks_destroy_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def tasks_destroy_with_http_info(self, id, **kwargs):  # noqa: E501
        """Revoke a task  # noqa: E501

        Try to revoke a task using its ID. Only tasks that are not yet in progress can be revoked.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tasks_destroy_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: A UUID string identifying this task. (required)
        :return: OpenApiResponseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tasks_destroy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `tasks_destroy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.api+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jwtAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tasks/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OpenApiResponseResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def tasks_list(self, **kwargs):  # noqa: E501
        """List all tasks  # noqa: E501

        Retrieve a list of all tasks with options for filtering by name, state, and other criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tasks_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] fields_tasks: endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter.
        :param str filter_name:
        :param str filter_name__icontains:
        :param str filter_search: A search term.
        :param str filter_state: Current state of the task being run  * `available` - Available * `scheduled` - Scheduled * `executing` - Executing * `completed` - Completed * `failed` - Failed * `cancelled` - Cancelled
        :param int page_number: A page number within the paginated result set.
        :param int page_size: Number of results to return per page.
        :param list[str] sort: [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting)
        :return: PaginatedTaskList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.tasks_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.tasks_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def tasks_list_with_http_info(self, **kwargs):  # noqa: E501
        """List all tasks  # noqa: E501

        Retrieve a list of all tasks with options for filtering by name, state, and other criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tasks_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] fields_tasks: endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter.
        :param str filter_name:
        :param str filter_name__icontains:
        :param str filter_search: A search term.
        :param str filter_state: Current state of the task being run  * `available` - Available * `scheduled` - Scheduled * `executing` - Executing * `completed` - Completed * `failed` - Failed * `cancelled` - Cancelled
        :param int page_number: A page number within the paginated result set.
        :param int page_size: Number of results to return per page.
        :param list[str] sort: [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting)
        :return: PaginatedTaskList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fields_tasks', 'filter_name', 'filter_name__icontains', 'filter_search', 'filter_state', 'page_number', 'page_size', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tasks_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields_tasks' in params:
            query_params.append(('fields[tasks]', params['fields_tasks']))  # noqa: E501
            collection_formats['fields[tasks]'] = 'csv'  # noqa: E501
        if 'filter_name' in params:
            query_params.append(('filter[name]', params['filter_name']))  # noqa: E501
        if 'filter_name__icontains' in params:
            query_params.append(('filter[name__icontains]', params['filter_name__icontains']))  # noqa: E501
        if 'filter_search' in params:
            query_params.append(('filter[search]', params['filter_search']))  # noqa: E501
        if 'filter_state' in params:
            query_params.append(('filter[state]', params['filter_state']))  # noqa: E501
        if 'page_number' in params:
            query_params.append(('page[number]', params['page_number']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page[size]', params['page_size']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.api+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jwtAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tasks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaginatedTaskList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def tasks_retrieve(self, id, **kwargs):  # noqa: E501
        """Retrieve data from a specific task  # noqa: E501

        Fetch detailed information about a specific task by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tasks_retrieve(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: A UUID string identifying this task. (required)
        :param list[str] fields_tasks: endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter.
        :return: TaskResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.tasks_retrieve_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.tasks_retrieve_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def tasks_retrieve_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieve data from a specific task  # noqa: E501

        Fetch detailed information about a specific task by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tasks_retrieve_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: A UUID string identifying this task. (required)
        :param list[str] fields_tasks: endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter.
        :return: TaskResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'fields_tasks']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tasks_retrieve" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `tasks_retrieve`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'fields_tasks' in params:
            query_params.append(('fields[tasks]', params['fields_tasks']))  # noqa: E501
            collection_formats['fields[tasks]'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.api+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jwtAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tasks/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
