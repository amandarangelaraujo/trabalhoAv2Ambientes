import unittest

def fatorial(n):
    if n == 0:
        return 1
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

class TestFatorial(unittest.TestCase):

    def test_fatorial_zero(self):
        resultado = fatorial(0)
        self.assertEqual(resultado, 1)

    def test_fatorial_um(self):
        resultado = fatorial(1)
        self.assertEqual(resultado, 1)

    def test_fatorial_positivo(self):
        resultado = fatorial(5)
        self.assertEqual(resultado, 120)

if __name__ == '__main__':
    unittest.main()
