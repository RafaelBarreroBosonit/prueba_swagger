import connexion
import six
import numpy as np

from swagger_server.models import CalcularCuadradoArray
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
    list_array = []
    if numeros:
        numbers = np.array(numeros)
        for number in numbers:
            try:
                cuadrado = int(np.square(int(number)))
            except ValueError:
                cuadrado = float(np.square(float(number)))
            list_array.append(CalcularCuadradoArray(cuadrado, number))
        return CalcularCuadradoResponse(list_array, len(list_array))


def media_post(numeros):  # noqa: E501
    """Devuelve la media de los números introducidos

     # noqa: E501

    :param numeros: La media de los números a devolver
    :type numeros: dict | bytes

    :rtype: CalcularMediaResponse200
    """
    if connexion.request.is_json:
        numeros = CalcularMediaPost.from_dict(connexion.request.get_json())  # noqa: E501
        numbers = np.array(numeros.numeros)
        redondear = numeros.redondear
        if redondear:
            media = np.trunc(np.mean(numbers))
        else:
            media = np.mean(numbers)
        return CalcularMediaResponse200(media)
