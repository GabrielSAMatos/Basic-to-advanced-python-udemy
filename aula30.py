def create_multiplier(multiplier):
    def multiply(number):
        return multiplier * number
    return multiply

multiply_for_2 = create_multiplier(2)
multiply_for_3 = create_multiplier(3)
multiply_for_4 = create_multiplier(4)

print(multiply_for_2(3))
print(multiply_for_3(5))
print(multiply_for_4(10))
