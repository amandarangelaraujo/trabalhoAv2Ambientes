import unittest

class ContaBancária:

    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor

    def saque(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor

class TestContaBancária(unittest.TestCase):

    def setUp(self):
        self.conta = ContaBancária(1000)

    def test_deposito_valido(self):
        self.conta.deposito(500)
        self.assertEqual(self.conta.saldo, 1500)

    def test_deposito_valor_negativo(self):
        self.conta.deposito(-200)
        self.assertEqual(self.conta.saldo, 1000)

    def test_saque_valido(self):
        self.conta.saque(300)
        self.assertEqual(self.conta.saldo, 700)

    def test_saque_valor_maior_que_saldo(self):
        self.conta.saque(1500)
        self.assertEqual(self.conta.saldo, 1000)

    def test_saque_valor_negativo(self):
        self.conta.saque(-200)
        self.assertEqual(self.conta.saldo, 1000)

if __name__ == '__main__':
    unittest.main()