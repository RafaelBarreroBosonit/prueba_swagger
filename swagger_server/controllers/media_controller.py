from typing import Union, Tuple

import connexion
import six

from swagger_server.controllers.src.media import media_csv_url, media
from swagger_server.models import CalcularMediaResponse200
from swagger_server.models.calcular_media_csv_url import CalcularMediaCsvUrl  # noqa: E501
from swagger_server.models.calcular_media_post import CalcularMediaPost  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server import util


def media_csv_url_post(url) -> Union[CalcularMediaResponse200, Tuple[Error, int]]:  # noqa: E501
    """Devuelve la media de los números en un csv

     # noqa: E501

    :param url: url donde se encuentra el csv
    :type url: dict | bytes

    :rtype: CalcularMediaResponse200
    """
    try:
        if connexion.request.is_json:
            url = CalcularMediaCsvUrl.from_dict(connexion.request.get_json())  # noqa: E501
            return media_csv_url(url)
        else:
            return Error("No es un JSON válido"), 400
    except:
        return Error("Error desconocido"), 500


def media_post(numeros) -> Union[CalcularMediaResponse200, Tuple[Error, int]]:  # noqa: E501
    """Devuelve la media de los números introducidos

     # noqa: E501

    :param numeros: La media de los números a devolver
    :type numeros: dict | bytes

    :rtype: CalcularMediaResponse200
    """
    try:
        if connexion.request.is_json:
            numeros = CalcularMediaPost.from_dict(connexion.request.get_json())  # noqa: E501
            return media(numeros)
        else:
            return Error("No es un JSON válido"), 400
    except:
        return Error("Error desconocido"), 500
