import unittest

def ordenar_lista(lista):
    return sorted(lista)

class TestOrdenarLista(unittest.TestCase):

    def test_ordenar_lista_desordenada(self):
        lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        resultado = ordenar_lista(lista)
        self.assertEqual(resultado, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_ordenar_lista_vazia(self):
        lista = []
        resultado = ordenar_lista(lista)
        self.assertEqual(resultado, [])

    def test_ordenar_lista_um_elemento(self):
        lista = [42]
        resultado = ordenar_lista(lista)
        self.assertEqual(resultado, [42])

    def test_ordenar_lista_ordenada(self):
        lista = [1, 2, 3, 4, 5]
        resultado = ordenar_lista(lista)
        self.assertEqual(resultado, [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()