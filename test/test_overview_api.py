# coding: utf-8

"""
    Prowler API

    Prowler API specification.  This file is auto-generated.  # noqa: E501

    OpenAPI spec version: 1.6.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.overview_api import OverviewApi  # noqa: E501
from swagger_client.rest import ApiException


class TestOverviewApi(unittest.TestCase):
    """OverviewApi unit test stubs"""

    def setUp(self):
        self.api = OverviewApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_overviews_findings_retrieve(self):
        """Test case for overviews_findings_retrieve

        Get aggregated findings data  # noqa: E501
        """
        pass

    def test_overviews_findings_severity_retrieve(self):
        """Test case for overviews_findings_severity_retrieve

        Get findings data by severity  # noqa: E501
        """
        pass

    def test_overviews_providers_retrieve(self):
        """Test case for overviews_providers_retrieve

        Get aggregated provider data  # noqa: E501
        """
        pass

    def test_overviews_services_retrieve(self):
        """Test case for overviews_services_retrieve

        Get findings data by service  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
