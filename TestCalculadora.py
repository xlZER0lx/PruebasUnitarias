import unittest

class TestCalculadora(unittest.TestCase):

    def test_sumar_de_2_mas_2(self):
        calc = Calculadora()

        resultado = calc.sumar(2, 2)

        self.assertEqual(4, resultado)


if __main__ == ' __main__':
    unittest.main()
