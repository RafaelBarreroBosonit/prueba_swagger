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
                if number.isnumeric():
                    cuadrado = float(np.square(float(number)))
                else:
                    return Error("No se admiten letras"), 400
            except TypeError:
                return Error("Los datos introducidos no son válidos"), 400
            list_array.append(CalcularCuadradoArray(cuadrado, number))
        return CalcularCuadradoResponse(list_array, len(list_array))
    else:
        return Error("No se ha introducido números"), 400
