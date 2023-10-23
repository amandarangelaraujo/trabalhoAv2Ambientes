import unittest

def inverter_string(texto):
    return texto[::-1]

class TestInverterString(unittest.TestCase):

    def test_inverter_string(self):
        resultado = inverter_string("Hello, World!")
        self.assertEqual(resultado, "!dlroW ,olleH")

if __name__ == '__main__':
    unittest.main()

