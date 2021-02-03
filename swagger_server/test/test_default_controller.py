# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.calcular_cuadrado_response import CalcularCuadradoResponse  # noqa: E501
from swagger_server.models.calcular_media_post import CalcularMediaPost  # noqa: E501
from swagger_server.models.calcular_media_response200 import CalcularMediaResponse200  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_cuadrados_numeros_post(self):
        """Test case for cuadrados_numeros_post

        Devuelve el cuadrado de los números introducidos
        """
        response = self.client.open(
            '/cuadrados/{numeros}'.format(numeros=3.4),
            method='POST')
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
