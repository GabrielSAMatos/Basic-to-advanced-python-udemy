
# num = input('Enter a integer: ')

# def is_even(num):
#     if int(num) % 2 == 0:
#         return True

# if not num.isdigit():
#     print('This is not a whole number.')
# else:
#     if is_even(num):
#         print('The number is even.')
#     else: print('The number is odd.')


# time = input('What time is it? ')
# time_int = int(time)

# def whats_time(time):
#     if time <= 11:
#         return 'morning'
#     elif time <= 17:
#         return 'afternoon'
#     else:
#         return 'night'
    
# print(f'Good {whats_time(time_int)}.')



name = input('Digit your fisrt name: ')
name_size = len(name)

def size_name(name):
    if name <= 4:
        return 'Your first name is short!'
    elif name <= 6:
        return 'Your first name is normal!'
    else:
        return 'Your first name is very big!'

print(size_name(name_size))
