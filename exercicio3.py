import unittest

class Calculadora:

    def adicao(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        if b == 0:
            raise ValueError("Não é possível dividir por zero")
        return a / b

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calculadora = Calculadora()

    def test_adicao(self):
        resultado = self.calculadora.adicao(3, 4)
        self.assertEqual(resultado, 7)

    def test_subtracao(self):
        resultado = self.calculadora.subtracao(5, 2)
        self.assertEqual(resultado, 3)

    def test_multiplicacao(self):
        resultado = self.calculadora.multiplicacao(4, 3)
        self.assertEqual(resultado, 12)

    def test_divisao(self):
        resultado = self.calculadora.divisao(10, 2)
        self.assertEqual(resultado, 5)

    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            self.calculadora.divisao(5, 0)

if __name__ == '__main__':
    unittest.main()