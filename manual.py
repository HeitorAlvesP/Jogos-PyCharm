from funcoes import *


def manual():
    from time import sleep
    c = ('\033[m',    #0 - sem cor
         '\033[1;31m', #1 - vermelho
         '\033[1;32m', #2 - verde
         '\033[1;33m', #3 - amarelo
         '\033[1;34m', #4 - azul
         '\033[1;35m', #5 - roxo
         '\033[1;36m', #6 - azul claro
         '\033[1;37m' #7 - cinza
         )


    def ajuda(com):
        titulo(f'Acessando o manual do comando \'{com}\'', 2)
        help(com)
        sleep(0.6)

    def titulo(msg, cor=0):
        tam = len(msg) + 4
        print(c[cor], end='')
        print('~' * tam)
        print(f'  {msg}')
        print('~' * tam)
        print(c[0], end='')
        sleep(0.3)


    comando = ''
    while True:
        cabeçalho('SISTEMA DE AJUDA PyHELP')
        comando = str(input('função ou Biblioteca -> '))
        if comando.upper() == 'FIM':
            break
        else:
            ajuda(comando)
    titulo('ATE LOGO', 1)


if __name__ == "__main__":
    manual()
