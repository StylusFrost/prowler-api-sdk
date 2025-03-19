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

class Finding(object):
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
        'type': 'AllOfFindingType',
        'id': 'str',
        'attributes': 'FindingAttributes',
        'relationships': 'FindingRelationships'
    }

    attribute_map = {
        'type': 'type',
        'id': 'id',
        'attributes': 'attributes',
        'relationships': 'relationships'
    }

    def __init__(self, type=None, id=None, attributes=None, relationships=None):  # noqa: E501
        """Finding - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._id = None
        self._attributes = None
        self._relationships = None
        self.discriminator = None
        self.type = type
        self.id = id
        if attributes is not None:
            self.attributes = attributes
        if relationships is not None:
            self.relationships = relationships

    @property
    def type(self):
        """Gets the type of this Finding.  # noqa: E501

        The [type](https://jsonapi.org/format/#document-resource-object-identification) member is used to describe resource objects that share common attributes and relationships.  # noqa: E501

        :return: The type of this Finding.  # noqa: E501
        :rtype: AllOfFindingType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Finding.

        The [type](https://jsonapi.org/format/#document-resource-object-identification) member is used to describe resource objects that share common attributes and relationships.  # noqa: E501

        :param type: The type of this Finding.  # noqa: E501
        :type: AllOfFindingType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def id(self):
        """Gets the id of this Finding.  # noqa: E501


        :return: The id of this Finding.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Finding.


        :param id: The id of this Finding.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def attributes(self):
        """Gets the attributes of this Finding.  # noqa: E501


        :return: The attributes of this Finding.  # noqa: E501
        :rtype: FindingAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Finding.


        :param attributes: The attributes of this Finding.  # noqa: E501
        :type: FindingAttributes
        """

        self._attributes = attributes

    @property
    def relationships(self):
        """Gets the relationships of this Finding.  # noqa: E501


        :return: The relationships of this Finding.  # noqa: E501
        :rtype: FindingRelationships
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """Sets the relationships of this Finding.


        :param relationships: The relationships of this Finding.  # noqa: E501
        :type: FindingRelationships
        """

        self._relationships = relationships

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
        if issubclass(Finding, dict):
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
        if not isinstance(other, Finding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
