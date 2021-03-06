# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CalcularMediaCsvUrl(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, url: str=None, redondear: bool=None):  # noqa: E501
        """CalcularMediaCsvUrl - a model defined in Swagger

        :param url: The url of this CalcularMediaCsvUrl.  # noqa: E501
        :type url: str
        :param redondear: The redondear of this CalcularMediaCsvUrl.  # noqa: E501
        :type redondear: bool
        """
        self.swagger_types = {
            'url': str,
            'redondear': bool
        }

        self.attribute_map = {
            'url': 'url',
            'redondear': 'redondear'
        }

        self._url = url
        self._redondear = redondear

    @classmethod
    def from_dict(cls, dikt) -> 'CalcularMediaCsvUrl':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Calcular_media_csv_url of this CalcularMediaCsvUrl.  # noqa: E501
        :rtype: CalcularMediaCsvUrl
        """
        return util.deserialize_model(dikt, cls)

    @property
    def url(self) -> str:
        """Gets the url of this CalcularMediaCsvUrl.


        :return: The url of this CalcularMediaCsvUrl.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this CalcularMediaCsvUrl.


        :param url: The url of this CalcularMediaCsvUrl.
        :type url: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def redondear(self) -> bool:
        """Gets the redondear of this CalcularMediaCsvUrl.


        :return: The redondear of this CalcularMediaCsvUrl.
        :rtype: bool
        """
        return self._redondear

    @redondear.setter
    def redondear(self, redondear: bool):
        """Sets the redondear of this CalcularMediaCsvUrl.


        :param redondear: The redondear of this CalcularMediaCsvUrl.
        :type redondear: bool
        """
        if redondear is None:
            raise ValueError("Invalid value for `redondear`, must not be `None`")  # noqa: E501

        self._redondear = redondear
