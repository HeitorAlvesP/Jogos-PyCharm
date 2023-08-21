def jokenpo():

    import funcoes
    fim = ''
    while True:

        if fim == 'N':
            break

        from random import randint
        from time import sleep

        itens = ['Pedra', 'Papel', 'Tesoura']
        pc = randint(0, 2)

        funcoes.cabeçalho2('\033[1;33mJOKENPO\033[m')
        print('''Suas opções:
\033[1:35m[ 0 ]\033[m Pedra
\033[1:35m[ 1 ]\033[m Papel
\033[1:35m[ 2 ]\033[m Tesoura''')

        jogador = int(input('Qual é a sua jogada -> '))

        print('\033[1:35mJO\033[m')
        sleep(0.5)
        print('\033[1:35mKEN\033[m')
        sleep(0.5)
        print('\033[1:35mPO!!!\033[m')

        print('\033[1:36m-=\033[m ' * 11)
        print('O computador jogou \033[1:36m{}\033[m'.format(itens[pc]))
        print('O jogador jogou \033[1:36m{}\033[m'.format(itens[jogador]))

        resultado = [
            "EMPATE",
            "VITÓRIA",
            "DERROTA"
        ]

        if pc == jogador:
            print('\033[1:33m{}\033[m'.format(resultado[0]))
        elif (pc == 0 and jogador == 2) or (pc == 1 and jogador == 0) or (pc == 2 and jogador == 1):
            print('\033[1:31m{}\033[m'.format(resultado[2]))
        else:
            print('\033[1:32m{}\033[m'.format(resultado[1]))

        print('\033[1:36m-=\033[m ' * 11)
        fim = str(input('Deseja jogar dnovo [s/n] : ')).upper().strip()[0]
        print('Obrigado por jogar')


if __name__ == "__main__":
    jokenpo()
