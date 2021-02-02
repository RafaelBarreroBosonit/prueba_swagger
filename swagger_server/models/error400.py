# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Error400(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, error: str=None):  # noqa: E501
        """Error400 - a model defined in Swagger

        :param error: The error of this Error400.  # noqa: E501
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
    def from_dict(cls, dikt) -> 'Error400':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Error_400 of this Error400.  # noqa: E501
        :rtype: Error400
        """
        return util.deserialize_model(dikt, cls)

    @property
    def error(self) -> str:
        """Gets the error of this Error400.


        :return: The error of this Error400.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error: str):
        """Sets the error of this Error400.


        :param error: The error of this Error400.
        :type error: str
        """
        if error is None:
            raise ValueError("Invalid value for `error`, must not be `None`")  # noqa: E501

        self._error = error
