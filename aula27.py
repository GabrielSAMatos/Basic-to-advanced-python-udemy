def mult(*args):
    aws = 1
    for number in args:
        aws *= number
    return aws 

multi = mult(1, 2, 3, 4, 5, 0)
print(multi) 

def is_par(number):
    even = 'even' if number % 2 == 0 else 'odd'
    return f'{number} is {even}'

number = is_par(3)

print(number)

