import unittest

def somar_lista(lista):
    soma = 0
    for elemento in lista:
        soma += elemento
    return soma

class TestSomarLista(unittest.TestCase):

    def test_somar_lista(self):
        lista = [1, 2, 3, 4, 5]
        resultado = somar_lista(lista)
        self.assertEqual(resultado, 15)

if __name__ == '__main__':
    unittest.main()