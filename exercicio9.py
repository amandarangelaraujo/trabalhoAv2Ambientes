import unittest

def calcular_média(lista):
    if not lista:
        return None
    return sum(lista) / len(lista)

class TestCalcularMédia(unittest.TestCase):

    def test_calcular_média_inteiros(self):
        lista = [1, 2, 3, 4, 5]
        resultado = calcular_média(lista)
        self.assertEqual(resultado, 3.0)

    def test_calcular_média_ponto_flutuante(self):
        lista = [1.5, 2.5, 3.5, 4.5, 5.5]
        resultado = calcular_média(lista)
        self.assertAlmostEqual(resultado, 3.5, places=1)

    def test_calcular_média_lista_vazia(self):
        lista = []
        resultado = calcular_média(lista)
        self.assertIsNone(resultado)

    def test_calcular_média_um_elemento(self):
        lista = [42]
        resultado = calcular_média(lista)
        self.assertEqual(resultado, 42.0)

if __name__ == '__main__':
    unittest.main()
