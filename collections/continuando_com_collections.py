from email.policy import default

usuarios_data_science = [15, 23, 43, 56]

usuarios_machine_learning = [13, 23, 43, 42]

assistiram = usuarios_data_science.copy()

assistiram.extend(usuarios_data_science)

print(assistiram)

print(set(assistiram))

print(set([1, 2, 3, 4, 1]))

print({1, 2, 3, 4, 1})

print(type({1, 2, 3, 4, 1}))

usuarios_data_science = {15, 23, 43, 56}

usuarios_machine_learning = {13, 23, 56, 42}

# usuarios_machine_learning[3]  # no set não existe posição. Dará TypeError

for usuario in set(assistiram):
    print(usuario)

print(usuarios_data_science | usuarios_machine_learning)

print(usuarios_data_science & usuarios_machine_learning)

print(usuarios_data_science - usuarios_machine_learning)

usuarios = {1, 5, 76, 34, 52, 13, 17}

print(len(usuarios))

usuarios.add(13)

print(len(usuarios))

usuarios.add(765)

print(len(usuarios))

print(usuarios)

usuarios = frozenset(usuarios)  # impossibilita que se adicione item ao set e o tipo vira frozenset

type(usuarios)

# usuarios.add(134)

meu_texto = "Bem vindo meu nome é Guilherme, eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"

print(meu_texto.split())

print(set(meu_texto.split()))

aparicoes = {
    "Guilherme": 1,
    "cachorro": 2,
    "nome": 2,
    "vindo": 1,
}

print(type(aparicoes))

print(aparicoes['Guilherme'])

aparicoes['Carlos'] = 1

print(aparicoes)

aparicoes['Carlos'] = 2

print(aparicoes)

del aparicoes['Carlos']

print(aparicoes)

print('Carlos' in aparicoes)

for elementos in aparicoes:
    print(elementos)

for elementos in aparicoes.keys():
    print(elementos)

for elementos in aparicoes.values():
    print(elementos)

print(1 in aparicoes.values())

for elementos in aparicoes.items():
    print(elementos)

for chave, valor in aparicoes.items():
    print(chave, '=', valor)

print([f'Palavra {chave}' for chave in aparicoes.keys()])

meu_texto = meu_texto.lower()

aparicoes = {}

for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)

from collections import defaultdict

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
    aparicoes[palavra] += 1

print(aparicoes)


class Conta:
    def __init__(self):
        print('Criando conta.')


contas = defaultdict(Conta)

print(contas[15])

from collections import Counter

aparicoes = Counter(meu_texto.split())

print(aparicoes)
