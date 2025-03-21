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

class ComplianceOverviewFullAttributesRequirementsRequirementIdChecksStatus(object):
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
        'total': 'int',
        '_pass': 'int',
        'fail': 'int',
        'manual': 'int'
    }

    attribute_map = {
        'total': 'total',
        '_pass': 'pass',
        'fail': 'fail',
        'manual': 'manual'
    }

    def __init__(self, total=None, _pass=None, fail=None, manual=None):  # noqa: E501
        """ComplianceOverviewFullAttributesRequirementsRequirementIdChecksStatus - a model defined in Swagger"""  # noqa: E501
        self._total = None
        self.__pass = None
        self._fail = None
        self._manual = None
        self.discriminator = None
        if total is not None:
            self.total = total
        if _pass is not None:
            self._pass = _pass
        if fail is not None:
            self.fail = fail
        if manual is not None:
            self.manual = manual

    @property
    def total(self):
        """Gets the total of this ComplianceOverviewFullAttributesRequirementsRequirementIdChecksStatus.  # noqa: E501


        :return: The total of this ComplianceOverviewFullAttributesRequirementsRequirementIdChecksStatus.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ComplianceOverviewFullAttributesRequirementsRequirementIdChecksStatus.


        :param total: The total of this ComplianceOverviewFullAttributesRequirementsRequirementIdChecksStatus.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def _pass(self):
        """Gets the _pass of this ComplianceOverviewFullAttributesRequirementsRequirementIdChecksStatus.  # noqa: E501


        :return: The _pass of this ComplianceOverviewFullAttributesRequirementsRequirementIdChecksStatus.  # noqa: E501
        :rtype: int
        """
        return self.__pass

    @_pass.setter
    def _pass(self, _pass):
        """Sets the _pass of this ComplianceOverviewFullAttributesRequirementsRequirementIdChecksStatus.


        :param _pass: The _pass of this ComplianceOverviewFullAttributesRequirementsRequirementIdChecksStatus.  # noqa: E501
        :type: int
        """

        self.__pass = _pass

    @property
    def fail(self):
        """Gets the fail of this ComplianceOverviewFullAttributesRequirementsRequirementIdChecksStatus.  # noqa: E501


        :return: The fail of this ComplianceOverviewFullAttributesRequirementsRequirementIdChecksStatus.  # noqa: E501
        :rtype: int
        """
        return self._fail

    @fail.setter
    def fail(self, fail):
        """Sets the fail of this ComplianceOverviewFullAttributesRequirementsRequirementIdChecksStatus.


        :param fail: The fail of this ComplianceOverviewFullAttributesRequirementsRequirementIdChecksStatus.  # noqa: E501
        :type: int
        """

        self._fail = fail

    @property
    def manual(self):
        """Gets the manual of this ComplianceOverviewFullAttributesRequirementsRequirementIdChecksStatus.  # noqa: E501


        :return: The manual of this ComplianceOverviewFullAttributesRequirementsRequirementIdChecksStatus.  # noqa: E501
        :rtype: int
        """
        return self._manual

    @manual.setter
    def manual(self, manual):
        """Sets the manual of this ComplianceOverviewFullAttributesRequirementsRequirementIdChecksStatus.


        :param manual: The manual of this ComplianceOverviewFullAttributesRequirementsRequirementIdChecksStatus.  # noqa: E501
        :type: int
        """

        self._manual = manual

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
        if issubclass(ComplianceOverviewFullAttributesRequirementsRequirementIdChecksStatus, dict):
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
        if not isinstance(other, ComplianceOverviewFullAttributesRequirementsRequirementIdChecksStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
