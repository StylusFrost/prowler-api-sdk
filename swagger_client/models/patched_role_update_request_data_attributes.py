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

class PatchedRoleUpdateRequestDataAttributes(object):
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
        'manage_users': 'bool',
        'manage_account': 'bool',
        'manage_providers': 'bool',
        'manage_scans': 'bool',
        'permission_state': 'str',
        'unlimited_visibility': 'bool',
        'inserted_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'name': 'name',
        'manage_users': 'manage_users',
        'manage_account': 'manage_account',
        'manage_providers': 'manage_providers',
        'manage_scans': 'manage_scans',
        'permission_state': 'permission_state',
        'unlimited_visibility': 'unlimited_visibility',
        'inserted_at': 'inserted_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, name=None, manage_users=None, manage_account=None, manage_providers=None, manage_scans=None, permission_state=None, unlimited_visibility=None, inserted_at=None, updated_at=None):  # noqa: E501
        """PatchedRoleUpdateRequestDataAttributes - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._manage_users = None
        self._manage_account = None
        self._manage_providers = None
        self._manage_scans = None
        self._permission_state = None
        self._unlimited_visibility = None
        self._inserted_at = None
        self._updated_at = None
        self.discriminator = None
        self.name = name
        if manage_users is not None:
            self.manage_users = manage_users
        if manage_account is not None:
            self.manage_account = manage_account
        if manage_providers is not None:
            self.manage_providers = manage_providers
        if manage_scans is not None:
            self.manage_scans = manage_scans
        if permission_state is not None:
            self.permission_state = permission_state
        if unlimited_visibility is not None:
            self.unlimited_visibility = unlimited_visibility
        if inserted_at is not None:
            self.inserted_at = inserted_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def name(self):
        """Gets the name of this PatchedRoleUpdateRequestDataAttributes.  # noqa: E501


        :return: The name of this PatchedRoleUpdateRequestDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PatchedRoleUpdateRequestDataAttributes.


        :param name: The name of this PatchedRoleUpdateRequestDataAttributes.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def manage_users(self):
        """Gets the manage_users of this PatchedRoleUpdateRequestDataAttributes.  # noqa: E501


        :return: The manage_users of this PatchedRoleUpdateRequestDataAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._manage_users

    @manage_users.setter
    def manage_users(self, manage_users):
        """Sets the manage_users of this PatchedRoleUpdateRequestDataAttributes.


        :param manage_users: The manage_users of this PatchedRoleUpdateRequestDataAttributes.  # noqa: E501
        :type: bool
        """

        self._manage_users = manage_users

    @property
    def manage_account(self):
        """Gets the manage_account of this PatchedRoleUpdateRequestDataAttributes.  # noqa: E501


        :return: The manage_account of this PatchedRoleUpdateRequestDataAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._manage_account

    @manage_account.setter
    def manage_account(self, manage_account):
        """Sets the manage_account of this PatchedRoleUpdateRequestDataAttributes.


        :param manage_account: The manage_account of this PatchedRoleUpdateRequestDataAttributes.  # noqa: E501
        :type: bool
        """

        self._manage_account = manage_account

    @property
    def manage_providers(self):
        """Gets the manage_providers of this PatchedRoleUpdateRequestDataAttributes.  # noqa: E501


        :return: The manage_providers of this PatchedRoleUpdateRequestDataAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._manage_providers

    @manage_providers.setter
    def manage_providers(self, manage_providers):
        """Sets the manage_providers of this PatchedRoleUpdateRequestDataAttributes.


        :param manage_providers: The manage_providers of this PatchedRoleUpdateRequestDataAttributes.  # noqa: E501
        :type: bool
        """

        self._manage_providers = manage_providers

    @property
    def manage_scans(self):
        """Gets the manage_scans of this PatchedRoleUpdateRequestDataAttributes.  # noqa: E501


        :return: The manage_scans of this PatchedRoleUpdateRequestDataAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._manage_scans

    @manage_scans.setter
    def manage_scans(self, manage_scans):
        """Sets the manage_scans of this PatchedRoleUpdateRequestDataAttributes.


        :param manage_scans: The manage_scans of this PatchedRoleUpdateRequestDataAttributes.  # noqa: E501
        :type: bool
        """

        self._manage_scans = manage_scans

    @property
    def permission_state(self):
        """Gets the permission_state of this PatchedRoleUpdateRequestDataAttributes.  # noqa: E501


        :return: The permission_state of this PatchedRoleUpdateRequestDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._permission_state

    @permission_state.setter
    def permission_state(self, permission_state):
        """Sets the permission_state of this PatchedRoleUpdateRequestDataAttributes.


        :param permission_state: The permission_state of this PatchedRoleUpdateRequestDataAttributes.  # noqa: E501
        :type: str
        """

        self._permission_state = permission_state

    @property
    def unlimited_visibility(self):
        """Gets the unlimited_visibility of this PatchedRoleUpdateRequestDataAttributes.  # noqa: E501


        :return: The unlimited_visibility of this PatchedRoleUpdateRequestDataAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._unlimited_visibility

    @unlimited_visibility.setter
    def unlimited_visibility(self, unlimited_visibility):
        """Sets the unlimited_visibility of this PatchedRoleUpdateRequestDataAttributes.


        :param unlimited_visibility: The unlimited_visibility of this PatchedRoleUpdateRequestDataAttributes.  # noqa: E501
        :type: bool
        """

        self._unlimited_visibility = unlimited_visibility

    @property
    def inserted_at(self):
        """Gets the inserted_at of this PatchedRoleUpdateRequestDataAttributes.  # noqa: E501


        :return: The inserted_at of this PatchedRoleUpdateRequestDataAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._inserted_at

    @inserted_at.setter
    def inserted_at(self, inserted_at):
        """Sets the inserted_at of this PatchedRoleUpdateRequestDataAttributes.


        :param inserted_at: The inserted_at of this PatchedRoleUpdateRequestDataAttributes.  # noqa: E501
        :type: datetime
        """

        self._inserted_at = inserted_at

    @property
    def updated_at(self):
        """Gets the updated_at of this PatchedRoleUpdateRequestDataAttributes.  # noqa: E501


        :return: The updated_at of this PatchedRoleUpdateRequestDataAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this PatchedRoleUpdateRequestDataAttributes.


        :param updated_at: The updated_at of this PatchedRoleUpdateRequestDataAttributes.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if issubclass(PatchedRoleUpdateRequestDataAttributes, dict):
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
        if not isinstance(other, PatchedRoleUpdateRequestDataAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
