#Check CPF
cpf = '111.111.111-11'\
    .replace('.', '')\
    .replace('-', '')\
    .replace(' ', '')   
digit_1 = 0
digit_2 = 0
count = []
everything_equal = cpf[0] * len(cpf)

if everything_equal == cpf:
    print('Invalid CPF.')
    exit()

for i in range(10,1, -1): 
    count.append(i) 

for i in range(9):
    digit_1 += (int(cpf[i]) * count[i])
res1 = (digit_1 * 10) % 11
res1 = res1 if res1 <= 9 else 0

if res1 != int(cpf[-2]):
    print('Invalid CPF.')
    exit()

count.insert(0, 11)

for i in range(10):
    digit_2 += (int(cpf[i]) * count[i])
res2 = (digit_2 * 10) % 11
res2 = res2 if res2 <= 9 else 0

if res2 == int(cpf[-1]):
    print('Valid CPF.')
else:
    print('Invalid CPF.')