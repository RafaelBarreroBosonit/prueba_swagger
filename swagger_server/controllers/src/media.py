import csv
import os
from pathlib import Path

import numpy as np
import requests

from swagger_server.models import CalcularMediaResponse200, Error, CalcularMediaPost, CalcularMediaCsvUrl


def media_csv_url(url: CalcularMediaCsvUrl) -> (CalcularMediaResponse200, Error):
    base_path = Path(__file__).resolve().parent
    folder_csv = "input"
    absolute_path = Path(base_path).joinpath(folder_csv)  # Absolute path of input folder
    try:
        os.mkdir(absolute_path)
    except FileExistsError:
        pass
    try:
        r = requests.get(url.url)
    except requests.exceptions.MissingSchema:
        return Error("La URL no es válida"), 404
    except requests.exceptions.InvalidURL:
        return Error("La URL no es válida"), 404
    if r.status_code == 200:
        file_name = url.url.split("/")[-1]
        absolute_path_file = Path(absolute_path).joinpath(file_name)  # Absolute path of file

        with open(absolute_path_file, 'wb+') as file:
            file.write(r.content)

        with open(absolute_path_file, 'r') as file:
            my_reader = csv.reader(file, delimiter=',')
            next(my_reader)
            for row in my_reader:
                n = row[0]
                break
        n_lower = n.lower()
        if not n_lower.islower():
            numbers = np.fromstring(n, sep=',')
            redondear = url.redondear
            if redondear:
                media_numero = np.trunc(np.mean(numbers))
            else:
                media_numero = np.mean(numbers)
            os.remove(absolute_path_file)
            return CalcularMediaResponse200(media_numero)
        else:
            os.remove(absolute_path_file)
            return Error("El archivo no es válido, contiene letras"), 400
    else:
        return Error("Archivo no encontrado"), 404


def media(numeros: CalcularMediaPost) -> (CalcularMediaResponse200, Error):
    if numeros.numeros:
        numbers = np.array(numeros.numeros)
        if numbers.dtype == np.float64 or numbers.dtype == np.int32:
            redondear = numeros.redondear
            if redondear:
                media_numero = np.trunc(np.mean(numbers))
            else:
                media_numero = np.mean(numbers)
            return CalcularMediaResponse200(media_numero)
        else:
            return Error("El array de números contiene tipos no válidos"), 400
    else:
        return Error("El array está vacío"), 400
