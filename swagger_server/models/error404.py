# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Error404(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, error: str=None):  # noqa: E501
        """Error404 - a model defined in Swagger

        :param error: The error of this Error404.  # noqa: E501
        :type error: str
        """
        self.swagger_types = {
            'error': str
        }

        self.attribute_map = {
            'error': 'error'
        }

        self._error = error

    @classmethod
    def from_dict(cls, dikt) -> 'Error404':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Error_404 of this Error404.  # noqa: E501
        :rtype: Error404
        """
        return util.deserialize_model(dikt, cls)

    @property
    def error(self) -> str:
        """Gets the error of this Error404.


        :return: The error of this Error404.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error: str):
        """Sets the error of this Error404.


        :param error: The error of this Error404.
        :type error: str
        """
        if error is None:
            raise ValueError("Invalid value for `error`, must not be `None`")  # noqa: E501

        self._error = error
