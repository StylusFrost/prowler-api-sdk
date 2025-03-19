# coding: utf-8

"""
    Prowler API

    Prowler API specification.  This file is auto-generated.  # noqa: E501

    OpenAPI spec version: 1.6.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class IntegrationCreateAttributes(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'inserted_at': 'datetime',
        'updated_at': 'datetime',
        'enabled': 'bool',
        'connected': 'bool',
        'connection_last_checked_at': 'datetime',
        'integration_type': 'str',
        'configuration': 'OneOfIntegrationCreateAttributesConfiguration',
        'credentials': 'OneOfIntegrationCreateAttributesCredentials'
    }

    attribute_map = {
        'inserted_at': 'inserted_at',
        'updated_at': 'updated_at',
        'enabled': 'enabled',
        'connected': 'connected',
        'connection_last_checked_at': 'connection_last_checked_at',
        'integration_type': 'integration_type',
        'configuration': 'configuration',
        'credentials': 'credentials'
    }

    def __init__(self, inserted_at=None, updated_at=None, enabled=None, connected=None, connection_last_checked_at=None, integration_type=None, configuration=None, credentials=None):  # noqa: E501
        """IntegrationCreateAttributes - a model defined in Swagger"""  # noqa: E501
        self._inserted_at = None
        self._updated_at = None
        self._enabled = None
        self._connected = None
        self._connection_last_checked_at = None
        self._integration_type = None
        self._configuration = None
        self._credentials = None
        self.discriminator = None
        if inserted_at is not None:
            self.inserted_at = inserted_at
        if updated_at is not None:
            self.updated_at = updated_at
        if enabled is not None:
            self.enabled = enabled
        if connected is not None:
            self.connected = connected
        if connection_last_checked_at is not None:
            self.connection_last_checked_at = connection_last_checked_at
        self.integration_type = integration_type
        self.configuration = configuration
        self.credentials = credentials

    @property
    def inserted_at(self):
        """Gets the inserted_at of this IntegrationCreateAttributes.  # noqa: E501


        :return: The inserted_at of this IntegrationCreateAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._inserted_at

    @inserted_at.setter
    def inserted_at(self, inserted_at):
        """Sets the inserted_at of this IntegrationCreateAttributes.


        :param inserted_at: The inserted_at of this IntegrationCreateAttributes.  # noqa: E501
        :type: datetime
        """

        self._inserted_at = inserted_at

    @property
    def updated_at(self):
        """Gets the updated_at of this IntegrationCreateAttributes.  # noqa: E501


        :return: The updated_at of this IntegrationCreateAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this IntegrationCreateAttributes.


        :param updated_at: The updated_at of this IntegrationCreateAttributes.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def enabled(self):
        """Gets the enabled of this IntegrationCreateAttributes.  # noqa: E501


        :return: The enabled of this IntegrationCreateAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this IntegrationCreateAttributes.


        :param enabled: The enabled of this IntegrationCreateAttributes.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def connected(self):
        """Gets the connected of this IntegrationCreateAttributes.  # noqa: E501


        :return: The connected of this IntegrationCreateAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        """Sets the connected of this IntegrationCreateAttributes.


        :param connected: The connected of this IntegrationCreateAttributes.  # noqa: E501
        :type: bool
        """

        self._connected = connected

    @property
    def connection_last_checked_at(self):
        """Gets the connection_last_checked_at of this IntegrationCreateAttributes.  # noqa: E501


        :return: The connection_last_checked_at of this IntegrationCreateAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._connection_last_checked_at

    @connection_last_checked_at.setter
    def connection_last_checked_at(self, connection_last_checked_at):
        """Sets the connection_last_checked_at of this IntegrationCreateAttributes.


        :param connection_last_checked_at: The connection_last_checked_at of this IntegrationCreateAttributes.  # noqa: E501
        :type: datetime
        """

        self._connection_last_checked_at = connection_last_checked_at

    @property
    def integration_type(self):
        """Gets the integration_type of this IntegrationCreateAttributes.  # noqa: E501

        * `amazon_s3` - Amazon S3 * `saml` - SAML * `aws_security_hub` - AWS Security Hub * `jira` - JIRA * `slack` - Slack  # noqa: E501

        :return: The integration_type of this IntegrationCreateAttributes.  # noqa: E501
        :rtype: str
        """
        return self._integration_type

    @integration_type.setter
    def integration_type(self, integration_type):
        """Sets the integration_type of this IntegrationCreateAttributes.

        * `amazon_s3` - Amazon S3 * `saml` - SAML * `aws_security_hub` - AWS Security Hub * `jira` - JIRA * `slack` - Slack  # noqa: E501

        :param integration_type: The integration_type of this IntegrationCreateAttributes.  # noqa: E501
        :type: str
        """
        if integration_type is None:
            raise ValueError("Invalid value for `integration_type`, must not be `None`")  # noqa: E501
        allowed_values = ["amazon_s3", "saml", "aws_security_hub", "jira", "slack"]  # noqa: E501
        if integration_type not in allowed_values:
            raise ValueError(
                "Invalid value for `integration_type` ({0}), must be one of {1}"  # noqa: E501
                .format(integration_type, allowed_values)
            )

        self._integration_type = integration_type

    @property
    def configuration(self):
        """Gets the configuration of this IntegrationCreateAttributes.  # noqa: E501


        :return: The configuration of this IntegrationCreateAttributes.  # noqa: E501
        :rtype: OneOfIntegrationCreateAttributesConfiguration
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this IntegrationCreateAttributes.


        :param configuration: The configuration of this IntegrationCreateAttributes.  # noqa: E501
        :type: OneOfIntegrationCreateAttributesConfiguration
        """
        if configuration is None:
            raise ValueError("Invalid value for `configuration`, must not be `None`")  # noqa: E501

        self._configuration = configuration

    @property
    def credentials(self):
        """Gets the credentials of this IntegrationCreateAttributes.  # noqa: E501


        :return: The credentials of this IntegrationCreateAttributes.  # noqa: E501
        :rtype: OneOfIntegrationCreateAttributesCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this IntegrationCreateAttributes.


        :param credentials: The credentials of this IntegrationCreateAttributes.  # noqa: E501
        :type: OneOfIntegrationCreateAttributesCredentials
        """
        if credentials is None:
            raise ValueError("Invalid value for `credentials`, must not be `None`")  # noqa: E501

        self._credentials = credentials

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(IntegrationCreateAttributes, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IntegrationCreateAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
