import unittest

def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0

    for letra in texto:
        if letra in vogais:
            contador += 1

    return contador

class TestContarVogais(unittest.TestCase):

    def test_contar_vogais_mistas(self):
        resultado = contar_vogais("Hello, World!")
        self.assertEqual(resultado, 3)

    def test_sem_vogais(self):
        resultado = contar_vogais("Rhythm")
        self.assertEqual(resultado, 0)

    def test_todas_vogais_minusculas(self):
        resultado = contar_vogais("aeiou")
        self.assertEqual(resultado, 5)

    def test_todas_vogais_maiusculas(self):
        resultado = contar_vogais("AEIOU")
        self.assertEqual(resultado, 5)

    def test_string_vazia(self):
        resultado = contar_vogais("")
        self.assertEqual(resultado, 0)

if __name__ == '__main__':
    unittest.main()