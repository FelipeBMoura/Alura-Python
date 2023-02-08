def jogar():
    print('*********************************')
    print('***Bem vindo ao jogo de Forca!***')
    print('*********************************')

    palavra_secreta = "banana".upper()
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
