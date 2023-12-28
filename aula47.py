def sum(x,y):
    return x + y

def mult(x,y):
    return x * y

def execute(function, x):
    def internal(y):
        return function(x,y)
    return internal

sum_with_five = execute(sum, 5)
mult_with_ten = execute(mult, 10)

print(sum_with_five(10))
print(mult_with_ten(10))
