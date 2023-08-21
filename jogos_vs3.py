from jogo_forca import *
from jogo_jokenpo import *
from jogo_adivinha_vs3 import *
from manual import *
from funcoes import *


def jogos():

    # PROGRAMA PRINCIPAL
    cabeçalho2('\033[1;35mMENU PRINCIPAL\033[m')
    while True:
        cabeçalho('''OQUE DESEJA ACESSAR 
1_ JOGOS
2_ MANUAL DE FUNÇOES
0_ SAIR ''')
        opcao = leiaint('Acessar -> ')

        if opcao == 1:
            while True:
                cabeçalho('''Escolha o jogo
1_ FORCA
2_ ADIVINHA
3_ JOKENPO
0_ SAIR''')
                escolha = leiaint('Jogar -> ')
                if escolha == 1:
                    enforca()
                if escolha == 2:
                    adivinha()
                if escolha == 3:
                    jokenpo()
                if escolha == 0:
                    print('Obrigado volte sempre')
                    break

        elif opcao == 2:
            manual()

        elif opcao == 0:
            print('Obrigado volte sempre')
            break

        else:
            print('\033[1;31mInforme uma opçao correta\033[m')

if __name__ == "__main__":
    jogos()
