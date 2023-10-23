import unittest

def é_par(numero):
    return numero % 2 == 0

class TestÉPar(unittest.TestCase):

    def test_numero_par(self):
        resultado = é_par(4)
        self.assertTrue(resultado)

    def test_numero_impar(self):
        resultado = é_par(7)
        self.assertFalse(resultado)

    def test_zero(self):
        resultado = é_par(0)
        self.assertTrue(resultado)

    def test_numero_negativo_par(self):
        resultado = é_par(-6)
        self.assertTrue(resultado)

    def test_numero_negativo_impar(self):
        resultado = é_par(-3)
        self.assertFalse(resultado)

if __name__ == '__main__':
    unittest.main()