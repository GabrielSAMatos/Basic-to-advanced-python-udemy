def salutation(msg, name):
    return f'{msg}, {name}!'

def execute(function,*args):
    return function(*args)


v = execute(salutation, 'Good Morning', 'Gabriel')
print(v)