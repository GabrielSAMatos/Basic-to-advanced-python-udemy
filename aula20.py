#Ex antes de ver a aula
import os

def limpar_terminal():
    os.system('cls')

secret_class = ['*', '*', '*', '*', '*', '*', '*']
secret_word = ['p', 'e', 'r', 'f', 'u', 'm', 'e']
count = 0

def check_secret(letter):
    for i in range (len(secret_word)):
        if letter == secret_word[i]:
            secret_class[i] = letter

def win():
    if secret_class == secret_word:
        limpar_terminal()
        print('You win, congratulations!\n'\
            'The word was: perfume\n'\
            f'Attempts: {count}')
        return True

while True:
    try_letter = input('Enter one letter: ')
    if len(try_letter) > 1:
        print('One letter please.')
        continue 
    
    if try_letter in secret_word:
        check_secret(try_letter)
    print('Palavra formatada: ', end='')
    for i in secret_class:
        print(i, end='')
    print('')
    count += 1
    win()
    if win() == True:
        secret_class = ['*', '*', '*', '*', '*', '*', '*']
        count = 0 