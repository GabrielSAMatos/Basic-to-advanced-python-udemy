name = input('Digit your name: ')
age = input('Digit your age: ')

if name and age:
    print(f'Your name is {name}')
    print(f'Your reversed name is: {name[::-1]}')

    if ' ' in name:
        print(f'Your name have empty spaces.')
    else:
        print(f"Your name don't have empty spaces.")

    print(f'Your name have {len(name)} letters.')
    print(f'The first letter in your name is: {name[0]}')
    print(f'The last letter in your name is: {name[-1]}')

else:
    print('Sorry, u left empty fields')
