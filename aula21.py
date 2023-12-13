#Ex depois de ver a aula
import os

palavra = 'perfume'
letra_acertada = ''
count = 0
while True:
    letra_user = input('Digite uma letra: ')
    count += 1
    if len(letra_user) > 1:
        print('Digite apenas 1 letra.')
        continue

    if letra_user in palavra:
        letra_acertada += letra_user

    palavra_formada = ''
    for letra in palavra:
        if letra in letra_acertada:
            palavra_formada += letra
        else:
            palavra_formada += '*'
    print(palavra_formada)
    if palavra_formada == palavra:
        os.system('cls')
        print('Você ganhou, parabéns!\n'\
              f'Tentativas: {count}\n'
              f'A palavra era: {palavra_formada}')
        letra_acertada = ''
        count = 0