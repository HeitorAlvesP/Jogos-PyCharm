import funcoes
from funcoes import *
import random


def enforca():

    funcoes.cabeçalho2('\033[1;33mJOGO DA FORCA\033[m')
    palavra_secreta = carrega_palavra_secreta()

    letra_certa = ['_' for letra in palavra_secreta]
    print(letra_certa)

    enforcou = False
    acertou = False
    erros = 0
    
    while not enforcou and not acertou:

        chute = str(input('Qual seu chute -> ')).strip().upper()[0]

        if chute in palavra_secreta:
            marca_chute_certo(chute, palavra_secreta, letra_certa)

        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = '_' not in letra_certa
        print(letra_certa)

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)


if __name__ == "__main__":
    enforca()
