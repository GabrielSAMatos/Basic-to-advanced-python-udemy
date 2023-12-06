"""
Introduction to try/except
try -> trying to execute the code
except -> an error occurred when trying to execute
"""
while True:
    try:
        n_str = input('Digit which number u want know double: ')
        n_float = float(n_str)
        print(f'FLOAT: {n_float}')
        print(f'The double of {n_float} is {n_float*2}')
        break
        
    except:
        print(f'Digit a number!')