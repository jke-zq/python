# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.13.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1ListMeta(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        '_continue': 'str',
        'resource_version': 'str',
        'self_link': 'str'
    }

    attribute_map = {
        '_continue': 'continue',
        'resource_version': 'resourceVersion',
        'self_link': 'selfLink'
    }

    def __init__(self, _continue=None, resource_version=None, self_link=None):
        """
        V1ListMeta - a model defined in Swagger
        """

        self.__continue = None
        self._resource_version = None
        self._self_link = None
        self.discriminator = None

        if _continue is not None:
          self._continue = _continue
        if resource_version is not None:
          self.resource_version = resource_version
        if self_link is not None:
          self.self_link = self_link

    @property
    def _continue(self):
        """
        Gets the _continue of this V1ListMeta.
        continue may be set if the user set a limit on the number of items returned, and indicates that the server has more data available. The value is opaque and may be used to issue another request to the endpoint that served this list to retrieve the next set of available objects. Continuing a consistent list may not be possible if the server configuration has changed or more than a few minutes have passed. The resourceVersion field returned when using this continue value will be identical to the value in the first response, unless you have received this token from an error message.

        :return: The _continue of this V1ListMeta.
        :rtype: str
        """
        return self.__continue

    @_continue.setter
    def _continue(self, _continue):
        """
        Sets the _continue of this V1ListMeta.
        continue may be set if the user set a limit on the number of items returned, and indicates that the server has more data available. The value is opaque and may be used to issue another request to the endpoint that served this list to retrieve the next set of available objects. Continuing a consistent list may not be possible if the server configuration has changed or more than a few minutes have passed. The resourceVersion field returned when using this continue value will be identical to the value in the first response, unless you have received this token from an error message.

        :param _continue: The _continue of this V1ListMeta.
        :type: str
        """

        self.__continue = _continue

    @property
    def resource_version(self):
        """
        Gets the resource_version of this V1ListMeta.
        String that identifies the server's internal version of this object that can be used by clients to determine when objects have changed. Value must be treated as opaque by clients and passed unmodified back to the server. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#concurrency-control-and-consistency

        :return: The resource_version of this V1ListMeta.
        :rtype: str
        """
        return self._resource_version

    @resource_version.setter
    def resource_version(self, resource_version):
        """
        Sets the resource_version of this V1ListMeta.
        String that identifies the server's internal version of this object that can be used by clients to determine when objects have changed. Value must be treated as opaque by clients and passed unmodified back to the server. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#concurrency-control-and-consistency

        :param resource_version: The resource_version of this V1ListMeta.
        :type: str
        """

        self._resource_version = resource_version

    @property
    def self_link(self):
        """
        Gets the self_link of this V1ListMeta.
        selfLink is a URL representing this object. Populated by the system. Read-only.

        :return: The self_link of this V1ListMeta.
        :rtype: str
        """
        return self._self_link

    @self_link.setter
    def self_link(self, self_link):
        """
        Sets the self_link of this V1ListMeta.
        selfLink is a URL representing this object. Populated by the system. Read-only.

        :param self_link: The self_link of this V1ListMeta.
        :type: str
        """

        self._self_link = self_link

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1ListMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
