def execute(function, *args):
    return function(*args)

def sum(x,y):
    return x + y

def make_multiplier(multiplier):
    def multiply(num):
        return num * multiplier
    return multiply

print(execute(lambda x,y: x + y, 2,3))

print(execute(lambda x,y: x * y, 2,3))


def um(num):
    print()






