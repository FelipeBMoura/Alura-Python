class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo o objeto... {self}")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f"Saldo de {self.saldo} do titular {self.titular}")

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print(f"Saldo insuficiente para sacar {valor} do titular {self.titular}")
