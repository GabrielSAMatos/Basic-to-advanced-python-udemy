#Calculator with while

def sum(choice, num1, num2):
    if choice == "+":
        print(f'\n{num1} + {num2} = {num1 + num2}\n')

def sub(choice, num1, num2):
    if choice == "-":
        print(f'\n{num1} - {num2} = {num1 - num2}\n')

def mult(choice, num1, num2):
    if choice == "*":
        print(f'\n{num1} * {num2} = {num1 * num2}\n')

def div(choice, num1, num2):
    if choice == "/":
        print(f'\n{num1} / {num2} = {num1 / num2}\n')

def line():
    print('='*15)

def are_number(num1, num2):
    if (num1.isdigit() and num2.isdigit()):
        return True
    print('Have a invalid number. Check and digit again.')
    False

val_num = None

while True:
    try:
        num1 = input('Enter a first number: ')
        num2 = input('Enter a second number: ')
        num1_float = float(num1)
        num2_float = float(num2)
        val_num = True
    except:
        print('One or both numbers entered are invalid. Please type again.')
        val_num = None

    if val_num == None:
        continue
    line()
    cal_fun = input('Choose an operation.'
                    "\nFor sum, digit: +"
                    '\nFor sub, digit: -'
                    '\nFor mult, digit: *'
                    '\nFor div, digit: /\n')
    
    if not cal_fun[0] in ('+-*/'):
        print('Invalid operator.')
        continue

    if len(cal_fun) > 1:
        print('Enter just one operator.')
        continue

    line()
    sum(cal_fun,num1_float, num2_float)
    sub(cal_fun,num1_float, num2_float)
    mult(cal_fun,num1_float, num2_float)
    div(cal_fun,num1_float, num2_float)
    exit = input('Do u want exit? If yes, Digit "exit": ')
    if exit == 'exit':
        break