import unittest

from swagger_server.controllers.src.cuadrados_numeros import cuadrados_numeros
from swagger_server.models import CalcularCuadradoArray, Error


class TestCuadradoNumeros(unittest.TestCase):

    def test_ok(self):
        c = cuadrados_numeros([2])
        expected_total = 1
        expected_total_resultados = [CalcularCuadradoArray(4, 2)]
        self.assertEqual(c.total, expected_total)
        self.assertEqual(c.resultados, expected_total_resultados)

    def test_ok2(self):
        c = cuadrados_numeros([2, 4, 6])
        expected_total = 3
        expected_total_resultados = [CalcularCuadradoArray(4, 2), CalcularCuadradoArray(16, 4),
                                     CalcularCuadradoArray(36, 6)]
        self.assertEqual(c.total, expected_total)
        self.assertEqual(c.resultados, expected_total_resultados)

    def test_none(self):
        c = cuadrados_numeros(None)
        expected_error = Error('No se ha introducido números')
        expected_code = 400
        self.assertEqual(c[0], expected_error)
        self.assertEqual(c[1], expected_code)

    def test_list_none(self):
        c = cuadrados_numeros([None])
        expected_error = Error('Los datos introducidos no son válidos')
        expected_code = 400
        self.assertEqual(c[0], expected_error)
        self.assertEqual(c[1], expected_code)

    def test_list_empty(self):
        c = cuadrados_numeros([])
        expected_error = Error('No se ha introducido números')
        expected_code = 400
        self.assertEqual(c[0], expected_error)
        self.assertEqual(c[1], expected_code)

    def test_list_string(self):
        c = cuadrados_numeros([1, "asdasd", "2",  5])
        expected_error = Error('No se admiten letras')
        expected_code = 400
        self.assertEqual(c[0], expected_error)
        self.assertEqual(c[1], expected_code)


if __name__ == '__main__':
    unittest.main()
