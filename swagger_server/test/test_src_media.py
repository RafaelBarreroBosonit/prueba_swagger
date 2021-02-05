import unittest

from swagger_server.controllers.src.media import media, media_csv_url
from swagger_server.models import CalcularMediaPost, Error, CalcularMediaCsvUrl


class TestMediaNumeros(unittest.TestCase):

    def test_ok_false(self):
        c = media(CalcularMediaPost([1, 4.34, 9], False))
        expected_media = 4.78
        self.assertEqual(c.media, expected_media)

    def test_ok_true(self):
        c = media(CalcularMediaPost([1, 4.34, 9], True))
        expected_media = 4
        self.assertEqual(c.media, expected_media)

    def test_ok_no_bool(self):
        c = media(CalcularMediaPost([1, 4.34, 9]))
        expected_media = 4.78
        self.assertEqual(c.media, expected_media)

    def test_none(self):
        c = media(CalcularMediaPost(None))
        expected_error = Error('El array está vacío')
        expected_code = 400
        self.assertEqual(c[0], expected_error)
        self.assertEqual(c[1], expected_code)

    def test_list_none(self):
        c = media(CalcularMediaPost([None]))
        expected_error = Error('El array de números contiene tipos no válidos')
        expected_code = 400
        self.assertEqual(c[0], expected_error)
        self.assertEqual(c[1], expected_code)

    def test_empty(self):
        c = media(CalcularMediaPost())
        expected_error = Error("El array está vacío")
        expected_code = 400
        self.assertEqual(c[0], expected_error)
        self.assertEqual(c[1], expected_code)

    def test_list_empty(self):
        c = media(CalcularMediaPost([]))
        expected_error = Error("El array está vacío")
        expected_code = 400
        self.assertEqual(c[0], expected_error)
        self.assertEqual(c[1], expected_code)

    def test_list_string(self):
        c = media(CalcularMediaPost([1, "asdasd", "2",  5]))
        expected_error = Error('El array de números contiene tipos no válidos')
        expected_code = 400
        self.assertEqual(c[0], expected_error)
        self.assertEqual(c[1], expected_code)

    def test_list_string_none(self):
        c = media(CalcularMediaPost([1, "asdasd", None,  5]))
        expected_error = Error('El array de números contiene tipos no válidos')
        expected_code = 400
        self.assertEqual(c[0], expected_error)
        self.assertEqual(c[1], expected_code)


class TestMediaNumerosCsvUrl(unittest.TestCase):

    def test_ok_false(self):
        self.url = "https://raw.githubusercontent.com/RafaelBarreroBosonit/prueba_swagger/master/csvs/numeros.csv"
        c = media_csv_url(CalcularMediaCsvUrl(self.url, False))
        expected_media = 4.78
        self.assertEqual(c.media, expected_media)

    def test_ok_true(self):
        self.url = "https://raw.githubusercontent.com/RafaelBarreroBosonit/prueba_swagger/master/csvs/numeros.csv"
        c = media_csv_url(CalcularMediaCsvUrl(self.url, True))
        expected_media = 4
        self.assertEqual(c.media, expected_media)

    def test_ok_no_bool(self):
        self.url = "https://raw.githubusercontent.com/RafaelBarreroBosonit/prueba_swagger/master/csvs/numeros.csv"
        c = media_csv_url(CalcularMediaCsvUrl(self.url))
        expected_media = 4.78
        self.assertEqual(c.media, expected_media)

    def test_error_in_csv(self):
        self.url = "https://raw.githubusercontent.com/RafaelBarreroBosonit/prueba_swagger/master/csvs/numeros_error.csv"
        c = media_csv_url(CalcularMediaCsvUrl(self.url))
        expected_error = Error('El archivo no es válido, contiene letras')
        expected_code = 400
        self.assertEqual(c[0], expected_error)
        self.assertEqual(c[1], expected_code)

    def test_error_in_url(self):
        self.url = "https://raw.githubusercontent.com/RafaelBarreroBosonit/prueba_swagger/master/csvs/numero_error.csv"
        c = media_csv_url(CalcularMediaCsvUrl(self.url))
        expected_error = Error('Archivo no encontrado')
        expected_code = 404
        self.assertEqual(c[0], expected_error)
        self.assertEqual(c[1], expected_code)

    def test_none(self):
        c = media_csv_url(CalcularMediaCsvUrl(None))
        expected_error = Error('La URL no es válida')
        expected_code = 404
        self.assertEqual(c[0], expected_error)
        self.assertEqual(c[1], expected_code)

    def test_string_none(self):
        c = media_csv_url(CalcularMediaCsvUrl("None"))
        expected_error = Error('La URL no es válida')
        expected_code = 404
        self.assertEqual(c[0], expected_error)
        self.assertEqual(c[1], expected_code)

    def test_empty(self):
        c = media_csv_url(CalcularMediaCsvUrl())
        expected_error = Error("La URL no es válida")
        expected_code = 404
        self.assertEqual(c[0], expected_error)
        self.assertEqual(c[1], expected_code)

    def test_list_as_string(self):
        c = media_csv_url(CalcularMediaCsvUrl('[1, "asdasd", "2",  5]'))
        expected_error = Error('La URL no es válida')
        expected_code = 404
        self.assertEqual(c[0], expected_error)
        self.assertEqual(c[1], expected_code)


if __name__ == '__main__':
    unittest.main()
