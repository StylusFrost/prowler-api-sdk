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

class TokenSwitchTenant(object):
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
        'type': 'AllOfTokenSwitchTenantType',
        'attributes': 'TokenSwitchTenantAttributes'
    }

    attribute_map = {
        'type': 'type',
        'attributes': 'attributes'
    }

    def __init__(self, type=None, attributes=None):  # noqa: E501
        """TokenSwitchTenant - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._attributes = None
        self.discriminator = None
        self.type = type
        if attributes is not None:
            self.attributes = attributes

    @property
    def type(self):
        """Gets the type of this TokenSwitchTenant.  # noqa: E501

        The [type](https://jsonapi.org/format/#document-resource-object-identification) member is used to describe resource objects that share common attributes and relationships.  # noqa: E501

        :return: The type of this TokenSwitchTenant.  # noqa: E501
        :rtype: AllOfTokenSwitchTenantType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TokenSwitchTenant.

        The [type](https://jsonapi.org/format/#document-resource-object-identification) member is used to describe resource objects that share common attributes and relationships.  # noqa: E501

        :param type: The type of this TokenSwitchTenant.  # noqa: E501
        :type: AllOfTokenSwitchTenantType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def attributes(self):
        """Gets the attributes of this TokenSwitchTenant.  # noqa: E501


        :return: The attributes of this TokenSwitchTenant.  # noqa: E501
        :rtype: TokenSwitchTenantAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this TokenSwitchTenant.


        :param attributes: The attributes of this TokenSwitchTenant.  # noqa: E501
        :type: TokenSwitchTenantAttributes
        """

        self._attributes = attributes

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
        if issubclass(TokenSwitchTenant, dict):
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
        if not isinstance(other, TokenSwitchTenant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
