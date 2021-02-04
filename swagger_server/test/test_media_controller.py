# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.calcular_media_csv_url import CalcularMediaCsvUrl  # noqa: E501
from swagger_server.models.calcular_media_post import CalcularMediaPost  # noqa: E501
from swagger_server.models.calcular_media_response200 import CalcularMediaResponse200  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMediaController(BaseTestCase):
    """MediaController integration test stubs"""

    def test_media_csv_url_post(self):
        """Test case for media_csv_url_post

        Devuelve la media de los números en un csv
        """
        url = CalcularMediaCsvUrl()
        response = self.client.open(
            '/media_csv_url',
            method='POST',
            data=json.dumps(url),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_media_post(self):
        """Test case for media_post

        Devuelve la media de los números introducidos
        """
        numeros = CalcularMediaPost()
        response = self.client.open(
            '/media',
            method='POST',
            data=json.dumps(numeros),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
