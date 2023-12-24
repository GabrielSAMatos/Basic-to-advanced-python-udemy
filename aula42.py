def d_is_zero(d):
    if d ==0: 
        raise ZeroDivisionError('U are trying to divide by 0')
    return True

def int_float(n):
    type_n = type(n)
    if not isinstance(n, (int, float)):
        raise TypeError(f'"{n}" are not int or float'
                        f'"{type_n.__name__}" sent.')
    return True


def divide(n, d):
    d_is_zero(d)
    int_float(n)
    int_float(d)
    return n/d
    
print(divide(9,'1'))