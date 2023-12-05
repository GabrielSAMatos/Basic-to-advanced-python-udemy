first_value = input('Digit a value: ')
second_value = input('Digit another value: ')

int_first_value = int(first_value)
int_second_value = int(second_value)

if int_first_value > int_second_value:
    print(f'{first_value=} is greater than the {second_value=}')

elif int_first_value < int_second_value:
    print(f'{second_value=} is greater than the {first_value=}')

else:
    print(f'{first_value=} is equal to {second_value=}')
