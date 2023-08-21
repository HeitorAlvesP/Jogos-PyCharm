import funcoes


def adivinha():

    from random import randint
    fim = ' '
    while True:

        if fim == 'N':
            print('Obrigado por jogar')
            break

        pc = int(randint(1, 100))
        #print(pc)
        vidas = 0
        chute = 0

        funcoes.cabeçalho2('\033[1;33mJOGO DO ADIVINHA\033[m')
        print('''  COMEÇAR
[0]_SAIR_
[1]_FACIL_(7vidas)
[2]_MEDIO_(5vidas)
[3]_DIFICL_(3vidas) ''')

        player = int(input('Escolha -> '))

        if player == 0:
            print('Obrigado por jogar')
            break
        elif player == 1:
            vidas = 7
        elif player == 2:
            vidas = 5
        elif player == 3:
            vidas = 3
        '''else:
            print('ERRO...', end='')'''

        while True:

            if player != 0:
                chute = int(input('Digite seu chute : '))
                vidas -= 1
                if vidas == 0:
                    print(f'O numero pensado foi {pc}, sinto muito')
                    break
                elif chute == pc:
                    print(f'Vocé ACERTOU!! O numero pensado é {pc}')
                    break
                else:
                    print(f'Vocé perdeu uma vida, agora vocé tem {vidas} vidas')
                    if chute > pc:
                        print('(o numero é menor)', end='')
                    elif chute < pc:
                        print('(o numero é maior)', end='')

        fim = str(input('Deseja jogar dnovo [s/n]: ')).upper().strip()[0]
    print('FIM')


if __name__ == "__main__":
    adivinha()
