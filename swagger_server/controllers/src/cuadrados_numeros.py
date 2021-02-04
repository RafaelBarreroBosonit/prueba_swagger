import numpy as np

from swagger_server.models import CalcularCuadradoArray, CalcularCuadradoResponse, Error


def cuadrados_numeros(numeros: list) -> (CalcularCuadradoResponse, Error):
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
    else:
        return Error("No se ha introducido números"), 400
