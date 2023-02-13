class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo o objeto... {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo de {self.__saldo} do titular {self.__titular}")

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print(f"Saldo insuficiente para sacar {valor} do titular {self.__titular}")

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
