from jogo_forca import *
from jogo_jokenpo import *
from jogo_adivinha_vs3 import *
import random


def linha(tam=42):
    return '\033[36m-\033[m' * (tam - 7)


def linha2(tam=42):
    return '\033[1;35m=\033[m' * (tam - 7)


def cabeçalho2(txt):
    print(linha2())
    print(txt.center(42))
    print(linha2())


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor digite um valor inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usário.\033[m')
            return 0
        else:
            return n


def carrega_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []

    for lynha in arquivo:
        lynha = lynha.strip()
        palavras.append(lynha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def marca_chute_certo(chute, palavra_secreta, letra_certa):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letra_certa[index] = letra
        index += 1


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("\033[1;31m    _______________         ")
    print("\033[1;31m   /               \       ")
    print("\033[1;31m  /                 \      ")
    print("\033[1;31m//                   \/\  ")
    print("\033[1;31m\|   XXXX     XXXX   | /   ")
    print("\033[1;31m |   XXXX     XXXX   |/     ")
    print("\033[1;31m |   XXX       XXX   |      ")
    print("\033[1;31m |                   |      ")
    print("\033[1;31m \__      XXX      __/     ")
    print("\033[1;31m   |\     XXX     /|       ")
    print("\033[1;31m   | |           | |        ")
    print("\033[1;31m   | I I I I I I I |        ")
    print("\033[1;31m   |  I I I I I I  |        ")
    print("\033[1;31m   \_             _/       ")
    print("\033[1;31m     \_         _/         ")
    print("\033[1;31m      \_______/           \033[m")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("\033[1;33m       ___________      ")
    print("\033[1;33m      '._==_==_=_.'     ")
    print("\033[1;33m      .-\\:      /-.    ")
    print("\033[1;33m     | (|:.     |) |    ")
    print("\033[1;33m      '-|:.     |-'     ")
    print("\033[1;33m        \\::.    /      ")
    print("\033[1;33m         '::. .'        ")
    print("\033[1;33m           ) (          ")
    print("\033[1;33m         _.' '._        ")
    print("\033[1;33m        '-------'       \033[m")


def desenha_forca(erros):
    print("\033[1;34m  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print('\033[m')
