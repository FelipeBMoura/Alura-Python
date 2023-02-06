def jogar():
    print('*********************************')
    print('***Bem vindo ao jogo de Forca!***')
    print('*********************************')

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = input("Qual letra?").upper().strip()
        index = 0
        for letra in palavra_secreta:
            if chute == letra:
                letras_acertadas[index] = letra
            index = index + 1
        print(letras_acertadas)

    print('Fim do jogo')


if __name__ == '__main__':
    jogar()
