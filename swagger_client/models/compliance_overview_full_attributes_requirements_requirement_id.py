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

class ComplianceOverviewFullAttributesRequirementsRequirementId(object):
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
        'checks': 'ComplianceOverviewFullAttributesRequirementsRequirementIdChecks',
        'status': 'str',
        'attributes': 'list[object]',
        'description': 'str',
        'checks_status': 'ComplianceOverviewFullAttributesRequirementsRequirementIdChecksStatus'
    }

    attribute_map = {
        'name': 'name',
        'checks': 'checks',
        'status': 'status',
        'attributes': 'attributes',
        'description': 'description',
        'checks_status': 'checks_status'
    }

    def __init__(self, name=None, checks=None, status=None, attributes=None, description=None, checks_status=None):  # noqa: E501
        """ComplianceOverviewFullAttributesRequirementsRequirementId - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._checks = None
        self._status = None
        self._attributes = None
        self._description = None
        self._checks_status = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if checks is not None:
            self.checks = checks
        if status is not None:
            self.status = status
        if attributes is not None:
            self.attributes = attributes
        if description is not None:
            self.description = description
        if checks_status is not None:
            self.checks_status = checks_status

    @property
    def name(self):
        """Gets the name of this ComplianceOverviewFullAttributesRequirementsRequirementId.  # noqa: E501


        :return: The name of this ComplianceOverviewFullAttributesRequirementsRequirementId.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComplianceOverviewFullAttributesRequirementsRequirementId.


        :param name: The name of this ComplianceOverviewFullAttributesRequirementsRequirementId.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def checks(self):
        """Gets the checks of this ComplianceOverviewFullAttributesRequirementsRequirementId.  # noqa: E501


        :return: The checks of this ComplianceOverviewFullAttributesRequirementsRequirementId.  # noqa: E501
        :rtype: ComplianceOverviewFullAttributesRequirementsRequirementIdChecks
        """
        return self._checks

    @checks.setter
    def checks(self, checks):
        """Sets the checks of this ComplianceOverviewFullAttributesRequirementsRequirementId.


        :param checks: The checks of this ComplianceOverviewFullAttributesRequirementsRequirementId.  # noqa: E501
        :type: ComplianceOverviewFullAttributesRequirementsRequirementIdChecks
        """

        self._checks = checks

    @property
    def status(self):
        """Gets the status of this ComplianceOverviewFullAttributesRequirementsRequirementId.  # noqa: E501


        :return: The status of this ComplianceOverviewFullAttributesRequirementsRequirementId.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ComplianceOverviewFullAttributesRequirementsRequirementId.


        :param status: The status of this ComplianceOverviewFullAttributesRequirementsRequirementId.  # noqa: E501
        :type: str
        """
        allowed_values = ["PASS", "FAIL", "MANUAL"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def attributes(self):
        """Gets the attributes of this ComplianceOverviewFullAttributesRequirementsRequirementId.  # noqa: E501


        :return: The attributes of this ComplianceOverviewFullAttributesRequirementsRequirementId.  # noqa: E501
        :rtype: list[object]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this ComplianceOverviewFullAttributesRequirementsRequirementId.


        :param attributes: The attributes of this ComplianceOverviewFullAttributesRequirementsRequirementId.  # noqa: E501
        :type: list[object]
        """

        self._attributes = attributes

    @property
    def description(self):
        """Gets the description of this ComplianceOverviewFullAttributesRequirementsRequirementId.  # noqa: E501


        :return: The description of this ComplianceOverviewFullAttributesRequirementsRequirementId.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ComplianceOverviewFullAttributesRequirementsRequirementId.


        :param description: The description of this ComplianceOverviewFullAttributesRequirementsRequirementId.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def checks_status(self):
        """Gets the checks_status of this ComplianceOverviewFullAttributesRequirementsRequirementId.  # noqa: E501


        :return: The checks_status of this ComplianceOverviewFullAttributesRequirementsRequirementId.  # noqa: E501
        :rtype: ComplianceOverviewFullAttributesRequirementsRequirementIdChecksStatus
        """
        return self._checks_status

    @checks_status.setter
    def checks_status(self, checks_status):
        """Sets the checks_status of this ComplianceOverviewFullAttributesRequirementsRequirementId.


        :param checks_status: The checks_status of this ComplianceOverviewFullAttributesRequirementsRequirementId.  # noqa: E501
        :type: ComplianceOverviewFullAttributesRequirementsRequirementIdChecksStatus
        """

        self._checks_status = checks_status

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
        if issubclass(ComplianceOverviewFullAttributesRequirementsRequirementId, dict):
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
        if not isinstance(other, ComplianceOverviewFullAttributesRequirementsRequirementId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
