import unittest

def soma(a, b):
    return a + b

class TestSoma(unittest.TestCase):

    def test_soma_positivos(self):
        resultado = soma(3, 4)
        self.assertEqual(resultado, 7)

    def test_soma_negativos(self):
        resultado = soma(-2, -5)
        self.assertEqual(resultado, -7)

    def test_soma_misto(self):
        resultado = soma(5, -3)
        self.assertEqual(resultado, 2)

if __name__ == '__main__':
    unittest.main()
