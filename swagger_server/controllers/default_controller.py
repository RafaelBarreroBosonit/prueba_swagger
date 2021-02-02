import connexion
import six

from swagger_server.models.calcular_cuadrado_response import CalcularCuadradoResponse  # noqa: E501
from swagger_server.models.calcular_media_post import CalcularMediaPost  # noqa: E501
from swagger_server.models.calcular_media_response200 import CalcularMediaResponse200  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.error400 import Error400  # noqa: E501
from swagger_server.models.error404 import Error404  # noqa: E501
from swagger_server.models.error500 import Error500  # noqa: E501
from swagger_server import util


def cuadrados_numeros_post(numeros):  # noqa: E501
    """Devuelve el cuadrado de los números introducidos

     # noqa: E501

    :param numeros: 
    :type numeros: List[]

    :rtype: CalcularCuadradoResponse
    """
    return 'do some magic!'


def media_post(numeros):  # noqa: E501
    """Devuelve la media de los números introducidos

     # noqa: E501

    :param numeros: La media de los números a devolver
    :type numeros: dict | bytes

    :rtype: CalcularMediaResponse200
    """
    if connexion.request.is_json:
        numeros = CalcularMediaPost.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
