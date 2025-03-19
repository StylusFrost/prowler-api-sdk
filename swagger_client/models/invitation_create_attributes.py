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

class InvitationCreateAttributes(object):
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
        'email': 'str',
        'expires_at': 'datetime',
        'state': 'str',
        'token': 'str'
    }

    attribute_map = {
        'email': 'email',
        'expires_at': 'expires_at',
        'state': 'state',
        'token': 'token'
    }

    def __init__(self, email=None, expires_at=None, state=None, token=None):  # noqa: E501
        """InvitationCreateAttributes - a model defined in Swagger"""  # noqa: E501
        self._email = None
        self._expires_at = None
        self._state = None
        self._token = None
        self.discriminator = None
        self.email = email
        if expires_at is not None:
            self.expires_at = expires_at
        if state is not None:
            self.state = state
        if token is not None:
            self.token = token

    @property
    def email(self):
        """Gets the email of this InvitationCreateAttributes.  # noqa: E501


        :return: The email of this InvitationCreateAttributes.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this InvitationCreateAttributes.


        :param email: The email of this InvitationCreateAttributes.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def expires_at(self):
        """Gets the expires_at of this InvitationCreateAttributes.  # noqa: E501

        UTC. Default 7 days. If this attribute is provided, it must be at least 24 hours in the future.  # noqa: E501

        :return: The expires_at of this InvitationCreateAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this InvitationCreateAttributes.

        UTC. Default 7 days. If this attribute is provided, it must be at least 24 hours in the future.  # noqa: E501

        :param expires_at: The expires_at of this InvitationCreateAttributes.  # noqa: E501
        :type: datetime
        """

        self._expires_at = expires_at

    @property
    def state(self):
        """Gets the state of this InvitationCreateAttributes.  # noqa: E501

        * `pending` - Invitation is pending * `accepted` - Invitation was accepted by a user * `expired` - Invitation expired after the configured time * `revoked` - Invitation was revoked by a user  # noqa: E501

        :return: The state of this InvitationCreateAttributes.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this InvitationCreateAttributes.

        * `pending` - Invitation is pending * `accepted` - Invitation was accepted by a user * `expired` - Invitation expired after the configured time * `revoked` - Invitation was revoked by a user  # noqa: E501

        :param state: The state of this InvitationCreateAttributes.  # noqa: E501
        :type: str
        """
        allowed_values = ["pending", "accepted", "expired", "revoked"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def token(self):
        """Gets the token of this InvitationCreateAttributes.  # noqa: E501


        :return: The token of this InvitationCreateAttributes.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this InvitationCreateAttributes.


        :param token: The token of this InvitationCreateAttributes.  # noqa: E501
        :type: str
        """

        self._token = token

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
        if issubclass(InvitationCreateAttributes, dict):
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
        if not isinstance(other, InvitationCreateAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
