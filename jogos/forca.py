import random


def jogar():
    print('*********************************')
    print('***Bem vindo ao jogo de Forca!***')
    print('*********************************')

    arquivo = open("palavras.txt", "r", encoding='UTF-8')

    # o .strip() é necessário para excluir o \n do final de cada linha
    palavras = [linha.strip() for linha in arquivo]

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ["_" for _ in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = input("Qual letra?").upper().strip()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print(f"Ops, você errou! Faltam {6 - erros} tentativas.")

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        if acertou:
            print("Você ganhou!")
        else:
            print("Você perdeu!")
        print(letras_acertadas)

    print('Fim do jogo')


if __name__ == '__main__':
    jogar()
