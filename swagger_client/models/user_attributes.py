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

class UserAttributes(object):
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
        'name': 'str',
        'email': 'str',
        'company_name': 'str',
        'date_joined': 'datetime'
    }

    attribute_map = {
        'name': 'name',
        'email': 'email',
        'company_name': 'company_name',
        'date_joined': 'date_joined'
    }

    def __init__(self, name=None, email=None, company_name=None, date_joined=None):  # noqa: E501
        """UserAttributes - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._email = None
        self._company_name = None
        self._date_joined = None
        self.discriminator = None
        self.name = name
        self.email = email
        if company_name is not None:
            self.company_name = company_name
        if date_joined is not None:
            self.date_joined = date_joined

    @property
    def name(self):
        """Gets the name of this UserAttributes.  # noqa: E501


        :return: The name of this UserAttributes.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserAttributes.


        :param name: The name of this UserAttributes.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def email(self):
        """Gets the email of this UserAttributes.  # noqa: E501

        Case insensitive  # noqa: E501

        :return: The email of this UserAttributes.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserAttributes.

        Case insensitive  # noqa: E501

        :param email: The email of this UserAttributes.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def company_name(self):
        """Gets the company_name of this UserAttributes.  # noqa: E501


        :return: The company_name of this UserAttributes.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this UserAttributes.


        :param company_name: The company_name of this UserAttributes.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def date_joined(self):
        """Gets the date_joined of this UserAttributes.  # noqa: E501


        :return: The date_joined of this UserAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._date_joined

    @date_joined.setter
    def date_joined(self, date_joined):
        """Sets the date_joined of this UserAttributes.


        :param date_joined: The date_joined of this UserAttributes.  # noqa: E501
        :type: datetime
        """

        self._date_joined = date_joined

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
        if issubclass(UserAttributes, dict):
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
        if not isinstance(other, UserAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
