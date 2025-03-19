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

class MembershipRelationships(object):
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
        'user': 'ResourceIdentifier4',
        'tenant': 'ResourceIdentifier5'
    }

    attribute_map = {
        'user': 'user',
        'tenant': 'tenant'
    }

    def __init__(self, user=None, tenant=None):  # noqa: E501
        """MembershipRelationships - a model defined in Swagger"""  # noqa: E501
        self._user = None
        self._tenant = None
        self.discriminator = None
        if user is not None:
            self.user = user
        if tenant is not None:
            self.tenant = tenant

    @property
    def user(self):
        """Gets the user of this MembershipRelationships.  # noqa: E501


        :return: The user of this MembershipRelationships.  # noqa: E501
        :rtype: ResourceIdentifier4
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this MembershipRelationships.


        :param user: The user of this MembershipRelationships.  # noqa: E501
        :type: ResourceIdentifier4
        """

        self._user = user

    @property
    def tenant(self):
        """Gets the tenant of this MembershipRelationships.  # noqa: E501


        :return: The tenant of this MembershipRelationships.  # noqa: E501
        :rtype: ResourceIdentifier5
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this MembershipRelationships.


        :param tenant: The tenant of this MembershipRelationships.  # noqa: E501
        :type: ResourceIdentifier5
        """

        self._tenant = tenant

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
        if issubclass(MembershipRelationships, dict):
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
        if not isinstance(other, MembershipRelationships):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
