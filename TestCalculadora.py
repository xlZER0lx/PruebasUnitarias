import unittest

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_sumar_de_2_mas_2(self):
        resultado = self.calc.sumar(2, 2)

        self.assertEqual(4, resultado)
        

    def test_sumar_de_3_mas_3(self):
        resultado = self.calc.sumar(3, 3)

        self.assertEqual(6, resultado)


    def test_sumar_de_5_mas_5(self):
        resultado = self.calc.sumar(5, 5)

        self.assertEqual(10, resultado)

    def test_resta_de_5_menos_3(self):
        resultado = self.calc.restar(5, 3)

        self.assertEqual(2, resultado)

    def test_resta_de_15_menos_8(self):
        resultado = self.calc.restar(15, 8)

        self.assertEqual(7, resultado)

class Calculadora():

    def sumar(self, num1, num2):
        return num1 + num2

    def restar(self, num1, num2):
        return num1 - num2

if __name__ == '__main__':
    unittest.main()
