import unittest

def é_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True

    if numero % 2 == 0 or numero % 3 == 0:
        return False

    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6

    return True

class TestÉPrimo(unittest.TestCase):

    def test_numero_primo(self):
        resultado = é_primo(5)
        self.assertTrue(resultado)

    def test_numero_nao_primo(self):
        resultado = é_primo(6)
        self.assertFalse(resultado)

    def test_numero_negativo(self):
        resultado = é_primo(-7)
        self.assertFalse(resultado)

    def test_numero_um(self):
        resultado = é_primo(1)
        self.assertFalse(resultado)

    def test_numero_zero(self):
        resultado = é_primo(0)
        self.assertFalse(resultado)

if __name__ == '__main__':
    unittest.main()