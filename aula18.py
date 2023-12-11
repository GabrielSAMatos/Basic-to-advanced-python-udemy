sentence = """
    O Python é uma linguagem de programação 
    multiparadigma. 
    Python foi criado por Guido van Rossum
    """

i = 0
count = 0
letter = input('Enter a letter that u want to know how many '
                'times is repeated in the setence.: ').lower()

for i in range (len(sentence)):
    if sentence[i].lower() == letter:
        count += 1


if count > 1:
    print(f'In the sentence "{sentence}".\n\nThere are {count} letters "{letter}".')

elif count == 1:
    print(f'In the sentence "{sentence}".\n\nThere is {count} letter "{letter}".')

else:   print('this letter was not found.')
