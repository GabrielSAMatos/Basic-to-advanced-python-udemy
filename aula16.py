name = 'Gabriel Matos'
size_name = len(name)
new_name = ''
count = 0

while count < size_name:
    new_name += f'*{name[count]}'
    count += 1
new_name += '*'
print(new_name)