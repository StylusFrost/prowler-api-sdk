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


class ResourceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def resources_list(self, **kwargs):  # noqa: E501
        """List all resources  # noqa: E501

        Retrieve a list of all resources with options for filtering by various criteria. Resources are objects that are discovered by Prowler. They can be anything from a single host to a whole VPC.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resources_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] fields_resources: endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter.
        :param date filter_inserted_at:
        :param datetime filter_inserted_at__gte:
        :param datetime filter_inserted_at__lte:
        :param str filter_name:
        :param str filter_name__icontains:
        :param str filter_provider:
        :param list[str] filter_provider__in: Multiple values may be separated by commas.
        :param str filter_provider_alias:
        :param str filter_provider_alias__icontains:
        :param list[str] filter_provider_alias__in: Multiple values may be separated by commas.
        :param str filter_provider_type: * `aws` - AWS * `azure` - Azure * `gcp` - GCP * `kubernetes` - Kubernetes
        :param list[str] filter_provider_type__in: Multiple values may be separated by commas.  * `aws` - AWS * `azure` - Azure * `gcp` - GCP * `kubernetes` - Kubernetes
        :param str filter_provider_uid:
        :param str filter_provider_uid__icontains:
        :param list[str] filter_provider_uid__in: Multiple values may be separated by commas.
        :param str filter_region:
        :param str filter_region__icontains:
        :param list[str] filter_region__in: Multiple values may be separated by commas.
        :param str filter_search: A search term.
        :param str filter_service:
        :param str filter_service__icontains:
        :param list[str] filter_service__in: Multiple values may be separated by commas.
        :param str filter_tag:
        :param str filter_tag_key:
        :param str filter_tag_value:
        :param str filter_tags:
        :param str filter_type:
        :param str filter_type__icontains:
        :param list[str] filter_type__in: Multiple values may be separated by commas.
        :param str filter_uid:
        :param str filter_uid__icontains:
        :param date filter_updated_at:
        :param datetime filter_updated_at__gte:
        :param datetime filter_updated_at__lte:
        :param list[str] include: include query parameter to allow the client to customize which related resources should be returned.
        :param int page_number: A page number within the paginated result set.
        :param int page_size: Number of results to return per page.
        :param list[str] sort: [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting)
        :return: PaginatedResourceList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.resources_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.resources_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def resources_list_with_http_info(self, **kwargs):  # noqa: E501
        """List all resources  # noqa: E501

        Retrieve a list of all resources with options for filtering by various criteria. Resources are objects that are discovered by Prowler. They can be anything from a single host to a whole VPC.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resources_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] fields_resources: endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter.
        :param date filter_inserted_at:
        :param datetime filter_inserted_at__gte:
        :param datetime filter_inserted_at__lte:
        :param str filter_name:
        :param str filter_name__icontains:
        :param str filter_provider:
        :param list[str] filter_provider__in: Multiple values may be separated by commas.
        :param str filter_provider_alias:
        :param str filter_provider_alias__icontains:
        :param list[str] filter_provider_alias__in: Multiple values may be separated by commas.
        :param str filter_provider_type: * `aws` - AWS * `azure` - Azure * `gcp` - GCP * `kubernetes` - Kubernetes
        :param list[str] filter_provider_type__in: Multiple values may be separated by commas.  * `aws` - AWS * `azure` - Azure * `gcp` - GCP * `kubernetes` - Kubernetes
        :param str filter_provider_uid:
        :param str filter_provider_uid__icontains:
        :param list[str] filter_provider_uid__in: Multiple values may be separated by commas.
        :param str filter_region:
        :param str filter_region__icontains:
        :param list[str] filter_region__in: Multiple values may be separated by commas.
        :param str filter_search: A search term.
        :param str filter_service:
        :param str filter_service__icontains:
        :param list[str] filter_service__in: Multiple values may be separated by commas.
        :param str filter_tag:
        :param str filter_tag_key:
        :param str filter_tag_value:
        :param str filter_tags:
        :param str filter_type:
        :param str filter_type__icontains:
        :param list[str] filter_type__in: Multiple values may be separated by commas.
        :param str filter_uid:
        :param str filter_uid__icontains:
        :param date filter_updated_at:
        :param datetime filter_updated_at__gte:
        :param datetime filter_updated_at__lte:
        :param list[str] include: include query parameter to allow the client to customize which related resources should be returned.
        :param int page_number: A page number within the paginated result set.
        :param int page_size: Number of results to return per page.
        :param list[str] sort: [list of fields to sort by](https://jsonapi.org/format/#fetching-sorting)
        :return: PaginatedResourceList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fields_resources', 'filter_inserted_at', 'filter_inserted_at__gte', 'filter_inserted_at__lte', 'filter_name', 'filter_name__icontains', 'filter_provider', 'filter_provider__in', 'filter_provider_alias', 'filter_provider_alias__icontains', 'filter_provider_alias__in', 'filter_provider_type', 'filter_provider_type__in', 'filter_provider_uid', 'filter_provider_uid__icontains', 'filter_provider_uid__in', 'filter_region', 'filter_region__icontains', 'filter_region__in', 'filter_search', 'filter_service', 'filter_service__icontains', 'filter_service__in', 'filter_tag', 'filter_tag_key', 'filter_tag_value', 'filter_tags', 'filter_type', 'filter_type__icontains', 'filter_type__in', 'filter_uid', 'filter_uid__icontains', 'filter_updated_at', 'filter_updated_at__gte', 'filter_updated_at__lte', 'include', 'page_number', 'page_size', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resources_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields_resources' in params:
            query_params.append(('fields[resources]', params['fields_resources']))  # noqa: E501
            collection_formats['fields[resources]'] = 'csv'  # noqa: E501
        if 'filter_inserted_at' in params:
            query_params.append(('filter[inserted_at]', params['filter_inserted_at']))  # noqa: E501
        if 'filter_inserted_at__gte' in params:
            query_params.append(('filter[inserted_at__gte]', params['filter_inserted_at__gte']))  # noqa: E501
        if 'filter_inserted_at__lte' in params:
            query_params.append(('filter[inserted_at__lte]', params['filter_inserted_at__lte']))  # noqa: E501
        if 'filter_name' in params:
            query_params.append(('filter[name]', params['filter_name']))  # noqa: E501
        if 'filter_name__icontains' in params:
            query_params.append(('filter[name__icontains]', params['filter_name__icontains']))  # noqa: E501
        if 'filter_provider' in params:
            query_params.append(('filter[provider]', params['filter_provider']))  # noqa: E501
        if 'filter_provider__in' in params:
            query_params.append(('filter[provider__in]', params['filter_provider__in']))  # noqa: E501
            collection_formats['filter[provider__in]'] = 'csv'  # noqa: E501
        if 'filter_provider_alias' in params:
            query_params.append(('filter[provider_alias]', params['filter_provider_alias']))  # noqa: E501
        if 'filter_provider_alias__icontains' in params:
            query_params.append(('filter[provider_alias__icontains]', params['filter_provider_alias__icontains']))  # noqa: E501
        if 'filter_provider_alias__in' in params:
            query_params.append(('filter[provider_alias__in]', params['filter_provider_alias__in']))  # noqa: E501
            collection_formats['filter[provider_alias__in]'] = 'csv'  # noqa: E501
        if 'filter_provider_type' in params:
            query_params.append(('filter[provider_type]', params['filter_provider_type']))  # noqa: E501
        if 'filter_provider_type__in' in params:
            query_params.append(('filter[provider_type__in]', params['filter_provider_type__in']))  # noqa: E501
            collection_formats['filter[provider_type__in]'] = 'csv'  # noqa: E501
        if 'filter_provider_uid' in params:
            query_params.append(('filter[provider_uid]', params['filter_provider_uid']))  # noqa: E501
        if 'filter_provider_uid__icontains' in params:
            query_params.append(('filter[provider_uid__icontains]', params['filter_provider_uid__icontains']))  # noqa: E501
        if 'filter_provider_uid__in' in params:
            query_params.append(('filter[provider_uid__in]', params['filter_provider_uid__in']))  # noqa: E501
            collection_formats['filter[provider_uid__in]'] = 'csv'  # noqa: E501
        if 'filter_region' in params:
            query_params.append(('filter[region]', params['filter_region']))  # noqa: E501
        if 'filter_region__icontains' in params:
            query_params.append(('filter[region__icontains]', params['filter_region__icontains']))  # noqa: E501
        if 'filter_region__in' in params:
            query_params.append(('filter[region__in]', params['filter_region__in']))  # noqa: E501
            collection_formats['filter[region__in]'] = 'csv'  # noqa: E501
        if 'filter_search' in params:
            query_params.append(('filter[search]', params['filter_search']))  # noqa: E501
        if 'filter_service' in params:
            query_params.append(('filter[service]', params['filter_service']))  # noqa: E501
        if 'filter_service__icontains' in params:
            query_params.append(('filter[service__icontains]', params['filter_service__icontains']))  # noqa: E501
        if 'filter_service__in' in params:
            query_params.append(('filter[service__in]', params['filter_service__in']))  # noqa: E501
            collection_formats['filter[service__in]'] = 'csv'  # noqa: E501
        if 'filter_tag' in params:
            query_params.append(('filter[tag]', params['filter_tag']))  # noqa: E501
        if 'filter_tag_key' in params:
            query_params.append(('filter[tag_key]', params['filter_tag_key']))  # noqa: E501
        if 'filter_tag_value' in params:
            query_params.append(('filter[tag_value]', params['filter_tag_value']))  # noqa: E501
        if 'filter_tags' in params:
            query_params.append(('filter[tags]', params['filter_tags']))  # noqa: E501
        if 'filter_type' in params:
            query_params.append(('filter[type]', params['filter_type']))  # noqa: E501
        if 'filter_type__icontains' in params:
            query_params.append(('filter[type__icontains]', params['filter_type__icontains']))  # noqa: E501
        if 'filter_type__in' in params:
            query_params.append(('filter[type__in]', params['filter_type__in']))  # noqa: E501
            collection_formats['filter[type__in]'] = 'csv'  # noqa: E501
        if 'filter_uid' in params:
            query_params.append(('filter[uid]', params['filter_uid']))  # noqa: E501
        if 'filter_uid__icontains' in params:
            query_params.append(('filter[uid__icontains]', params['filter_uid__icontains']))  # noqa: E501
        if 'filter_updated_at' in params:
            query_params.append(('filter[updated_at]', params['filter_updated_at']))  # noqa: E501
        if 'filter_updated_at__gte' in params:
            query_params.append(('filter[updated_at__gte]', params['filter_updated_at__gte']))  # noqa: E501
        if 'filter_updated_at__lte' in params:
            query_params.append(('filter[updated_at__lte]', params['filter_updated_at__lte']))  # noqa: E501
        if 'include' in params:
            query_params.append(('include', params['include']))  # noqa: E501
            collection_formats['include'] = 'csv'  # noqa: E501
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
            '/api/v1/resources', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaginatedResourceList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resources_retrieve(self, id, **kwargs):  # noqa: E501
        """Retrieve data for a resource  # noqa: E501

        Fetch detailed information about a specific resource by their ID. A Resource is an object that is discovered by Prowler. It can be anything from a single host to a whole VPC.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resources_retrieve(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: A UUID string identifying this resource. (required)
        :param list[str] fields_resources: endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter.
        :param list[str] include: include query parameter to allow the client to customize which related resources should be returned.
        :return: ResourceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.resources_retrieve_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.resources_retrieve_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def resources_retrieve_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieve data for a resource  # noqa: E501

        Fetch detailed information about a specific resource by their ID. A Resource is an object that is discovered by Prowler. It can be anything from a single host to a whole VPC.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resources_retrieve_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: A UUID string identifying this resource. (required)
        :param list[str] fields_resources: endpoint return only specific fields in the response on a per-type basis by including a fields[TYPE] query parameter.
        :param list[str] include: include query parameter to allow the client to customize which related resources should be returned.
        :return: ResourceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'fields_resources', 'include']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resources_retrieve" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `resources_retrieve`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'fields_resources' in params:
            query_params.append(('fields[resources]', params['fields_resources']))  # noqa: E501
            collection_formats['fields[resources]'] = 'csv'  # noqa: E501
        if 'include' in params:
            query_params.append(('include', params['include']))  # noqa: E501
            collection_formats['include'] = 'csv'  # noqa: E501

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
            '/api/v1/resources/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourceResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
