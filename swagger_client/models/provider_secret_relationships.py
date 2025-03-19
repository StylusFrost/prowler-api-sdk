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

class ProviderSecretRelationships(object):
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
        'provider': 'ResourceIdentifier8'
    }

    attribute_map = {
        'provider': 'provider'
    }

    def __init__(self, provider=None):  # noqa: E501
        """ProviderSecretRelationships - a model defined in Swagger"""  # noqa: E501
        self._provider = None
        self.discriminator = None
        self.provider = provider

    @property
    def provider(self):
        """Gets the provider of this ProviderSecretRelationships.  # noqa: E501


        :return: The provider of this ProviderSecretRelationships.  # noqa: E501
        :rtype: ResourceIdentifier8
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ProviderSecretRelationships.


        :param provider: The provider of this ProviderSecretRelationships.  # noqa: E501
        :type: ResourceIdentifier8
        """
        if provider is None:
            raise ValueError("Invalid value for `provider`, must not be `None`")  # noqa: E501

        self._provider = provider

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
        if issubclass(ProviderSecretRelationships, dict):
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
        if not isinstance(other, ProviderSecretRelationships):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
