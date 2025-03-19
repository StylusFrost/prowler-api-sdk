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

class OverviewProviderAttributes(object):
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
        'id': 'str',
        'findings': 'OverviewProviderAttributesFindings',
        'resources': 'OverviewProviderAttributesResources'
    }

    attribute_map = {
        'id': 'id',
        'findings': 'findings',
        'resources': 'resources'
    }

    def __init__(self, id=None, findings=None, resources=None):  # noqa: E501
        """OverviewProviderAttributes - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._findings = None
        self._resources = None
        self.discriminator = None
        self.id = id
        if findings is not None:
            self.findings = findings
        if resources is not None:
            self.resources = resources

    @property
    def id(self):
        """Gets the id of this OverviewProviderAttributes.  # noqa: E501


        :return: The id of this OverviewProviderAttributes.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OverviewProviderAttributes.


        :param id: The id of this OverviewProviderAttributes.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def findings(self):
        """Gets the findings of this OverviewProviderAttributes.  # noqa: E501


        :return: The findings of this OverviewProviderAttributes.  # noqa: E501
        :rtype: OverviewProviderAttributesFindings
        """
        return self._findings

    @findings.setter
    def findings(self, findings):
        """Sets the findings of this OverviewProviderAttributes.


        :param findings: The findings of this OverviewProviderAttributes.  # noqa: E501
        :type: OverviewProviderAttributesFindings
        """

        self._findings = findings

    @property
    def resources(self):
        """Gets the resources of this OverviewProviderAttributes.  # noqa: E501


        :return: The resources of this OverviewProviderAttributes.  # noqa: E501
        :rtype: OverviewProviderAttributesResources
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this OverviewProviderAttributes.


        :param resources: The resources of this OverviewProviderAttributes.  # noqa: E501
        :type: OverviewProviderAttributesResources
        """

        self._resources = resources

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
        if issubclass(OverviewProviderAttributes, dict):
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
        if not isinstance(other, OverviewProviderAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
