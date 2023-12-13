import os

shopping_lista = []

while True:
    option = input('Select one option\n'\
               '[i]sert [e]rased [l]ist: ')

    if option == 'i':
        os.system('cls')
        value = input('Value: ')
        shopping_lista.append(value)

    elif option == 'e':
        erase = input('Chose the index to delete: ')
        if (erase.isdigit()) and (int(erase) < len(shopping_lista)):
            for i, valor in enumerate(shopping_lista):
                if int(erase) == i:
                    shopping_lista.remove(valor)
        else:
            print("Unable to delete this index")
            
    elif option == 'l':
        os.system('cls')
        if len(shopping_lista) < 1:
                print('Nothing to list')
        else: 
            for i, valor in enumerate(shopping_lista):
                print(i, valor)
    else:
        print('Please chose: e, i or l')
