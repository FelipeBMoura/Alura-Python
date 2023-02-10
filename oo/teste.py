def cria_conta(numero, titular, saldo, limite):
    conta = {
        'numero': numero,
        'titular': titular,
        'saldo': saldo,
        'limite': limite
    }
    return conta


def deposita(conta, valor):
    conta['saldo'] += valor
    return conta


def saca(conta, valor):
    if conta['saldo'] >= valor:
        conta['saldo'] -= valor
        return conta
    else:
        return 'Saldo insuficiente'


def extrato(conta):
    print(f'Numero: {conta["numero"]}')
    print(f'Titular: {conta["titular"]}')
    print(f'Saldo: {conta["saldo"]}')
    print(f'Limite: {conta["limite"]}')
