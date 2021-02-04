from typing import Tuple, Union

import connexion
import six

from swagger_server.controllers.src.cuadrados_numeros import cuadrados_numeros
from swagger_server.models.calcular_cuadrado_response import CalcularCuadradoResponse  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server import util


def cuadrados_numeros_post(numeros) -> Union[CalcularCuadradoResponse, Tuple[Error, int]]:  # noqa: E501
    """Devuelve el cuadrado de los números introducidos

     # noqa: E501

    :param numeros: 
    :type numeros: List[]

    :rtype: CalcularCuadradoResponse
    """
    try:
        return cuadrados_numeros(numeros)
    except:
        return Error("Error desconocido"), 500
