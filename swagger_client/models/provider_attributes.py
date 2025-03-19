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

class ProviderAttributes(object):
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
        'provider': 'str',
        'uid': 'str',
        'alias': 'str',
        'connection': 'ProviderAttributesConnection'
    }

    attribute_map = {
        'inserted_at': 'inserted_at',
        'updated_at': 'updated_at',
        'provider': 'provider',
        'uid': 'uid',
        'alias': 'alias',
        'connection': 'connection'
    }

    def __init__(self, inserted_at=None, updated_at=None, provider=None, uid=None, alias=None, connection=None):  # noqa: E501
        """ProviderAttributes - a model defined in Swagger"""  # noqa: E501
        self._inserted_at = None
        self._updated_at = None
        self._provider = None
        self._uid = None
        self._alias = None
        self._connection = None
        self.discriminator = None
        if inserted_at is not None:
            self.inserted_at = inserted_at
        if updated_at is not None:
            self.updated_at = updated_at
        self.provider = provider
        self.uid = uid
        if alias is not None:
            self.alias = alias
        if connection is not None:
            self.connection = connection

    @property
    def inserted_at(self):
        """Gets the inserted_at of this ProviderAttributes.  # noqa: E501


        :return: The inserted_at of this ProviderAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._inserted_at

    @inserted_at.setter
    def inserted_at(self, inserted_at):
        """Sets the inserted_at of this ProviderAttributes.


        :param inserted_at: The inserted_at of this ProviderAttributes.  # noqa: E501
        :type: datetime
        """

        self._inserted_at = inserted_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ProviderAttributes.  # noqa: E501


        :return: The updated_at of this ProviderAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ProviderAttributes.


        :param updated_at: The updated_at of this ProviderAttributes.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def provider(self):
        """Gets the provider of this ProviderAttributes.  # noqa: E501

        * `aws` - AWS * `azure` - Azure * `gcp` - GCP * `kubernetes` - Kubernetes  # noqa: E501

        :return: The provider of this ProviderAttributes.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ProviderAttributes.

        * `aws` - AWS * `azure` - Azure * `gcp` - GCP * `kubernetes` - Kubernetes  # noqa: E501

        :param provider: The provider of this ProviderAttributes.  # noqa: E501
        :type: str
        """
        if provider is None:
            raise ValueError("Invalid value for `provider`, must not be `None`")  # noqa: E501
        allowed_values = ["aws", "azure", "gcp", "kubernetes"]  # noqa: E501
        if provider not in allowed_values:
            raise ValueError(
                "Invalid value for `provider` ({0}), must be one of {1}"  # noqa: E501
                .format(provider, allowed_values)
            )

        self._provider = provider

    @property
    def uid(self):
        """Gets the uid of this ProviderAttributes.  # noqa: E501


        :return: The uid of this ProviderAttributes.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this ProviderAttributes.


        :param uid: The uid of this ProviderAttributes.  # noqa: E501
        :type: str
        """
        if uid is None:
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501

        self._uid = uid

    @property
    def alias(self):
        """Gets the alias of this ProviderAttributes.  # noqa: E501


        :return: The alias of this ProviderAttributes.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this ProviderAttributes.


        :param alias: The alias of this ProviderAttributes.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def connection(self):
        """Gets the connection of this ProviderAttributes.  # noqa: E501


        :return: The connection of this ProviderAttributes.  # noqa: E501
        :rtype: ProviderAttributesConnection
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """Sets the connection of this ProviderAttributes.


        :param connection: The connection of this ProviderAttributes.  # noqa: E501
        :type: ProviderAttributesConnection
        """

        self._connection = connection

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
        if issubclass(ProviderAttributes, dict):
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
        if not isinstance(other, ProviderAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
