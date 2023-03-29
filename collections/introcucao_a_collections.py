from abc import ABCMeta, abstractmethod


class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return f'[>>Código {self._codigo} Saldo {self._saldo}<<]'


class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2


class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


class ContaInvestimento(Conta):
    pass


# ContaInvestimento(17) # Não roda pois falta implementar o método abstrato da classe abstrata

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print(conta16)

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
print(conta17)

contas = [conta16, conta17]

for conta in contas:
    conta.passa_o_mes()  # duck typing
    print(conta)

import array as arr

# evitamos usaar array puro. Paddrão é usar Numpy
print(arr.array('d', [1, 3.5]))  # 'd' significa double, conforme documentação

# print(arr.array('d', [1, 3.5, "Guilherme"]))

import numpy as np

numeros = np.array([[1, 3.5]])

print(numeros)

numeros = numeros + 3

print(numeros)
