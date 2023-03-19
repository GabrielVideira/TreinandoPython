import random


def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def carregar_palavra_secreta():
    arquivo = open("palavras.txt" "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()


def inicializa_letras_acertadas(palavra):
    letras_acertadas = ["_" for letra in palavra]


def pedir_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
        index = index + 1


def jogar():

    imprime_mensagem_abertura()

    palavra_secreta = carregar_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    while (not acertou and not enforcou):

        chute = pedir_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros = erros + 1
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if (acertou):
        print("Você descobriu a palavra Secreta!")
    else:
        print("Você perdeu")


if (__name__ == "__main__"):
    jogar()
